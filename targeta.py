print("--bienvenido--")
print("--Ingrese su tarjeta al datafono--")
contraseña=(int(input("Ingrese PIN:")))
if contraseña <100:
    print("Su contraseña es incorrecta, no se podra realizar el pago")
else:
    print("Su contraseña es correcta, se podra realizar el pago")