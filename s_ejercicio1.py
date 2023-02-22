
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
    