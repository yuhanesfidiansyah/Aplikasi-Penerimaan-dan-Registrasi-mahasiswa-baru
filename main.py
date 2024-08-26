import sys
from PyQt5.QtWidgets import *
#from forms.MainWindow import MainWindow
from forms.FrmLogin import WindowLogin

__author__ = 'yuhanes firdiansyah'

def main():
    a = QApplication(sys.argv)
    a.setQuitOnLastWindowClosed(True)
    login_window = WindowLogin()
    login_window.show()
    sys.exit(a.exec_())

main()