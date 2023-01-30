#calculadora radio Button

import tkinter as tk

class Calculadora:

    def __init__(self):
        #abre ventana
        self.vent1=tk.Tk()
        #pone titulo a la ventana
        self.vent1.title("Calculadora")
        # primera etiqueta
        self.label1=tk.Label(self.vent1, text="primer valor: ")
        self.label1.grid(column=0, row=0)
        #cajita de primera etiqueta
        self.dato1=tk.StringVar()
        self.entry1=tk.Entry(self.vent1, width=20, textvariable=self.dato1)
        self.entry1.grid(column=1, row=0)

        #crear segunda etiqueta
        self.label2=tk.Label(self.vent1, text="Sengundo valor: ")
        self.label2.grid(column=0, row=1)

        #cajita de segunda etiqueta
        self.dato2=tk.StringVar()
        self.entry2=tk.Entry(self.vent1, width=20, textvariable=self.dato2)
        self.entry2.grid(column=1, row=1)

        #se indica que va a entrar un int
        self.seleccion=tk.IntVar()

        #declarar radio button
        self.radio1=tk.Radiobutton(self.vent1, text="Sumar", variable=self.seleccion, value=1)
        self.radio1.grid(column=1,row=2)
        #declara 2 radio button

        self.radio2=tk.Radiobutton(self.vent1, text="Restar", variable=self.seleccion, value=1)
        self.radio2.grid(column=1,row=3)
        #declara 3 radio button

        self.radio3=tk.Radiobutton(self.vent1, text="Multiplicar", variable=self.seleccion, value=1)
        self.radio3.grid(column=1,row=4)


        #boton que realizara la operacion
        self.boton1=tk.Button(self.vent1, text="Operar", command=self.operaciones)
        self.boton1.grid(column=1, row=5)

        #etiqueta del resultado
        self.label3=tk.Label(self.vent1, text="Resultado")
        self.label3.grid(column=1, row=6)

    def operaciones(self):

        if self.seleccion.get()==1:
            
                suma= int(self.dato1.get())+int(self.dato2.get())
                self.label3.configure(text=suma)

        if self.seleccion.get()==2:
             
                resta= int(self.dato1.get())-int(self.dato2.get())
                self.label3.configure(text=resta)

        if self.seleccion.get()==3:
             
                multi= int(self.dato1.get())* int(self.dato2.get())
                self.label3.configure(text=multi)

cal= Calculadora()
            
            
