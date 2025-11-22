
Accion =  int(input("Que deseas hacer " \
"1.registrarme  2.Ingresar => "))

user = []
if Accion == 1:
    user.append({"name":input("Ingresa tu nombre"), "password":input("Ingresa tu contraseña")}) 
    print("usuario creado exitosamente")
    ingresoLuegoDeCreadoNuevoUser=input("¿deseas ingresar a tu usuario? 1.Si 2.No") 
    if int(ingresoLuegoDeCreadoNuevoUser) == 1:
        usuarioABuscar =input("ingresa tu usuario => ")
        contraseñaABuscar = input("ingresa tu contraseña =>") 
         
    else:
        print("gracias por tu registro")
elif Accion == 2:
    print("ingresado")

else:
    print("opcion invalida")