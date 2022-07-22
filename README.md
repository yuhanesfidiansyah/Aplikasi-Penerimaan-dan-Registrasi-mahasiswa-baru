# Kelompok 6 - Aplikasi penerimaan dan Registrasi Mahasiswa Baru
Aplikasi dibuat untuk memenuhi tugas Ujian Akhir Semester Pemrograman Berbasis Objek 2.
# Persiapan 
* Download dan Install [Visual Studio Code atau code](https://code.visualstudio.com/) atau bisa juga menggunakan editor lainnya seperti [atom](https://atom.io/) dan [sublimetext](https://www.sublimetext.com/) 
* Download dan Install Python
* Download dan Install PosgreSQL
* Download dan Install QtDesigner
Setelah selesai semua dilanjutkan dengan menginstall package pyqt5 dan psycopg2 dengan pip 

   ``` 
   pip install pyqt5 
   ```
   dan 
   ```
   pip install psycopg2
   ```
# Struktur Konfigurasi Database
 * Create database KelasK1
 firdiansyah=> create table users
 firdiansyah(> id serial primary key,
 firdiansyah(> username varchar(100) not null,
 firdiansyah(> password varchar(100) not null,
 firdiansyah(> rolename varchar(100) not null);
 
 CREATE TABLE
 firdiansyah=> create table PMB(
 firdiansyah(> id serial primary key,
 firdiansyah(> nisn varchar(100) unique not null,
 firdiansyah(> nama varchar(100) not null,
 firdiansyah(> lahir varchar(100) not null,
 firdiansyah(> jk char(1) not null,
 firdiansyah(> sekolah varchar(100) not null,
 firdiansyah(> telepon varchar(100) not null,
 firdiansyah(> email varchar(100) not null,
 firdiansyah(> alamat varchar(100) not null,
 firdiansyah(> kode_prodi varchar(100) not null);
 CREATE TABLE

 firdiansyah=> create table registrasi(
 firdiansyah(> id serial primary key,
 firdiansyah(> pendaftaran varchar(100) not null,
 firdiansyah(> input varchar(100) not null,
 firdiansyah(> nama varchar(100) not null,
 firdiansyah(> jk char(1) not null,
 firdiansyah(> biaya varchar(100) not null,
 firdiansyah(> kode_prodi varchar(100) not null);
 CREATE TABLE
 
 
# Penggunaan aplikasi PMB
  * Setelah dwonload file aplikasi buat database sesuai struktur database diatas, anda bisa jalankan file main.py
  
# Kelompok 6
  * Yuhanes Firdiansyah(200511145)              
  * Muhammad Filauhin Mahfudin(200511144)       
  * Sahrul Mubarok (200511133)
  * Muhammad Iqbal Trimulyono(200511153)




