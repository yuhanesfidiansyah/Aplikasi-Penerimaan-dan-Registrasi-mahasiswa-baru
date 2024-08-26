import os, sys; sys.path.insert(0, os.path.dirname(os.path.realpath(__name__)))
import psycopg2 as mc
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QMessageBox
from classes.Registrasi import Registrasi

qtcreator_file  = "./ui/registrasi.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)


class RegistrasiWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Event Setup
        self.btnCari.clicked.connect(self.search_data) # Jika tombol cari diklik
        self.btnSimpan.clicked.connect(self.save_data) # Jika tombol simpan diklik
        self.txtDAFTAR.returnPressed.connect(self.search_data) # Jika menekan tombol Enter saat berada di textbox pendaftaran
        self.btnClear.clicked.connect(self.clear_entry)
        self.btnHapus.clicked.connect(self.delete_data)
        self.edit_mode=""   
        self.btnHapus.setEnabled(False) # Matikan tombol hapus
        self.btnHapus.setStyleSheet("color:black;background-color : Red")

    def select_data(self):
        try:
            mhs = Registrasi()

            # Get all 
            result = mhs.getAllData()

            self.gridRegistrasi.setHorizontalHeaderLabels(['ID' , 'No pendaftaran', 'pendaftaran', 'Nama lengkap', 'Jenis kelamin', 'biaya registrasi' , 'Program Studi'])
            self.gridRegistrasi.setRowCount(0)
            

            for row_number, row_data in enumerate(result):
                #print(row_number)
                self.gridRegistrasi.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    #print(column_number)
                    self.gridRegistrasi.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        
        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def search_data(self):
        try:           
            pendaftaran=self.txtDAFTAR.text()        
            mhs = Registrasi()

            # search process
            result = mhs.getBypendaftaran(pendaftaran)
            a = mhs.affected
            if(a>0):
                self.TampilData(result)
            else:
                self.messagebox("INFO", "Data tidak ditemukan")
                self.txtNama.setFocus()
                self.btnSimpan.setText("Simpan")
                self.edit_mode=False
                self.btnHapus.setEnabled(False) # Matikan tombol hapus
                self.btnHapus.setStyleSheet("color:black;background-color : grey")
            
        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def save_data(self, MainWindow):
        try:
            mhs = Registrasi()
            pendaftaran=self.txtDAFTAR.text()
            input=self.txtInput.text()
            nama=self.txtNama.text()
            biaya=self.txtBiaya.text()
            if self.optLaki.isChecked():
                jk="L"
            
            if self.optPerempuan.isChecked():
                jk="P"


            kode_prodi=self.cboProdi.currentText()
            
            if(self.edit_mode==False):   
                mhs.pendaftaran = pendaftaran
                mhs.input = input
                mhs.nama = nama
                mhs.jk = jk
                mhs.biaya = biaya
                mhs.kode_prodi = kode_prodi
                a = mhs.simpan()
                if(a>0):
                    self.messagebox("SUKSES", "Data RegistrasiTersimpan")
                else:
                    self.messagebox("GAGAL", "Data RegistrasiGagal Tersimpan")
                
                self.clear_entry(self) # Clear Entry Form
                self.select_data() # Reload Datagrid
            elif(self.edit_mode==True):
                mhs.input = input
                mhs.nama = nama
                mhs.jk = jk
                mhs.biaya = biaya
                mhs.kode_prodi = kode_prodi
                a = mhs.updateBypendaftaran(pendaftaran)
                if(a>0):
                    self.messagebox("SUKSES", "Data RegistrasiDiperbarui")
                else:
                    self.messagebox("GAGAL", "Data RegistrasiGagal Diperbarui")
                
                self.clear_entry(self) # Clear Entry Form
                self.select_data() # Reload Datagrid
            else:
                self.messagebox("ERROR", "Terjadi kesalahan Mode Edit")
            

        except mc.Error as e:
            self.messagebox("ERROR", str(e))

    def delete_data(self, MainWindow):
        try:
            mhs = Registrasi()
            pendaftaran=self.txtDAFTAR.text()
            
                      
            if(self.edit_mode==True):
                a = mhs.deleteBypendaftaran(pendaftaran)
                if(a>0):
                    self.messagebox("SUKSES", "Data Registrasi Dihapus")
                else:
                    self.messagebox("GAGAL", "Data Registrasi Gagal Dihapus")
                
                self.clear_entry(self) # Clear Entry Form
                self.select_data() # Reload Datagrid
            else:
                self.messagebox("ERROR", "Sebelum meghapus data harus ditemukan dulu")
            

        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def TampilData(self,result):
        self.txtDAFTAR.setText(result[1])
        self.txtInput.setText(result[2])
        self.txtNama.setText(result[3])
        if(result[4]=="L"):
            self.optLaki.setChecked(True)
            self.optPerempuan.setChecked(False)
        else:
            self.optLaki.setChecked(False)
            self.optPerempuan.setChecked(True)

        self.txtBiaya.setText(result[5])

        self.cboProdi.setCurrentText(result[6])
        self.btnSimpan.setText("Update")
        self.edit_mode=True
        self.btnHapus.setEnabled(True) # Aktifkan tombol hapus
        self.btnHapus.setStyleSheet("background-color : red")

    def clear_entry(self, MainWindow):
        self.txtDAFTAR.setText("")
        self.txtInput.setText("")
        self.txtNama.setText("")
        self.optLaki.setChecked(False)
        self.optPerempuan.setChecked(False)
        self.txtBiaya.setText("")
        self.cboProdi.setCurrentText("")
        self.btnHapus.setEnabled(False) # Matikan tombol hapus
        self.btnHapus.setStyleSheet("color:black;background-color : red")

    def messagebox(self, title, message):
        mess = QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QMessageBox.Ok)
        mess.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = RegistrasiWindow()
    window.show()
    window.select_data()
    sys.exit(app.exec_())
else:
    app = QtWidgets.QApplication(sys.argv)
    window = RegistrasiWindow()
    #window.show()
    #window.select_data()
