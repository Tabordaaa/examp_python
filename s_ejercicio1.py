
#lavar ropa 
print("sistema para lavar tu ropa ")

metodo = int(input("si desea lavar a mano ingrese el numero 1, si desea lavar en lavadora ingrese el numero 2:"))
N = input("ingrese que materiales necesita separados por comas:")

if metodo == 1:
    print("ya sera dirigido a su punto de lavado a mano")
    print("sus materiales elegidos son:",N)
else:
    print("En un momento se le asignara una 2lavadora con un tiempo limite de 1 hora ")
    print("sus materiales elegidos son:",N) 
    

#EJERCICIO LLAMAR A UN AMIGO 
print("ES NECESARIO EL NUMERO DE LA PERSONA PARA COMUNICARSE POR TELEFONO CON ELLA")
num1=int(input("si tiene el numero ingrese el numero 1, si no lo tiene ingrese el numero 2:"))
import random
if num1 == 1:
    numA= int(input("ingrese el numero de la persona con la que se desea comunicar:"))
    print(random.choice(["disponible", "No disponible"]))
    print("Espere un momento, contactando la persona...")
else:
    print("Es necesario el numero de la persona o no sera posible comunicarse con ella")
