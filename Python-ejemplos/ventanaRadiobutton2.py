import tkinter as tk

class programa:

    def __init__(self):

        self.vent1=tk.Tk()

        self.seleccion1=tk.IntVar()
        self.check1=tk.Checkbutton(self.vent1, text="pera", variable= self.seleccion1)
        self.check1.grid(column=0,row=0)

        self.seleccion2=tk.IntVar()
        self.check2=tk.Checkbutton(self.vent1, text="naranja", variable= self.seleccion2)
        self.check2.grid(column=0,row=1)

        self.seleccion3=tk.IntVar()
        self.check3=tk.Checkbutton(self.vent1, text="fresa", variable= self.seleccion3)
        self.check3.grid(column=0,row=2)


        
        self.botonn1=tk.Button(self.vent1, text="Verificar", command= self.verificar)
        self.botonn1.grid(column=0,row=4)

        self.label1=tk.Label(self.vent1, text="Cantidad: ")
        self.label1.grid(column=0, row=5)

        self.vent1.mainloop()

    def verificar(self):
        cant=0

        if self.seleccion1.get()==1:
            cant= cant+1
        if self.seleccion2.get()==1:
            cant= cant+1
        if self.seleccion3.get()==1:
            cant= cant+1
        self.label1.configure(text="cantidad: "+str(cant))


prom=programa()

        
