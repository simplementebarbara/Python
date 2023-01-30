#definir una clase
class operaciones:

    numero1=10
    numero2=20
    
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


#Crear un  objeto

oper =operaciones()
#llamamos del objeto operaciones sus metodos
oper.sumar()
oper.teclado()
oper.multiplicar()
