"""

Escriba la siguiente pirámide en python:

                                                 1
                                                121
                                               12321
                                              1234321
El ejemplo anterior es para N=4.
"""
num = int(input("Introduzca cuántas filas desea que tenga la piramide: "))
def piramideNumeros(num):
    """
    Función que dibuja una pirámide con n filas
    """
    for i in range(1, num+1):
        # Escribimos espacios en blanco a la izquierda para centrar la pirámide
        print(" " * (num-i), end="")
        # Escribimos los números de la fila
        for j in range(1, i+1):
            print(j, end="")
        # Escribimos los números de la fila en orden inverso
        for j in range(i-1, 0, -1):
            print(j, end="")
        print()

piramideNumeros(num)
