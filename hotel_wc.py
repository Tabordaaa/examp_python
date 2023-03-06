# Definir las tarifas por tipo de habitación
tarifa_ind = 2500
TARIFA_DOBLE = 4600
TARIFA_FAMILIAR = 5200

# Pedir datos de entrada
cantidad_huespedes = int(input("Ingrese el número de huéspedes: "))
dias_estadia = int(input("Ingrese el número de días de estadía: "))

# Calcular el precio de la habitación
if cantidad_huespedes == 1:
    precio_hab = tarifa_ind * dias_estadia
elif cantidad_huespedes == 2:
    precio_hab = TARIFA_DOBLE * dias_estadia
else:
    precio_hab = TARIFA_FAMILIAR * dias_estadia

# Aplicar el descuento correspondiente
if cantidad_huespedes == 1:
    precio_hab_desc = precio_hab * 0.95
elif cantidad_huespedes == 2:
    precio_hab_final = precio_hab * 0.91
else:
    precio_hab_final = precio_hab * 0.85

# Imprimir el resultado final
print("El precio de la habitación es: $", precio_hab_final)