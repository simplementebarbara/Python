"""
Escriba un programa en python que me muestre por pantalla
si un número es primo y si no lo es que me escriba el número
en factores primos, por ejemplo:


    20=2^2*5

"""

def es_primo(num):
    """
    Función que devuelve True si el número es primo y False en caso contrario
    """
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def factores_primos(num):
    """
    Función que escribe el número en factores primos
    """
    i = 2
    contador = 0
    while num > 1:
        # Si el número es divisible por i, dividimos el número y aumentamos el contador
        if num % i == 0:
            num /= i
            contador += 1
        else:
            # Si no es divisible, imprimimos el resultado y reiniciamos el contador
            if contador > 0:
                print(f"{i}^{contador}", end="*")
                contador = 0
            # Incrementamos i y buscamos el siguiente número primo
            i += 1
            while not es_primo(i):
                i += 1
    # Imprimimos el resultado final
    if contador > 0:
        print(f"{i}^{contador}", end="")

# Pedimos al usuario un número
num = int(input("Introduce un número: "))

# Comprobamos si es primo o no
if es_primo(num):
    print(f"{num} es primo.")
else:
    print(f"{num} no es primo, sus factores primos son: ", end="")
    factores_primos(num)
