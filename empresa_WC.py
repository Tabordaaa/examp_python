nombre_t1 = input("ingrese el nombre del trabajor 1:")
sueldo_t1 = 0
tipo_proyect_t1 = input("ingrese el tipo de proyecto que realiza el trabajor 1:")
nombre_t2 = input("ingrese el nombre del trabajor 2:")
sueldo_t2 = 0
tipo_proyect_t2 = input("ingrese el tipo de proyecto que realiza el trabajor 2:")
nombre_t3 = input("ingrese el nombre del trabajor 3:")
sueldo_t3 = 0
tipo_proyect_t3 = input("ingrese el tipo de proyecto que realiza el trabajor 3:")
nombre_t4 = input("ingrese el nombre del trabajor 4:")
sueldo_t4 = 0
tipo_proyect_t4 = input("ingrese el tipo de proyecto que realiza el trabajor 4:")

if tipo_proyect_t1 == "A":
    sueldo_t1=20000
elif tipo_proyect_t1 == "B":
    sueldo_t1=10000
else:
    sueldo_t1=5000
    
if tipo_proyect_t2 == "A":
    sueldo_t2=20000
elif tipo_proyect_t2 == "B":
    sueldo_t2=10000
else:
    sueldo_t2=5000
    
if tipo_proyect_t3 == "A":
    sueldo_t3=20000
elif tipo_proyect_t3 == "B":
    sueldo_t3=10000
else:
    sueldo_t3=5000
    
if tipo_proyect_t4 == "A":
    sueldo_t4=20000
elif tipo_proyect_t4 == "B":
    sueldo_t4=10000
else:
    sueldo_t4=5000



sueldo_mensual_T1= (sueldo_t1*8)*30
sueldo_mensual_T2= (sueldo_t2*8)*30
sueldo_mensual_T3= (sueldo_t3*8)*30
sueldo_mensual_T4= (sueldo_t4*8)*30





print("Sueldo mensual", nombre_t1,"es:", sueldo_mensual_T1 )
print("----------------------------------------------------------")
print("Sueldo mensual", nombre_t2,"es:", sueldo_mensual_T2 )
print("----------------------------------------------------------")
print("Sueldo mensual", nombre_t3,"es:", sueldo_mensual_T3 )
print("----------------------------------------------------------")
print("Sueldo mensual", nombre_t4,"es:", sueldo_mensual_T4 )

