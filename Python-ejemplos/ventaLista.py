import tkinter as tk

class Listas :

    def __init__(self):

        self.vent1=tk.Tk()

        self.lista1=tk.Listbox(self.vent1)
        self.lista1.grid(column=0, row=0)

        self.lista1.insert(0,"fresa")
        self.lista1.insert(1,"naranja")
        self.lista1.insert(2,"melon")
        self.lista1.insert(3,"pera")
        self.lista1.insert(4,"manzana")
        self.lista1.insert(5,"platano")

        self.boton1=tk.Button(self.vent1, text="recuperar", command= self.recuperar)
        self.boton1.grid(column=0, row=1)

        self.label1=tk.Label(self.vent1, text="seleccionado: ")
        self.label1.grid(column=0, row=2)

        self.vent1.mainloop()

    def recuperar(self):

        if len(self.lista1.curselection())!= 0:
            self.label1.configure(text= self.lista1.get(self.lista1.curselection()[0]))


listas= Listas()
