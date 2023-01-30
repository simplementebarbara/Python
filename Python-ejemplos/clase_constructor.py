#definir una clase
class operaciones:

    numero1=10
    numero2=20

# metodo init es como constructor de clase
#    def __init__(self):
#        self.numero1=int(input("Introduzca el primer numero "))
#         self.numero2=int(input("Introduzca el segundo numero "))

## constructor con argumentos
    def __init__(self, a,b):
         self.numero1=a
         self.numero2=b

#Se llama despues el metodo suma
#oper=operaciones(10,20)
#oper=sumar

#metodo str sirve para que cuando nos creemos un objeto, tenga el objeto un toString, con pasar el objeto a un print, ya imprime
    def __str__(self):
        cadena="El objeto es: "+str(self.numero1)+ " y "+ str(self.numero2)
        return cadena

#oper=operaciones()
#print(oper)

#metodo add para coger diferentes atributos de objetos del mismo tipo
    def __add__(self, objeto2):
        suma=sel.numero1 + objeto2.numero1
        return suma

#metodo para comparar dos objetos

    def __eq__(self, objeto2):
       if self.numero1==objeto2.numero1:
            return True
       else:
            return False
    
#definir metodos
    def sumar(self):

        suma= self.numero1+ self.numero2
        print ("La suma es: ", suma)

    def teclado(self):

        self.numero1=int(input("Introduzca el primer numero "))
        self.numero2=int(input("Introduzca el segundo numero "))

    def restar(self):

        resta= self.numero1 - self.numero2
        print("La resta es: ", resta)

    def multiplicar (self):
        mult= self.numero1* self.numero2
        print("La multiplicacion es: ", mult)


        
#oper=operaciones()
#print(oper)

#oper1=operaciones(10,20)
#oper2=operaciones(10,2)
#print(oper1.numero1+oper2.numero2)

#comprobacion metodo __sq__
"""if oper1==oper2:
    print("Son iguales")
else:
    print("No son iguales")
    """

