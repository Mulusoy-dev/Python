import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtGui import QIcon

def window():
    app = QtWidgets.QApplication(sys.argv)
    win = QtWidgets.QMainWindow()

    win.setWindowTitle('First Application')
    win.setGeometry(250,250,600,600)

    
    win.setWindowIcon(QIcon('icon.png'))



    win.show()
    sys.exit(app.exec_())

window()    








