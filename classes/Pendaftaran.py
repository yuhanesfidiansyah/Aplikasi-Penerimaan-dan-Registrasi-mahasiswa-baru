import os, sys
from unittest import result; sys.path.insert(0, os.path.dirname(os.path.realpath(__name__)))
from config.db import DBConnection as mydb

class Pendaftaran:

    def __init__(self):
        self.__id=None
        self.__nisn=None
        self.__nama=None
        self.__lahir=None
        self.__jk=None
        self.__orgtua=None
        self.__sekolah=None
        self.__telepon=None
        self.__email=None
        self.__alamat=None
        self.__kode_prodi=None
        self.__info = None
        self.conn = None
        self.affected = None
        self.result = None
        
    @property
    def info(self):
        if(self.__info==None):
            return "nisn:" + self.__nisn + "\n" +  "nama:" + self.__nama + "\n" + "lahir:" + self.__lahir + "\n" + "Jk:" + self.__jk + "\n" + "orgtua:" + self.__orgtua + "\n" + "Asal Sekolah:" + self.__sekolah + "\n" + "Telepon:" + self.__telepon + "\n" + "email:" + self.__email + "\n" + "Alamat:" + self.__alamat + "\n" + "Kode Prodi:" + self.__kode_prodi
        else:
            return self.__info
    
    @info.setter
    def info(self, value):
        self.__info = value

    @property
    def id(self):
        return self.__id

    @property
    def nisn(self):
        return self.__nisn

    @nisn.setter
    def nisn(self, value):
        self.__nisn = value

    @property
    def nama(self):
        return self.__nama

    @nama.setter
    def nama(self, value):
        self.__nama = value


    @property
    def lahir(self):
        return self.__lahir

    @lahir.setter
    def lahir(self, value):
        self.__lahir = value

    @property
    def jk(self):
        return self.__jk

    @jk.setter
    def jk(self, value):
        self.__jk = value

    @property
    def orgtua(self):
        return self.__orgtua

    @orgtua.setter
    def orgtua(self, value):
        self.__orgtua = value
        
    @property
    def sekolah(self):
        return self.__sekolah

    @sekolah.setter
    def sekolah(self, value):
        self.__sekolah = value

    @property
    def telepon(self):
        return self.__telepon

    @telepon.setter
    def telepon(self, value):
        self.__telepon = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    @property
    def alamat(self):
        return self.__alamat

    @alamat.setter
    def alamat(self, value):
        self.__alamat = value

    @property
    def kode_prodi(self):
        return self.__kode_prodi

    @kode_prodi.setter
    def kode_prodi(self, value):
        self.__kode_prodi = value

    def simpan(self):
        self.conn = mydb()
        val = (self.__nisn, self.__nama, self.__lahir, self.__jk, self.__orgtua, self.__sekolah, self.__telepon, self.__email, self.__alamat, self.__kode_prodi)
        sql="INSERT INTO PMB (nisn, nama, lahir, jk, orgtua, sekolah, telepon, email, alamat, kode_prodi) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected

    def update(self, id):
        self.conn = mydb()
        val = (self.__nisn, self.__nama, self.__lahir, self.__jk, self.__orgtua, self.__sekolah, self.__telepon, self.__email, self.__alamat, self.__kode_prodi, id)
        sql="UPDATE PMB SET nisn =%s, nama =%s, lahir =%s, jk=%s, orgtua=%s,sekolah=%s, telepon=%s, email=%s, alamat=%s, kode_prodi=%s WHERE idmhs=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected

    def updateBynisn(self, nisn):
        self.conn = mydb()
        val = (self.__nama, self.__lahir, self.__jk, self.__orgtua, self.__sekolah, self.__telepon, self.__email, self.__alamat, self.__kode_prodi, nisn)
        sql="UPDATE PMB SET nama =%s, lahir =%s, jk=%s, orgtua=%s,sekolah=%s, telepon=%s, email=%s, alamat=%s, kode_prodi=%s WHERE nisn=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected        

    def delete(self, id):
        self.conn = mydb()
        sql="DELETE FROM PMB WHERE idmhs='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def deleteBynisn(self, nisn):
        self.conn = mydb()
        sql="DELETE FROM PMB WHERE nisn='" + str(nisn) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def getByID(self, id):
        self.conn = mydb()
        sql="SELECT * FROM PMB WHERE idmhs='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        self.__nisn = self.result[1]
        self.__nama = self.result[2]
        self.__lahir = self.result[3]
        self.__jk = self.result[4]
        self.__orgtua = self.result(5)
        self.__kode_prodi = self.result[6]
        self.conn.disconnect
        return self.result

    def getBynisn(self, nisn):
        self.conn = mydb()
        sql="SELECT * FROM PMB WHERE nisn='" + str(nisn) + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__nisn = self.result[1]
            self.__nama = self.result[2]
            self.__lahir = self.result[3]
            self.__jk = self.result[4]
            self.__orgtua = self.result[5]
            self.__sekolah = self.result[6]
            self.__telepon = self.result[7]
            self.__email = self.result[8]
            self.__alamat = self.result[9]
            self.__kode_prodi = self.result[10]
            self.affected = self.conn.cursor.rowcount
        else:
            self.__nisn = ''
            self.__nama = ''
            self.__lahir = ''
            self.__jk = ''
            self.__orgtua = ''
            self.__sekolah = ''
            self.__telepon = ''
            self.__email = ''
            self.__alamat = ''
            self.__kode_prodi = ''
            self.affected = 0
        self.conn.disconnect
        return self.result

    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM PMB"
        self.result = self.conn.findAll(sql)
        return self.result
