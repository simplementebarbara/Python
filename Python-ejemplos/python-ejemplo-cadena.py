#listas

lista=[2,4,45,6,7,8]
lista1=["nombre","apellido", "dni"]
lista2=[2,4,"nombre",5.5]

print(lista2[3])

print("la longitud de la cadena: ", len(lista1))

for fila in range(1, len(lista1)):
    print(lista1[fila])

    #lista dentro de otra
lista4=[3,4,"nombre",[3,5,6.7,"apellido"],98]

print(lista4[3][2])

lista5=[3,4,"nombre",[3,5,["dd","rr"],6.7,"apellido"],98]
print(lista5[3][2][0])

#añade a lista lo pasado por paramatro. append()

lista1.append(7)

#imprime la lista entera
print(lista5)

#funcion para insertar donde yo quiera, se indica primero posicion y despues el
#elemento a insertar
lista1.insert(0,34)
print(lista1)


#para borrar la posicion que se pase por parametro
lista1.pop(1)
print(lista1)

#meter en una lista anidada dentro de otra algun valor
# lista5=[3,4,"nombre",[3,5,["dd","rr"],6.7,"apellido"],98]
print(lista5)
lista5[3][2].insert(0,"bb")
print(lista5)
#borrado de una lista anidada
lista5[3][2].pop(1)

#lista vacia. Se va insertando la lista elemento

lista=[]
x=0

while x<3:
        print("escriba el valor ",x+1 , " :")
        
        aux=int(input(""))
        lista.append(aux)
        x=x+1
        print(lista)
