import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

SQL_Tabla_de_Productos="CREATE TABLE IF NOT EXISTS PRODUCTOS (ID serial PRIMARY KEY, PRODUCTO_NOMBRE VARCHAR(100) NOT NULL, PRECIO INTEGER NOT NULL, DESCRIPCION VARCHAR(500), PRODUCTO_USUARIO_ID INTEGER NOT NULL)"

DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')

class Coneaxion_a_DB_Productos:
    def __init__(self):
        self.conn = psycopg2.connect(DB_NAME,
                                     DB_USER,   
                                     DB_PASSWORD,
                                     DB_HOST,
                                     DB_PORT)
        self.cursor = self.conn.cursor()
        self.cursor.execute(SQL_Tabla_de_Productos)
        self.conn.commit()

    def cerrar(self):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

#____________________________________________________________ Sección de productos ____________________________________________________________

def Printear_Todos_los_Datos_del_DB():
    DB = Coneaxion_a_DB_Productos()
    DB.cursor.execute("SELECT * FROM PRODUCTOS")
    return DB.cursor.fetchall()

def Printear_un_Producto(ID):
    DB = Coneaxion_a_DB_Productos()
    DB.cursor.execute("SELECT * FROM productos WHERE ID = %s", (ID,))
    return DB.cursor.fetchone()

#Agreagar un nuevo producto

def Agreagar_Producto(Nombre_Producto,Precio_Producto,Descripcion_Producto, Id_Usuario):
    DB = Coneaxion_a_DB_Productos()
    DB.cursor.execute("INSERT INTO PRODUCTOS (PRODUCTO_NOMBRE, PRECIO, DESCRIPCION, PRODUCTO_USUARIO_ID) VALUES (%s,%s,%s,%s)",(Nombre_Producto, Precio_Producto, Descripcion_Producto, Id_Usuario))
    DB.cerrar()

#Borrar el producto seleccionado

def Borrar_Producto(ID, Id_Usuario):
    DB = Coneaxion_a_DB_Productos()
    DB.cursor.execute("DELETE FROM PRODUCTOS WHERE ID = %s AND PRODUCTO_USUARIO_ID = %s",(ID, Id_Usuario))
    DB.cerrar()

#Editar un producto seleccionado

def Editar_Producto(ID, Nombre_Editado, Precio_Editado, Descripcion_Editada, Id_Usuario):
    DB = Coneaxion_a_DB_Productos()
    DB.cursor.execute("UPDATE PRODUCTOS SET PRODUCTO_NOMBRE = %s, PRECIO = %s, DESCRIPCION = %s WHERE ID = %s AND PRODUCTO_USUARIO_ID = %s",(Nombre_Editado, Precio_Editado, Descripcion_Editada, ID, Id_Usuario))
    DB.cerrar()

#Buscar los productos

def Buscar_Producto(Buscar_Producto_s):
    DB = Coneaxion_a_DB_Productos()
    query = "SELECT * FROM Productos WHERE PRODUCTO_NOMBRE ILIKE %s"
    DB.cursor.execute(query, ('%' + Buscar_Producto_s + '%',))
    return DB.cursor.fetchall()

#Busca los productos del usuario creador

def Printear_Mis_Productos(Id_Usuario):
    DB = Coneaxion_a_DB_Productos()
    DB.cursor.execute("SELECT * FROM productos WHERE PRODUCTO_USUARIO_ID = %s", (Id_Usuario,))
    return DB.cursor.fetchall()
