"""
Escriba un programa en python que me dibuje lo siguiente,
hasta una cierta fila:
                                              *
                                             ***
                                            *****
                                           *******
                                          *********
El ejemplo anterior es para N=5.
"""
k=0
num = int (input("Introduzca las filas deseadas: "))

for i in range (1, num +1):
    blancos = " " * (num - i)
    estrellas = "*" * (2 * i -1)
    print(blancos + estrellas)
