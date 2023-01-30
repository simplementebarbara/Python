#para construir una ventana con una etiqueta y dos botones
import tkinter as tk

class ventana_principal:

    def __init__(self):
        self.valor=1
        #creear ventana
        self.vent1=tk.Tk()
        self.vent1.title("Boton y label")
        #se crea etiqueta (self.vent1 --> hace referencia al padre)
        self.label1= tk.Label(self.vent1, text=self.valor)
        self.label1.grid(column=0, row=0)
        self.label1.configure(foreground="green")
        #se crea boton y se va a colocar el boton1 en la rejilla
        self.boton1=tk.Button(self.vent1, text="sumar 1", command=self.sumar)
        self.boton1.grid(column=1,row=0)
         #se crea boton2 y se va a colocar el boton2 en la rejilla
        self.boton2=tk.Button(self.vent1, text="restar 1", command=self.restar)
        self.boton2.grid(column=2,row=0)
        #se construye la ventana
        self.vent1.mainloop()

    def sumar(self):

        self.valor= self.valor+1
        self.label1.config(text=self.valor)

    def restar(self):

        self.valor= self.valor-1
        self.label1.config(text=self.valor)

vent_principal= ventana_principal()
