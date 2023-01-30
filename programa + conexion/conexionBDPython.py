#cargar el paquete de mysql connector
import mysql.connector
#hace la conexion
con1=mysql.connector.connect(host="localhost", user="root", passwd="")
#crea un objeto para manejar la conexion
cursor1= con1.cursor()
#execcute--> ejecuta una query
cursor1.execute("show databases")

for fila in cursor1:
    print(fila)

con1.close()
