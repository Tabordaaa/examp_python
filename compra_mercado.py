
productos = ["manzanas", "peras", "plátanos", "naranjas", "sandías"]
precios = [1500, 2000, 1000, 2500, 5000]

compras = []
cantidades = []


while True:
    producto = input("Introduce un producto que quieras comprar (o escribe 'fin' para terminar): ")
    if producto == "fin":
        break
    elif producto not in productos:
        print("Lo siento, ese producto no está disponible.")
    else:
        cantidad = int(input("Introduce la cantidad que quieres comprar: "))
        compras.append(producto)
        cantidades.append(cantidad)


total = 0
for i in range(len(compras)):
    indice = productos.index(compras[i])
    precio = precios[indice]
    cantidad = cantidades[i]
    total += precio * cantidad


print("El precio total de la compra es: ", total)