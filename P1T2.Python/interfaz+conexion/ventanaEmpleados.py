import tkinter as tk
import mysql.connector


 
class interfaz:
    def __init__(self):

        self.vent1=tk.Tk()
    #label y textFiel nombre
        self.labelNombre=tk.Label(self.vent1, text= "Nombre: ")
        self.labelNombre.grid(column=0, row=0)
        self.nombre= tk.StringVar()
        self.entryNombre= tk.Entry(self.vent1, width=10, textvariable =self.nombre)
        self.entryNombre.grid(column=1, row= 0)

    #label y texField primer_apellido
        self.labelPrimerApell=tk.Label(self.vent1, text= "Primer apellido: ")
        self.labelPrimerApell.grid(column=0, row=1)
        self.primero= tk.StringVar()
        self.entryPrimerApell= tk.Entry(self.vent1, width=10, textvariable =self.primero)
        self.entryPrimerApell.grid(column=1, row= 1)


    #label y texField segundo_apellido
        self.labelSegundoApell=tk.Label(self.vent1, text= "Segundo apellido: ")
        self.labelSegundoApell.grid(column=0, row=2)
        self.segundo= tk.StringVar()
        self.entrySegundoApell= tk.Entry(self.vent1, width=10, textvariable =self.segundo)
        self.entrySegundoApell.grid(column=1, row= 2)


    #label y texField DNI
        self.labelDNI=tk.Label(self.vent1, text= "DNI: ")
        self.labelDNI.grid(column=0, row=3)
        self.DNI= tk.StringVar()
        self.entryDNI = tk.Entry(self.vent1, width=10, textvariable =self.DNI)
        self.entryDNI.grid(column=1, row= 3)
        
    #label y texField fecha_nacimiento
        self.labelFechaNacimiento=tk.Label(self.vent1, text= "Fecha nacimiento: ")
        self.labelFechaNacimiento.grid(column=0, row=4)
        self.fecha= tk.StringVar()
        self.entryFechaNacimiento= tk.Entry(self.vent1, width=10, textvariable =self.fecha)
        self.entryFechaNacimiento.grid(column=1, row= 4)

    #label y texField puesto
        self.labelpuesto=tk.Label(self.vent1, text= "Puesto: ")
        self.labelpuesto.grid(column=0, row=5)
        self.puesto= tk.StringVar()
        self.entryPuesto= tk.Entry(self.vent1, width=10, textvariable =self.puesto)
        self.entryPuesto.grid(column=1, row= 5)

    #label y texField sueldo
        self.labelSueldo=tk.Label(self.vent1, text= "Sueldo: ")
        self.labelSueldo.grid(column=0, row=6)
        self.sueldo= tk.StringVar()
        self.entrySueldo= tk.Entry (self.vent1, width=10, textvariable =self.sueldo)
        self.entrySueldo.grid(column=1, row= 6)

    #label y texField antiguedad
        self.labelAntiguedad=tk.Label(self.vent1, text= "Antiguedad: ")
        self.labelAntiguedad.grid(column=0, row=7)
        self.antiguedad= tk.StringVar()
        self.entryAntiguedad= tk.Entry (self.vent1, width=10, textvariable =self.antiguedad)
        self.entryAntiguedad.grid(column=1, row= 7)

    #boton insertar
        self.botonInsertar= tk.Button(self.vent1, text="Insertar", command= self.insert)
        self.botonInsertar.grid(column= 1, row=10)
    #boton update
        self.botonUpdate= tk.Button(self.vent1, text="Actualizar", command= self.updatePuesto)
        self.botonUpdate.grid(column= 1, row=11)
        
    #boton select
        self.botonSelect= tk.Button(self.vent1, text="Select", command= self.select)
        self.botonSelect.grid(column= 1, row=12)
        
    #boton DELETE
        self.botonDelete= tk.Button(self.vent1, text="Borrar", command= self.delete)
        self.botonDelete.grid(column= 1, row=13)
    #limpiar campos
        self.clear_button = tk.Button(self.vent1, text="Clear text", command=self.clear_text)
        self.clear_button.grid(column= 0, row=11)

 
        
        self.vent1.mainloop()


    def clear_text(self):
        self.entryNombre.delete(0, 'end')
        self.entryPrimerApell.delete(0, 'end')
        self.entrySegundoApell.delete(0, 'end')
        self.entryDNI.delete(0, 'end')
        self.entryFechaNacimiento.delete(0, 'end')
        self.entryPuesto.delete(0, 'end')
        self.entrySueldo.delete(0, 'end')
        self.entryAntiguedad.delete(0, 'end')
        

    def select(self):
        DNI= self.DNI.get()
         #se recoge los datos
        datos= (DNI,)
        #Conexion a BD
        con= mysql.connector.connect(host="localhost", user="root", passwd="", database="empleados")
        cursor= con.cursor()
        #sql select
        sql = " SELECT `nombre`, `primer_apellido`, `segundo_apellido`, `DNI`, `fecha_nacimiento`, `puesto`, `sueldo`, `antiguedad` FROM `empleados` WHERE DNI =%s"

        cursor.execute(sql,datos)
        filas = cursor.fetchall()
        for fila in filas:
            print (fila)
        
        con.close()
        
    
    def updatePuesto(self):
        DNI= self.DNI.get()
        puesto = self.entryPuesto.get()

         #se recoge los datos
        datos= (puesto,DNI)
        #Conexion a BD
        con= mysql.connector.connect(host="localhost", user="root", passwd="", database="empleados")
        cursor= con.cursor()
        #sql UPDATE
        sql = "update empleados set puesto =%s where DNI =%s"

        cursor.execute(sql,datos)
        con.commit()
        con.close()

    def delete(self):
        DNI= self.DNI.get()

         #se recoge los datos
        datos= (DNI,)
        #Conexion a BD
        con= mysql.connector.connect(host="localhost", user="root", passwd="", database="empleados")
        cursor= con.cursor()
        #sql delete
        sql = "delete from empleados where DNI = %s"

        cursor.execute(sql,datos)
        con.commit()
        con.close()

        
        
    def insert(self):
        nombre = self.nombre.get()
        primer_apellido= self.primero.get()
        segundo_apellido = self.segundo.get()
        DNI= self.DNI.get()
        fecha_nacimiento= self.fecha.get()
        puesto= self.puesto.get()
        sueldo= self.sueldo.get()
        antiguedad =self.antiguedad.get()

        #se recoge los datos
        datos= (nombre,primer_apellido,segundo_apellido, DNI,fecha_nacimiento, puesto,sueldo,antiguedad)

        #Conexion a BD
        con= mysql.connector.connect(host="localhost", user="root", passwd="", database="empleados")
        cursor= con.cursor()
        #Sql Insert
        sql= "insert into empleados (nombre,primer_apellido, segundo_apellido, DNI, fecha_nacimiento, puesto, sueldo, antiguedad )values (%s, %s,%s, %s,%s, %s,%s, %s)"
        cursor.execute(sql,datos)
        con.commit()
        con.close()
    
        
        
ventana = interfaz()


