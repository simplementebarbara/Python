
#vamos a crear una funcion que va a llamar a otra 
def mayor(lista):

    mayor=0
    for fila in range(0,len(lista)):
        if lista[fila]>mayor:
            mayor= lista[fila]
    return mayor
