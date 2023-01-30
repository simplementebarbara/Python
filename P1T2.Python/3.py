# 3) Escribir un programa que me muestre por pantalla si un
# número introducido por teclado es primo o no.

print("Comprobación de números primos")
num = int (input("Introduzca numero: "))
x = 2
noPrimo = False

if num > 1 and num != 0:
    while x <= num:
        if num % x == 0:
            noPrimo = True

        if noPrimo is False:
           print(str (num) + " es un numero primo.")
           x = num + 1
           
        else:
            print(str (num) + " no es un numero primo.")
            x = num + 1
    x+=1
else:
    print(str (num) + " no es un numero primo.")
    
       
