import email
import os, sys; sys.path.insert(0, os.path.dirname(os.path.realpath(__name__)))
import psycopg2 as mc
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QMessageBox
from classes.Pendaftaran import Pendaftaran

qtcreator_file  = "./ui/pendaftaran.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)


class PendaftaranWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Event Setup
        self.btnCari.clicked.connect(self.search_data) # Jika tombol cari diklik
        self.btnSimpan.clicked.connect(self.save_data) # Jika tombol simpan diklik
        self.txtNISN.returnPressed.connect(self.search_data) # Jika menekan tombol Enter saat berada di textbox pendaftaran
        self.btnClear.clicked.connect(self.clear_entry)
        self.btnHapus.clicked.connect(self.delete_data)
        self.edit_mode=""   
        self.btnHapus.setEnabled(False) # Matikan tombol hapus
        self.btnHapus.setStyleSheet("color:black;background-color : Red")

    def select_data(self):
        try:
            mhs = Pendaftaran()

            # Get all 
            result = mhs.getAllData()

            self.gridPendaftaran.setHorizontalHeaderLabels(['ID' , 'NISN', 'Nama Lengkap', 'Tanggal Lahir', 'Jenis kelamin', 'Nama Ibu/Ayah' , 'Asal Sekolah', 'Telepon','Email', 'Alamat', 'Program Studi'])
            self.gridPendaftaran.setRowCount(0)
            

            for row_number, row_data in enumerate(result):
                #print(row_number)
                self.gridPendaftaran.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    #print(column_number)
                    self.gridPendaftaran.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        
        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def search_data(self):
        try:           
            nisn=self.txtNISN.text()        
            mhs = Pendaftaran()

            # search process
            result = mhs.getBynisn(nisn)
            a = mhs.affected
            if(a>0):
                self.TampilData(result)
            else:
                self.messagebox("INFO", "Data tidak ditemukan")
                self.txtLahir.setFocus()
                self.btnSimpan.setText("Simpan")
                self.edit_mode=False
                self.btnHapus.setEnabled(False) # Matikan tombol hapus
                self.btnHapus.setStyleSheet("color:black;background-color : grey")
            
        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def save_data(self, MainWindow):
        try:
            mhs = Pendaftaran()
            nisn=self.txtNISN.text()
            nama=self.txtNama.text()
            lahir=self.txtLahir.text()
            orgtua=self.txtOrgtua.text()
            sekolah=self.txtSekolah.text()
            telepon=self.txtTelepon.text()
            email=self.txtEmail.text()
            alamat=self.txtAlamat.text()
            if self.optLaki.isChecked():
                jk="L"
            
            if self.optPerempuan.isChecked():
                jk="P"


            kode_prodi=self.cboProdi.currentText()
            
            if(self.edit_mode==False):   
                mhs.nisn = nisn
                mhs.nama = nama
                mhs.lahir = lahir
                mhs.jk = jk
                mhs.orgtua = orgtua
                mhs.sekolah = sekolah
                mhs.telepon = telepon
                mhs.email = email
                mhs.alamat = alamat
                mhs.kode_prodi = kode_prodi
                a = mhs.simpan()
                if(a>0):
                    self.messagebox("SUKSES", "Data Pendaftaran Tersimpan")
                else:
                    self.messagebox("GAGAL", "Data Pendaftaran Gagal Tersimpan")
                
                self.clear_entry(self) # Clear Entry Form
                self.select_data() # Reload Datagrid
            elif(self.edit_mode==True):
                mhs.nama = nama
                mhs.lahir = lahir
                mhs.jk = jk
                mhs.orgtua = orgtua
                mhs.sekolah = sekolah
                mhs.telepon = telepon
                mhs.email = email
                mhs.alamat = alamat
                mhs.kode_prodi = kode_prodi
                a = mhs.updateBynisn(nisn)
                if(a>0):
                    self.messagebox("SUKSES", "Data PendaftaranDiperbarui")
                else:
                    self.messagebox("GAGAL", "Data PendaftaranGagal Diperbarui")
                
                self.clear_entry(self) # Clear Entry Form
                self.select_data() # Reload Datagrid
            else:
                self.messagebox("ERROR", "Terjadi kesalahan Mode Edit")
            

        except mc.Error as e:
            self.messagebox("ERROR", str(e))

    def delete_data(self, MainWindow):
        try:
            mhs = Pendaftaran()
            nisn=self.txtNISN.text()
            
                      
            if(self.edit_mode==True):
                a = mhs.deleteBynisn(nisn)
                if(a>0):
                    self.messagebox("SUKSES", "Data Pendaftaran Dihapus")
                else:
                    self.messagebox("GAGAL", "Data Pendaftaran Gagal Dihapus")
                
                self.clear_entry(self) # Clear Entry Form
                self.select_data() # Reload Datagrid
            else:
                self.messagebox("ERROR", "Sebelum meghapus data harus ditemukan dulu")
            

        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def TampilData(self,result):
        self.txtNISN.setText(result[1])
        self.txtNama.setText(result[2])
        self.txtLahir.setText(result[3])
        if(result[4]=="L"):
            self.optLaki.setChecked(True)
            self.optPerempuan.setChecked(False)
        else:
            self.optLaki.setChecked(False)
            self.optPerempuan.setChecked(True)

        self.txtOrgtua.setText(result[5])
        self.txtSekolah.setText(result[6])
        self.txtTelepon.setText(result[7])
        self.txtEmail.setText(result[8])
        self.txtAlamat.setText(result[9])
        

        self.cboProdi.setCurrentText(result[10])
        self.btnSimpan.setText("Update")
        self.edit_mode=True
        self.btnHapus.setEnabled(True) # Aktifkan tombol hapus
        self.btnHapus.setStyleSheet("background-color : red")

    def clear_entry(self, MainWindow):
        self.txtNISN.setText("")
        self.txtNama.setText("")
        self.txtLahir.setText("")
        self.optLaki.setChecked(False)
        self.optPerempuan.setChecked(False)
        self.txtOrgtua.setText("")
        self.txtSekolah.setText("")
        self.txtTelepon.setText("")
        self.txtEmail.setText("")
        self.txtAlamat.setText("")
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
    window = PendaftaranWindow()
    window.show()
    window.select_data()
    sys.exit(app.exec_())
else:
    app = QtWidgets.QApplication(sys.argv)
    window = PendaftaranWindow()
    #window.show()
    #window.select_data()
