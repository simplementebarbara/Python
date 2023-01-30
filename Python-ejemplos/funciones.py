#funciones  que averigue cual es el numero mayor
def mayor(n1,n2,n3):
    if n1>=n2 and n1>=n3:
        print ("El mayor es: " ,n1)
    if n2>=n1 and n2>=n1:
        print ("El mayor es: ", n2)
    elif n3>=n1 and n3>=n2:
        print("El mayor es: ", n3)

mayor(3,6,8)

#funciones con return
def mayor1(n1,n2,n3):

    mayor= 0
    if n1>=n2 and n1>=n3:
        mayor= n1
    if n2>=n1 and n2>=n1:
        mayor= n2
    elif n3>=n1   and n3>=n2: 
       mayor= n3
    return mayor

print ("el mayor es: ", mayor1(10,50,69))
