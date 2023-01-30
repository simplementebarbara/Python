"""
Escriba un programa que me escriba todas las variaciones posibles
de números con 4 cifras
con las cifras 1,2,3,4,5 sin y con repetición.
"""

contador = 0
for x1 in range(1,6):
    for x2 in range(1,6):
        for x3 in range(1,6):
            for x4 in range(1,6):
                if x1 != x2 and x1 != x3 and x1 != x4 and x2 != x3 and x2 != x4 and x3 != x4:
                    contador +=1
                    print(x1, end=",")
                    print(x2, end=",")
                    print(x3, end=",")
                    print(x4)
print("Total de variaciones sin repetición : ", contador)   

#Numero de variaciones con repetición          
contador2 = 0
for x1 in range(1,6):
    for x2 in range(1,6):
        for x3 in range(1,6):
            for x4 in range(1,6):
                    contador2 +=1
                    print(x1, end=",")
                    print(x2, end=",")
                    print(x3, end=",")
                    print(x4)
print("Total de variaciones con repetición : ", contador2)  
