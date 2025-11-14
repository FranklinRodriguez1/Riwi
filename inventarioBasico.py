
    # Crea un archivo inventario.py. 
    # Declara variables para nombre (string), precio (float) y cantidad (int).
    # Solicita al usuario estos datos con la función input().
    # Asegúrate de que el precio y la cantidad se conviertan correctamente a sus tipos numéricos usando float() e int().
    # Si el usuario ingresa un valor inválido, muestra un mensaje y vuelve a pedirlo. 


    # Crea una variable llamada costo_total.
    # Almacena en ella el resultado de multiplicar el precio por la cantidad (precio * cantidad).
    # Asegúrate de que la operación se realice después de validar los datos de entrada. 


    # Usa la función print() para mostrar un mensaje con:
    #     Nombre del producto
    #     Precio unitario
    #     Cantidad
    #     Costo total calculado
    # El formato del mensaje debe ser claro, por ejemplo: "Producto: Lápiz | Precio: 500 | Cantidad: 3 | Total: 1500"




while True:
    try: 
        nombre = str(input("ingresa tu nombre (solo letras)"))
        precio = float(input("ingresa precio (solo numeros evita colocar  , . o cualquier caracter especial)"))  
        cantidad = int(input("ingresa cantidad (solo numeros )"))   
        costoTotal = 0  #se genera variable para guardar el precio de completo de la operacion
        # se solicita datos al cliente para la validar operacion correspondiente  
        costoTotal += precio * cantidad #operacion  de precio por cantidad para que el costo total se al correcto
        print(f"""nombre del producto es :{nombre} \n 
              Precio unitario es :{precio} \n 
              Cantidad es :{cantidad} \n 
              Costo total calculado es :{costoTotal}""") #se imprime el resultado total de todas las operacion
        break
    except ValueError: #se maneja el error al inscribir un error en el programa
            print("Valor invalido ingresa el dato solicitado de manera correcta")
  

#   es un programa basico que sirve para registrar productos comprados y valida cuando es el gasto que se hace basandose en la cantidad






