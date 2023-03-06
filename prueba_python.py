# Definimos un diccionario con los valores de las monedas
valores_monedas = {'USD': 0.00021, 'EUR': 0.00020, 'JPY': 0.028, 'Rupia': 0.017, 'CHF': 0.00020}

# Definimos un diccionario con los porcentajes de intermediación para cada moneda
porcentajes_intermediacion = {'USD': 0.05, 'EUR': 0.07, 'JPY': 0.09, 'GBP': 0.1, 'CHF': 0.12}

# Pedimos al usuario que ingrese su información personal
nombre_usuario = input('Ingrese su nombre: ')
documento_identidad = input('Ingrese su documento de identidad: ')

# Pedimos al usuario que ingrese la moneda origen y la cantidad de dinero
moneda_origen = input('Ingrese la moneda origen (USD, EUR, JPY, GBP, CHF): ').upper()
cantidad_origen = float(input('Ingrese la cantidad de dinero: '))

# Verificamos que la moneda origen existe en el diccionario de valores de monedas
if moneda_origen not in valores_monedas:
    print('La moneda origen ingresada no existe')
else:
    # Pedimos al usuario que ingrese la moneda destino
    moneda_destino = len(input('Ingrese la moneda destino (USD, EUR, JPY, GBP, CHF): ').upper())

    # Verificamos que la moneda destino existe en el diccionario de valores de monedas
if moneda_destino not in valores_monedas:
    print('La moneda destino ingresada no existe')
else:
    # Calculamos el valor de la operación sin intermediación
    valor_sin_intermediacion = cantidad_origen * valores_monedas[moneda_origen] / valores_monedas[moneda_destino]

    # Calculamos el porcentaje de intermediación para la moneda origen
    porcentaje_intermediacion_origen = porcentajes_intermediacion[moneda_origen]

    # Calculamos el porcentaje de intermediación para la moneda destino
    porcentaje_intermediacion_destino = porcentajes_intermediacion[moneda_destino]

    # Calculamos el porcentaje de intermediación total
    porcentaje_intermediacion_total = porcentaje_intermediacion_origen + porcentaje_intermediacion_destino

    # Calculamos el valor de la operación con intermediación
    valor_con_intermediacion = cantidad_origen * valores_monedas[moneda_origen] / valores_monedas[moneda_destino] * (1 - porcentaje_intermediacion_total)

    # Verificamos si el porcentaje de intermediación supera el 10% del dinero expresado en pesos colombianos
if porcentaje_intermediacion_total * cantidad_origen * valores_monedas[moneda_origen] > 0.1:
    respuesta_usuario = input('El porcentaje de intermediación supera el 10% del dinero expresado en pesos colombianos. ¿Desea continuar? (S/N) ').upper()
    if respuesta_usuario == 'N':
        print('Operación cancelada')
else:
    # Mostramos los resultados al usuario
    print('Nombre: ', nombre_usuario)
    print('Documento de identidad: ', documento_identidad)
    print(int(valor_con_intermediacion))

