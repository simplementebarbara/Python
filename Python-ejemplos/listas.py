# estructura de datos
# listas se pueden cambiar lista =[1,....]
#tuplas no se puede cambiar tupla = (1,2)
#diccionarios se puede modificar

#lista vacia
lista= []
#definir lista
lista2= [1,2,"nombre", 2.4, "aaa"]
print (lista2[2])
#añade campo
lista2.append(4)
print (lista2)
#insertar
lista2.insert(1,"op")
print (lista2)
#borrado
lista2.pop(4)
print (lista2)

#acceder a una lista anidada
lista4= [3,"nombre",[2,43,3], "."]

#tupla, al crear una tupla ya no se puede cambiar, ni insertar ni borrar
tupla1 = (1,2,3,4)
print (tupla1[2])
tupla2=(1,2"nombre",7,8)
#calcular longitud de tipla
print (len(tupla2))
#la lista dentro de la tupla si se puede cambiar
tupla3=(3,"!nombre",[1,2,3], 34)
tupla3[2].pop(0)

#puede haber dentro de una tupla otra tupla y no se le puede modificar
tupla4=(3,"!nombre",(1,2,3), 34)

#diccionarios

dic1 ={"color":1,"ancho": "grande"}
print(dic1)
print(dic1["color"])
