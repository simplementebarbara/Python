#select

import mysql.connector

con= mysql.connector.connect(host="localhost", user="root", passwd="", database="fruta")

cursor1= con.cursor()


sql= "select nombre, descripcion, precio, from fruta"
"""
#select
sql= "select nombre, descripcion, precio, from fruta where nombre%s"
datos= ("fresa")
"""
cursor1.execute(sql)

#para ver el resultado en pantalla

for fila in cursor1:
    print (fila)
#actualizacion
    """
sql= "update fruta set precio=%s where nombre=%s"
datos=("200","fresa")
"""
con.commit()
con.close()
