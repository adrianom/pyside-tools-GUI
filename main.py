# -*- coding: utf-8 -*-

#!/usr/bin/env python

#Created on 05/gen/2011
#Semplice interfaccia grafica per pyuic4
#Permette di aggiungere un'insieme di file di tipo ui(creati con QT Designer) e di convertirli
#in file python, utilizzando il comando pyuic4 -o <file_output.py> [-x] <file_input.ui>
#il parametro -o restituisce l'output su file
#il parametro -x inserisce codice extra per l'esecuzione della classe
#provato su windows 7 il 09/01/2011 , modifiche effettuate rimosso commands,aggiunto subprocess
#@authors: adrianom, bonaccorsop

import sys
from PySide import QtGui,QtCore
from mainw_ui import Ui_MainWindow
#import commands l'ho tolto perche funziona solo su UNIX, uso subprocess,moderna e multipiattaforma
import subprocess #http://docs.python.org/release/2.6.6/library/subprocess.html?highlight=subprocess
import shlex
import os

class pytgui(QtGui.QMainWindow,Ui_MainWindow):

    def __init__(self):

        #INITGFX
        super(pytgui,self).__init__()
        self.setupUi(self)
        self.fileviewlist=ListaDrag()
        self.listlayout.addWidget(self.fileviewlist)

        #INIT ATTRIBUTES
        self.__filelist=QtGui.QStandardItemModel() #File model [filepathname,type(ui or qrc)]
#        self.__execomm='pyside-uic-python3'
#        self.__execommrcc='pyside-rcc-python3'
        self.__execommrcc='pyside-rcc-python3'
        self.__execomm='pyside-uic-python3'
        self.__filelist.setHorizontalHeaderLabels(["Filename","Type"])

        #If OS is Mswindows then append .exe to program name
        if os.name=='nt':
            self.__execomm+='.exe'
            self.__execommrcc+='.exe'

        #SIGNAL CONNECTIONS
        self.addbtn.clicked.connect(self.Add_files)
        self.clearbtn.clicked.connect(self.Clear)
        self.removebtn.clicked.connect(self.Remove)
        self.gobtn.clicked.connect(self.Convert)
        self.fileviewlist.dropped[list].connect(self.AddDragged)

        #Carico informazioni inziali sulla statusbar: verifico l'esistenza di pyuic4 e ne visualizzo la versione
        try:
            #nuovo metodo per ricavare l'output di un comando eseguito
            print(subprocess.Popen([self.__execomm,"--version"],stdout=subprocess.PIPE).communicate()[0])
            self.statusbar.showMessage(str(subprocess.Popen([self.__execomm,"--version"],stdout=subprocess.PIPE).communicate()[0]))
        except IOError as e:
            print(e)
            self.statusbar.showMessage('Pyuic4 and PyRcc not found!')
            self.centralwidget.setEnabled(False)

        #CONNECT MODEL TO VIEW
        self.fileviewlist.setModel(self.__filelist)
        self.__CheckList()

    def __CheckList(self):
        flag=self.__filelist.rowCount()>0
        self.gobtn.setEnabled(flag)
        self.clearbtn.setEnabled(flag)
        self.removebtn.setEnabled(flag)

    def AddDragged(self,url_list):
        self.__Check_UIRCCfiles(url_list)
        self.fileviewlist.resizeColumnToContents(0)
        self.__CheckList()

    def Convert(self):
        myparams='' #lista parametri da passare a pyuic4
        if self.Xcheck.isChecked() :
            myparams='-x' #se checkato aggiunto alla stringa il parametro corrispondente
        self.Xcheck.setEnabled(False)

        for i  in range(self.__filelist.rowCount()):
            if self.__filelist.item(i,1).text()=="UI":
                bi=str(self.__filelist.item(i,0).text())
                #creo la stringa del path di output
                #unisco due parti di path con os.path,cosi in base al sistema operativo aggiunge lo slash o il backslash
                myoutfilename=os.path.join(os.path.dirname(bi) ,os.path.splitext(os.path.basename(bi))[0]+"_ui.py'")
                #creo la stringa che rappresenta il comando da eseguire
                mycommandline=self.__execomm+" -o"+" '"+myoutfilename+' '+myparams+' '+"'"+bi+"'"
                #preparo la stringa con http://docs.python.org/release/2.6.6/library/shlex.html#shlex.split
                #eseguo il comando con Popen
                subprocess.Popen(shlex.split(mycommandline))
            elif self.__filelist.item(i,1).text()=="RCC":
                bi=str(self.__filelist.item(i,0).text())
                #creo la stringa del path di output
                #unisco due parti di path con os.path,cosi in base al sistema operativo aggiunge lo slash o il backslash
                myoutfilename=os.path.join(os.path.dirname(bi) ,os.path.splitext(os.path.basename(bi))[0]+"_rc.py'")
                #creo la stringa che rappresenta il comando da eseguire
                mycommandline=self.__execommrcc+" -o"+" '"+myoutfilename+' '+"'"+bi+"'"
                #preparo la stringa con http://docs.python.org/release/2.6.6/library/shlex.html#shlex.split
                #eseguo il comando con Popen
                subprocess.Popen(shlex.split(mycommandline))
        self.Xcheck.setEnabled(True)


    def Remove(self):
        if(self.__filelist.rowCount()>0) and len(self.fileviewlist.selectedIndexes())>0:
            self.__filelist.takeRow(self.fileviewlist.selectedIndexes()[0].row())
        self.__CheckList()

    def Clear(self):
        self.__filelist.clear()
        self.__filelist.setHorizontalHeaderLabels(["Filename","Type"])
        self.__CheckList()

    def Add_files(self):
        nuovifiles=QtGui.QFileDialog.getOpenFileNames(self,"Add .ui, .qrc files...",sys.path[0],'QtDesigner UI files or QtResource QRC files (*.ui *.qrc)')[0]
        self.__Check_UIRCCfiles(nuovifiles)
        self.fileviewlist.resizeColumnToContents(0)
        self.__CheckList()

    def __Check_UIRCCfiles(self,myfilelist):
        #devo controllare se i file hanno l'intestazione xml per evitare di processare file,
        #con estensione, ui di altra natura

        for i in myfilelist:
            myitem=[]
            f=open(i,'r')
            line1=str.strip(f.readline())  #forma compattata
            line2=str.strip(f.readline())
            if (line1=='<?xml version="1.0" encoding="UTF-8"?>' and line2=='<ui version="4.0">') :
                ui_costant=QtGui.QStandardItem()
                ui_costant.setData("UI",QtCore.Qt.DisplayRole)
                ui_costant.setEditable(False)
                curfilename=QtGui.QStandardItem()
                curfilename.setData(str(i),QtCore.Qt.DisplayRole)
                curfilename.setEditable(False)
                myitem.append(curfilename)
                myitem.append(ui_costant)
                self.__filelist.appendRow(myitem)
            elif (line1=='<RCC>'):
                qrc_costant=QtGui.QStandardItem()
                qrc_costant.setData("RCC",QtCore.Qt.DisplayRole)
                qrc_costant.setEditable(False)
                curfilename=QtGui.QStandardItem()
                curfilename.setData(str(i),QtCore.Qt.DisplayRole)
                curfilename.setEditable(False)
                myitem.append(curfilename)
                myitem.append(qrc_costant)
                self.__filelist.appendRow(myitem)


#Definizione di una lista che supporta il draganddrop di file esterni                                
class ListaDrag(QtGui.QTreeView):
    dropped=QtCore.Signal((list,))

    def __init__(self,parent=None):
        super(ListaDrag,self).__init__(parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self,event):
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self,event):
        if event.mimeData().hasUrls:
            event.setDropAction(QtCore.Qt.CopyAction)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self,event):
        if event.mimeData().hasUrls:
            event.setDropAction(QtCore.Qt.CopyAction)
            event.accept()
            links=[]
            for url in event.mimeData().urls():
                links.append(str(url.toLocalFile()))
            self.dropped[list].emit(links)
        else:
            event.ignore()
