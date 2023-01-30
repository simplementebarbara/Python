# Introduzca 3 valores por teclado que corresponden a 3 lados de un
# triángulo y que muestre por pantalla si es isósceles, equilátero o escaleno.

print("Escriba 3 valores correspondiente a lados de un triangulo")
num1= input("Primer lado : ")
num2= input("Segundo  lado : ")
num3= input("Tercer lado : ")

if (num1 == num2 and num1 == num3):
    print("Tiene 3 lados iguales, es un triángulo equilátero")
elif (num1 == num2 and num1 != num3  and num2 != num3):
    print("Tiene todos los lados diferentes, es un triángulo escaleno") 
else:
    print ("Tiene solo dos lados iguales, es un triángulo isósceles")
