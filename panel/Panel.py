from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
from forms.frmPendaftaran import PendaftaranWindow
from forms.frmRegistrasi import RegistrasiWindow


dock = QtWidgets.QDockWidget()

def child_panels(self):   
    Pendaftaran_panel(self)
    Registrasi_panel(self)
    

#Pendaftaran
def Pendaftaran_panel(self):     
    Pendaftaran_widget =PendaftaranWindow()
    Pendaftaran_widget.select_data()
    self.centralwidget =Pendaftaran_widget
    self.centralwidget.setObjectName("centralwidget")
    self.widget = QtWidgets.QWidget(self.centralwidget)

def Pendaftaran_on(self):
    Pendaftaran_widget =PendaftaranWindow()
    Pendaftaran_widget.select_data()
    self.centralwidget =Pendaftaran_widget
    dock.setWidget(self.centralwidget)
    self.addDockWidget(Qt.LeftDockWidgetArea, dock)
    self.centralWidget()      


# Registrasi
def Registrasi_panel(self):
    Registrasi_widget = RegistrasiWindow()
    Registrasi_widget.select_data()
    self.centralwidget = Registrasi_widget
    self.centralwidget.setObjectName("centralwidget")
    self.widget = QtWidgets.QWidget(self.centralwidget)

def Registrasi_on(self):
    Registrasi_widget = RegistrasiWindow()
    Registrasi_widget.select_data()
    self.centralwidget = Registrasi_widget
    dock.setWidget(self.centralwidget)
    self.addDockWidget(Qt.LeftDockWidgetArea, dock)
    self.centralWidget()

