#  Validación de datos con condicionales:

#     Crea un menú que pregunte al usuario qué acción desea realizar:
#         Agregar producto
#         Mostrar inventario
#         Calcular estadísticas
#         Salir
#     Usa condicionales if, elif y else para procesar la opción elegida.
#     Si el usuario ingresa una opción inválida, muestra un mensaje de error y pide nuevamente la entrada.



productosInventario = [] #se crea arreglo para guardar los productos tipo un carrito de compras
def inventario ():   #funcion para lanzar el programa
    while True: #se usa un for while junto con el boolean True para ejecutar el programa siempre, y salga solo hasta que el usuario elija la opcion para salir 
        try: #se usa el try para probar todo el algoritmo
            opcion = int(input("¿Que deseas hacer? \n" #se piden una opcion para elegir la accion a realizar
            "1. Agregar producto \n" #opcion agregar producto
            "2. Mostrar inventario \n" #opcion mostrar inventario
            "3. Calcular estadistica \n" #opcion calcular estadistica
            "4. Salir\n")) #opcion para salir del programa
            if opcion == 1:  #si la opcion elegida es 1 se agrega un producto al inventario
                producto = { #se crea un diccionario para guardar los datos del producto
                    "nombre" : input("ingresa tu nombre => "), 
                    "precio": int(input("ingresa precio => ")),
                    "cantidad": int(input("ingresa la cantidad => ")) }  
                print("Producto agregado exitosamente") #mensaje de exito al agregar el producto
                productosInventario.append(producto) #se agrega el producto al inventario
            if opcion == 2:  #si la opcion elegida es 2 se muestra el inventario
                if not productosInventario : #si el inventario esta vacio se muestra un mensaje
                    print("no hay elementos en el inventario") 
                else: # si no esta vacio se muestra el inventario
                    print(productosInventario) 
            if opcion == 3: #si la opcion elegida es 3 se calcula la estadistica 
                if not productosInventario: #si el inventario esta vacio se muestra un mensaje
                    print("no hay elementos en el inventario para calcular estadisticas")
                else: #si no esta vacio se calcula la estadistica
                    totalProductos = len(productosInventario) #se calcula el total de productos en el inventario
                    totalValor = sum(producto["precio"] * producto["cantidad"] for producto in productosInventario) #se calcula el valor total del inventario
                    print(f"Total de productos: {totalProductos}") #se imprime el total de productos
                    print(f"Valor total del inventario: {totalValor}") #se imprime el valor total del inventario
                
            if opcion == 4: #si la opcion elegida es 4 se sale del programa
                break
        except ValueError:#en caso de elegir una opcion erronea se maneja el error de eleccion con el except
            print("ingresa una opcion valida")    

inventario() 

