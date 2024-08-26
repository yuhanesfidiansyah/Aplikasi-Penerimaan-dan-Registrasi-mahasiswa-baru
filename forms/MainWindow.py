from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QKeySequence as QKSec
from GUI.Icons import get_icon
from GUI.RibbonButton import RibbonButton
from GUI.RibbonTextbox import RibbonTextbox
from GUI.RibbonWidget import *
from panel.Panel import *
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None)
        self.resize(1280, 800)
        self.setWindowTitle("Aplikasi Pendaftaran & Registrasi Mhs")
        self.setDockNestingEnabled(True)
        self.setWindowIcon(get_icon("k1"))
        child_panels(self)
        # -------------      actions       -----------------

        self._Pendaftaran_action = self.add_action("Pendaftaran", "pendaftaran", "Data pendaftaran mhs", True, self.on_Pendaftaran)
        self._Registrasi_action = self.add_action("Registrasi", "Registrasi", "Data registrasi", True, self.on_Registrasi_file)
        self._zoom_action = self.add_action("Umc", "umc", "Umc", True, self.on_zoom)
        self._k1_action = self.add_action("kelas K1", "k1", "KelasK1", True, self.on_k1)
        self._about_action = self.add_action("About", "about", "About QupyRibbon", True, self.on_about)
        self._license_action = self.add_action("umc", "umc", "Licenc for this software", True, self.on_license)
        self._exit_action = self.add_action("Exit", "exit", "Exit", True, self.app_exit)

        # Ribbon

        self._ribbon = RibbonWidget(self)
        self.addToolBar(self._ribbon)
        self.init_ribbon()

    def add_action(self, caption, icon_name, status_tip, icon_visible, connection, shortcut=None):
        action = QAction(get_icon(icon_name), caption, self)
        action.setStatusTip(status_tip)
        action.triggered.connect(connection)
        action.setIconVisibleInMenu(icon_visible)
        if shortcut is not None:
            action.setShortcuts(shortcut)
        self.addAction(action)
        return action

    def init_ribbon(self):
        home_tab = self._ribbon.add_ribbon_tab("Home")
        file_pane = home_tab.add_ribbon_pane("File")
        file_pane.add_ribbon_widget(RibbonButton(self, self._Pendaftaran_action, True))
        file_pane.add_ribbon_widget(RibbonButton(self, self._Registrasi_action, True))

        

        view_panel = home_tab.add_ribbon_pane("View")
        view_panel.add_ribbon_widget(RibbonButton(self, self._zoom_action, True))
        view_panel.add_ribbon_widget(RibbonButton(self, self._k1_action, True))
        view_panel.add_ribbon_widget(RibbonButton(self, self._exit_action, True))
        home_tab.add_spacer()

        about_tab = self._ribbon.add_ribbon_tab("About us ")
        info_panel = about_tab.add_ribbon_pane("Info")
        info_panel.add_ribbon_widget(RibbonButton(self, self._about_action, True))
        info_panel.add_ribbon_widget(RibbonButton(self, self._license_action, True))

       # -------------      Ribbon Button Functions      -----------------

    def closeEvent(self, close_event):
        pass

    def on_Registrasi_file(self):
        Registrasi_on(self)

    def on_save_to_excel(self):
        pass

    def on_Pendaftaran(self):
        Pendaftaran_on(self)


    def on_zoom(self):
        pass

    def on_k1(self):
        pass

    def on_license(self):
        pass

     
    def app_exit(self):
        sys.exit()

    def on_about(self): 
        text = "About App Pendaftaran dan Registrasi Mahasiswa Baru\n"
        text += "Yuhanes Firdiansyah\n"
        text +="Muhammad Iqbal Trimulyono\n"
        text +="Sahrul Mubarok\n"
        text +="Muhammad Filauhin Mahfudin\n"
        text += "Copyright © 2022"
        QMessageBox().about(self, "About app", text)