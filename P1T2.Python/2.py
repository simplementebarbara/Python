# Programa que me nuestre los números primos anteriores a un número dado.

num = int (input("Introduce un numero: "))

if num > 2:
    for y in range (2, num):
        x=2
        esPrimo= True
        while esPrimo is True and x < y:
            if y % x == 0:
                esPrimo = False
            else:
                x += 1

        if esPrimo is True:
            print(y)
else:
    print("El numero no es valido")
       
    
