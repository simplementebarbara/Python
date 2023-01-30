#recoge titulo 
import tkinter as tk

class entrada:
    def __init__(self):

        self.vent1= tk.Tk()

        self.label1=tk.Label(self.vent1, text="ingrese nombre: ")
        self.label1.grid(column=0, row=0)

        self.dato=tk.StringVar()
        self.entry1=tk.Entry(self.vent1, width=20, textvariable=self.dato)
        self.entry1.grid(column=1, row=0)

        self.boton1=tk.Button(self.vent1, text="Ingresar", command=self.poner)
        self.boton1.grid(column=1,row=1)

        self.vent1.mainloop()

    def poner(self):

        self.vent1.title(self.dato.get())

programa= entrada()

        
