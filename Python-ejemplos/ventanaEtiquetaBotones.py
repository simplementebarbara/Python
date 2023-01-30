#ventanaTexField-enter
import tkinter as tk

class Programa:

    def __init__(self):

        self.vent1=tk.Tk()

        self.label1=tk.Label(self.vent1, text ="Mete un numero: ")
        #se coloca en la rejilla
        self.label1.grid(column=0, row=0)
        #esta variable va a recoger lo que entre por teclado
        self.dato=tk.StringVar()
        #la caja que recoge los datos
        self.entry1=tk.Entry(self.vent1, width=10, textvariable= self.dato)
        self.entry1.grid(column=0,row=1)

        self.boton1=tk.Button(self.vent1, text="Doble", command=self.doble)
        self.boton1.grid(column=0, row=2)

        #segunda etiqueta
        self.label2=tk.Label(self.vent1, text ="Resultado: ")
        #se coloca en la rejilla
        self.label2.grid(column=0, row=3)

        self.vent1.mainloop()

    def doble(self):

        valor= int(self.dato.get())
        doble = 2*valor
        self.label2.configure(text=doble)
#constructor __init__
ventana=Programa()
                   
