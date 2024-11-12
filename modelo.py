import mysql.connector
from mysql.connector import Error

class Modelo():
    def conectar(self):
        conexion = mysql.connector.connect(host="localhost",user="root",passwd="",db="productos_mvc",port=3306)
        return conexion

    def SelectAll(self):
        con = self.conectar()
        cursor = con.cursor()
        sql = "SELECT * FROM productos WHERE 1"
        cursor.execute(sql)
        info = cursor.fetchall()
        cursor.close()
        return info

    def Insert(self, cod_pro, nom_pro, mod_pro, pre_pro, can_pro):
        try:
            con = self.conectar()
            cursor = con.cursor()
            sql = f"INSERT INTO productos (cod_pro, nom_pro, mod_pro, pre_pro, can_pro) VALUES('{cod_pro}', '{nom_pro}', '{mod_pro}', '{pre_pro}', '{can_pro}')"
            cursor.execute(sql)
            result = cursor.rowcount 
            cursor.execute("commit")
            con.close()
            return result
        except Error as e:
            return e

    def Select(self, cod_pro):
        con = self.conectar()
        cursor = con.cursor()
        sql = f"SELECT * FROM productos WHERE cod_pro = '{cod_pro}'"
        cursor.execute(sql)
        info = cursor.fetchone()
        return info

    def Update(self, cod_pro, nom_pro, mod_pro, pre_pro, can_pro):
        try:
            con = self.conectar()
            cursor = con.cursor()
            sql = f"UPDATE productos SET nom_pro = '{nom_pro}', mod_pro = '{mod_pro}', pre_pro = '{pre_pro}', can_pro = '{can_pro}' WHERE cod_pro = '{cod_pro}'"
            cursor.execute(sql)
            result = cursor.rowcount
            cursor.execute("commit")
            con.close()
            return result
        except Error as e:
            return e

    def Delete(self, cod_pro):
        con = self.conectar()
        cursor = con.cursor()
        sql = f"DELETE FROM productos WHERE cod_pro= '{cod_pro}'"
        cursor.execute(sql)
        result = cursor.rowcount
        cursor.execute("commit")
        con.close()
        return result