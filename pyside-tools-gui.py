#'''
#Created on 04/giu/2011
#
#@author: Adriano
#'''


import sys
from PySide import QtGui
from main import pytgui

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    app.setApplicationName("pyside-tools-gui")
    app.setApplicationVersion("0.2")
    mainWindow = pytgui()
    mainWindow.show()
    sys.exit(app.exec_())
