#4) Escriba un programa por teclado que me escriba los
# números divisores de un número dado.


listaDivisores =[]
num = int(input("Introduzca un número:"))

for i in range (2,num+1):
    if num%i == 0:
        divisor = i
        listaDivisores.insert(i, divisor)
     

print("Lista de divisores: ",listaDivisores)


