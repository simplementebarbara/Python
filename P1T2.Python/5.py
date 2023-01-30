# 5) Programa en python que me ordene 3 números, en el mayor,
# menor y mediano, o si son iguales o dos iguales, etc..

# Ponemos los números en una lista
numeros = []

#Agregamos 3 números
for i in range (3):
    numero = int (input("Introduce el numero  : "))
    numeros.append(numero)


# Asumir que el menor es el primero de la lista

menor = numeros [0]
mediano = numeros [1]
mayor = numeros [2]

#Recorrer y comparar
for numero in numeros:
    if numero < menor:
        menor = numero
    if numero > mayor:
        mayor = numero
    if numero < mayor and numero > menor:
        mediano=numero
        

print ("Mayor: ", mayor)
print ("Mediano: ", mediano)
print ("Menor: ", menor) 


      


   
