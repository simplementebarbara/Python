# estructura de datos
# listas se pueden cambiar lista =[1,....]
#tuplas no se puede cambiar tupla = (1,2)
#diccionarios se puede modificar

#lista vacia
lista= []
#definir lista
lista2= [1,2,"nombre", 2.4, "aaa",10,12]
#imprime la lista pero empezando poer el final
print(lista2[-1])
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
#accerder a un tzo de lista
lista_trozo= lista2[2:5]
#imprime desde el principio hasta el indice 3
lista_2=lista2[:3]
print(lista_2)
#imprime desde indice 3 hasta el final
lista_3=lista2[3:]


print(lista_3)

#tupla, al crear una tupla ya no se puede cambiar, ni insertar ni borrar
tupla1 = (1,2,3,4)
print (tupla1[2])
tupla2=(1,2,"nombre",7,8)
#calcular longitud de tipla
print (len(tupla2))
#la lista dentro de la tupla si se puede cambiar
tupla3=(3,"!nombre",[1,2,3], 34)
tupla3[2].pop(0)

#puede haber dentro de una tupla otra tupla y no se le puede modificar
tupla4=(3,"!nombre",(1,2,3), 34)

#diccionarios

dic1 ={"color":1,"ancho": "grande", "alto":4}
print(dic1)
print(dic1["color"])
dic1["dimension"]=9
 #para eliminar en un diccionario
del(dic1["color"])
print(dic1)
#se añade tupla al diccionario
 dic1 =["tupla"]=(2,4,"cas")
 print(dic1)
 #acceder a una tupla en diccionario
 print(dic1["tupla"][2])


 #añadir tupla endiccionario
 dic2={"primero":  [2,3,4,5],"segundo":(3,5,6), "tercero":{"uno":4,"dos":6}}
 dic2["cuarto"]=(2,4,"ads")
 #coger datos de diccionario
 print(dic2["primero"][1])
  print(dic2["segundo":][1])
   print(dic2["tercero"][1])


 #para eliminar en un diccionario
 
