from PyQt5.QtGui import *

__author__ = 'yuhanes firdiansyah'

icons_instance = None


def get_icon(name):
    global icons_instance
    if not icons_instance:
     icons_instance = Icons()
    return icons_instance.icon(name)


class Icons(object):
    def __init__(self):
        self._icons = {}
        self.make_icon("folder", "icons/folder.png")
        self.make_icon("icon", "icons/icon.png")
        self.make_icon("umc", "icons/umc.png")
        self.make_icon("exit", "icons/exit.png")
        self.make_icon("about", "icons/about.png")
        self.make_icon("umc", "icons/umc.png")
        self.make_icon("k1", "icons/k1.png")
        self.make_icon("default", "icons/folder.png")
        self.make_icon("pendaftaran", "icons/pendaftaran.png")
        self.make_icon("Registrasi", "icons/registrasi.png")
        
    def make_icon(self, name, path):
        icon = QIcon()
        icon.addPixmap(QPixmap(path), QIcon.Normal, QIcon.Off)
        self._icons[name] = icon

    def icon(self, name):
        icon = self._icons["default"]
        try:
            icon = self._icons[name]
        except KeyError:
            print("icon " + name + " not found")
        return icon
