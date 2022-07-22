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
  PMB
Column	Type	Comment	PK	        Nullable	Default
id    	integer		   YES	         NO	
nisn	   character varying(100)			NO	
nama	   character varying(100)			NO	
lahir	   character varying(100)			NO	
jk	      character(1)			         NO	
orgtua	character varying(100)			NO	
sekolah	character varying(100)			NO	
telepon	character varying(100)			NO	
email	character varying(100)		   	NO	
alamat	character varying(100)			NO	
kode_prodi	character varying(100)		NO	




registrasi
Column	      Type	                 Comment	  PK	   Nullable	Default
id	           integer	            	            YES	   NO	
pendaftaran	  character varying(100)			      NO	
input	        character varying(100)		      	NO	
nama	        character varying(100)			      NO	
jk         	  character(1)			                  NO	
biaya	        character varying(100)	      		NO	
kode_prodi	  character varying(100)	      		NO	




users
Column	Type	                  Comment	PK	Nullable	Default
iduser	integer		                     YES	NO	
username	character varying(100)		   	NO	
password	character varying(100)			   NO	
rolename	character varying(100)		   	NO	

# Penggunaan aplikasi PMB
  * Setelah dwonload file aplikasi buat database sesuai struktur database diatas, anda bisa jalankan file main.py
  
# Kelompok 6
  * Yuhanes Firdiansyah(200511145)              * Sahrul Mubarok (200511133)
  * Muhammad Filauhin Mahfudin(200511144)       * Muhammad Iqbal Trimulyono(2005111
  





