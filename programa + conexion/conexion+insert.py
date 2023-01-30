#conexion

import mysql.connector

con= mysql.connector.connect(host="localhost", user="root", passwd="", database="fruta")

cursor1= con.cursor()

sql="insert into fruta(nombre, descripcion, precio, cantidad)values (%s, %s,%s, %s)"

datos= ("naranja","fruta1","34.34","56")
cursor1.execute(sql, datos)

datos= ("fresa","fruta2","34","25")
cursor1.execute(sql, datos)

datos= ("platano","fruta3","12.12","10")
cursor1.execute(sql, datos)

con.commit()
con.close()
