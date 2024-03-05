from db import DBConnection as mydb
class Testkomik:
    def __init__(self):
        self.__id=None
        self.__idpelanggan=None
        self.__namapelanggan=None
        self.__judulkomik=None
        self.__waktupeminjaman=None
        self.__waktupengembalian=None
        self.__tarif=None
        self.conn = None
        self.affected = None
        self.result = None
    @property
    def id(self):
        return self.__id
    @property
    def idpelanggan(self):
        return self.__idpelanggan
        
    @idpelanggan.setter
    def idpelanggan(self, value):
        self.__idpelanggan = value
    @property
    def namapelanggan(self):
        return self.__namapelanggan
        
    @namapelanggan.setter
    def namapelanggan(self, value):
        self.__namapelanggan = value
    @property
    def judulkomik(self):
        return self.__judulkomik
        
    @judulkomik.setter
    def judulkomik(self, value):
        self.__judulkomik = value
    @property
    def waktupeminjaman(self):
        return self.__waktupeminjaman
        
    @waktupeminjaman.setter
    def waktupeminjaman(self, value):
        self.__waktupeminjaman = value
    @property
    def waktupengembalian(self):
        return self.__waktupengembalian
        
    @waktupengembalian.setter
    def waktupengembalian(self, value):
        self.__waktupengembalian = value
    @property
    def tarif(self):
        return self.__tarif
        
    @tarif.setter
    def tarif(self, value):
        self.__tarif = value
    def simpan(self):
        self.conn = mydb()
        val = (self.__idpelanggan,self.__namapelanggan,self.__judulkomik,self.__waktupeminjaman,self.__waktupengembalian,self.__tarif)
        sql="INSERT INTO Testkomik (idpelanggan,namapelanggan,judulkomik,waktupeminjaman,waktupengembalian,tarif) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected
    def update(self, id):
        self.conn = mydb()
        val = (self.__idpelanggan,self.__namapelanggan,self.__judulkomik,self.__waktupeminjaman,self.__waktupengembalian,self.__tarif, id)
        sql="UPDATE testkomik SET idpelanggan = %s,namapelanggan = %s,judulkomik = %s,waktupeminjaman = %s,waktupengembalian = %s,tarif = %s WHERE id=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected
    def updateBy(self, ):
        self.conn = mydb()
        val = (self.__idpelanggan,self.__namapelanggan,self.__judulkomik,self.__waktupeminjaman,self.__waktupengembalian,self.__tarif, )
        sql="UPDATE testkomik SET idpelanggan = %s,namapelanggan = %s,judulkomik = %s,waktupeminjaman = %s,waktupengembalian = %starif = %s WHERE =%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected        
    def delete(self, id):
        self.conn = mydb()
        sql="DELETE FROM testkomik WHERE id='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
    def deleteBy(self, ):
        self.conn = mydb()
        sql="DELETE FROM testkomik WHERE ='" + str() + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
    def getByID(self, id):
        self.conn = mydb()
        sql="SELECT * FROM testkomik WHERE id='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        self.__id = self.result[0]
        self.__idpelanggan = self.result[1]
        self.__namapelanggan = self.result[2]
        self.__judulkomik = self.result[3]
        self.__waktupeminjaman = self.result[4]
        self.__waktupengembalian = self.result[5]
        self.__tarif = self.result[6]
        self.conn.disconnect
        return self.result
    def getBy(self, ):
        a=str()
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM testkomik WHERE ='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
           self.__id = self.result[0]
           self.__idpelanggan = self.result[1]
           self.__namapelanggan = self.result[2]
           self.__judulkomik = self.result[3]
           self.__waktupeminjaman = self.result[4]
           self.__waktupengembalian = self.result[5]
           self.__tarif = self.result[6]
           self.affected = self.conn.cursor.rowcount
        else:
           self.__id = ''
           self.__idpelanggan = ''
           self.__namapelanggan = ''
           self.__judulkomik = ''
           self.__waktupeminjaman = ''
           self.__waktupengembalian = ''
           self.__tarif = ''
        
           self.affected = 0
        self.conn.disconnect
        return self.result
    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM testkomik"
        self.result = self.conn.findAll(sql)
        return self.result
        
    def getComboData(self):
        self.conn = mydb()
        sql="SELECT id,namapelanggan FROM testkomik"
        self.result = self.conn.findAll(sql)
        return self.result        