#funciones

def sumar(x1,x2):
    suma=x1+x2
    print("Suma: ",suma)
def restar (x1,x2):
    resta=x1-x2
    print("Resta: ",resta)

def multiplicar(x1,x2):
    multi=x1*x2
    print("Multiplicacion: ",multi)
def mostrar_mensaje():
    print("Programa de Calculadora")



mostrar_mensaje()
sumar(3,4)
restar(6,3)
multiplicar(2,2)

#funciones con return

def sumar1(x1,x2):
    sumar1=x1+x2
    return sumar1

def multiplicar1(x1,x2):
    multi1=x1*x2
    return multi1


print("El return de suma es: ", sumar1(3,3))

#funciones con return de listas

def sumar5(lista):
    suma=lista[0]+lista[1]
    return suma

print("El return de suma con lista es: ", sumar5([50,10]))
