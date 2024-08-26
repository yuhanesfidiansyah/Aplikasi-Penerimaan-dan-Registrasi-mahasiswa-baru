import os, sys; sys.path.insert(0, os.path.dirname(os.path.realpath(__name__)))
from config.db import DBConnection as mydb

class Registrasi:

    def __init__(self):
        self.__id=None
        self.__pendaftaran=None
        self.__input=None
        self.__nama=None
        self.__jk=None
        self.__biaya=None
        self.__kode_prodi=None
        self.__info = None
        self.conn = None
        self.affected = None
        self.result = None
        
    @property
    def info(self):
        if(self.__info==None):
            return "pendaftaran:" + self.__pendaftaran + "\n" +  "input:" + self.__input + "\n" + "Nama:" + self.__nama + "\n" + "Jk:" + self.__jk + "\n" + "biaya:" + self.__biaya + "\n" + "Kode Prodi:" + self.__kode_prodi
        else:
            return self.__info
    
    @info.setter
    def info(self, value):
        self.__info = value

    @property
    def id(self):
        return self.__id

    @property
    def pendaftaran(self):
        return self.__pendaftaran

    @pendaftaran.setter
    def pendaftaran(self, value):
        self.__pendaftaran = value

    @property
    def input(self):
        return self.__input

    @input.setter
    def input(self, value):
        self.__input = value


    @property
    def nama(self):
        return self.__nama

    @nama.setter
    def nama(self, value):
        self.__nama = value

    @property
    def jk(self):
        return self.__jk

    @jk.setter
    def jk(self, value):
        self.__jk = value

    @property
    def biaya(self):
        return self.__biaya

    @biaya.setter
    def biaya(self, value):
        self.__biaya = value

    @property
    def kode_prodi(self):
        return self.__kode_prodi

    @kode_prodi.setter
    def kode_prodi(self, value):
        self.__kode_prodi = value

    def simpan(self):
        self.conn = mydb()
        val = (self.__pendaftaran, self.__input, self.__nama, self.__jk, self.__biaya, self.__kode_prodi)
        sql="INSERT INTO registrasi (pendaftaran, input, nama, jk, biaya, kode_prodi) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected

    def update(self, id):
        self.conn = mydb()
        val = (self.__pendaftaran, self.__input, self.__nama, self.__jk, self.__biaya, self.__kode_prodi, id)
        sql="UPDATE registrasi SET pendaftaran =%s, input =%s, nama =%s, jk=%s, biaya=%s, kode_prodi=%s WHERE idmhs=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected

    def updateBypendaftaran(self, pendaftaran):
        self.conn = mydb()
        val = (self.__input, self.__nama, self.__jk, self.__biaya, self.__kode_prodi, pendaftaran)
        sql="UPDATE registrasi SET input =%s, nama =%s, jk=%s, biaya=%s, kode_prodi=%s WHERE pendaftaran=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected        

    def delete(self, id):
        self.conn = mydb()
        sql="DELETE FROM registrasi WHERE idmhs='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def deleteBypendaftaran(self, pendaftaran):
        self.conn = mydb()
        sql="DELETE FROM registrasi WHERE pendaftaran='" + str(pendaftaran) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def getByID(self, id):
        self.conn = mydb()
        sql="SELECT * FROM registrasi WHERE idmhs='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        self.__pendaftaran = self.result[1]
        self.__input = self.result[2]
        self.__nama = self.result[3]
        self.__jk = self.result[4]
        self.__biaya = self.result(5)
        self.__kode_prodi = self.result[6]
        self.conn.disconnect
        return self.result

    def getBypendaftaran(self, pendaftaran):
        self.conn = mydb()
        sql="SELECT * FROM registrasi WHERE pendaftaran='" + str(pendaftaran) + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__pendaftaran = self.result[1]
            self.__input = self.result[2]
            self.__nama = self.result[3]
            self.__jk = self.result[4]
            self.__biaya = self.result[5]
            self.__kode_prodi = self.result[6]
            self.affected = self.conn.cursor.rowcount
        else:
            self.__pendaftaran = ''
            self.__input = ''
            self.__nama = ''
            self.__jk = ''
            self.__biaya = ''
            self.__kode_prodi = ''
            self.affected = 0
        self.conn.disconnect
        return self.result

    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM registrasi"
        self.result = self.conn.findAll(sql)
        return self.result
