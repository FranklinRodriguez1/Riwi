from servicios import agregarProductos, mostrarInventario, buscarProducto, actualizarProducto, eliminarProducto, calcularEstadisticas

    # Mantén un inventario en memoria como lista de diccionarios, donde cada producto tenga:
    #     {"nombre": str, "precio": float, "cantidad": int}
    # Crea un archivo principal app.py y un módulo servicios.py (o nombres equivalentes) con funciones:
    #     agregar_producto(inventario, nombre, precio, cantidad)
    #     mostrar_inventario(inventario)
    #     buscar_producto(inventario, nombre) → retorna el dict o None
    #     actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None)
    #     eliminar_producto(inventario, nombre)
    #     calcular_estadisticas(inventario) → retorna tupla/dict con métricas
    # Documenta cada función con docstring (qué hace, parámetros, retorno) y agrega comentarios breves.

inventario = []

while True:
    print("\n--- Menú de Inventario ---")
    print("1. Agregar Producto")
    print("2. Mostrar Inventario")
    print("3. Buscar Producto")
    print("4. Actualizar Producto")
    print("5. Eliminar Producto")
    print("6. Calcular Estadísticas")
    print("7. Salir")

    opcion = input("Seleccione una opción (1-7): ")
    try:
        if opcion == '1': 
            try:
                nombre = input("Nombre del producto: ")
                precio = float(input("Precio del producto: "))
                cantidad = int(input("Cantidad del producto: "))
                agregarProductos(inventario, nombre, precio, cantidad) 
            except ValueError:
                print("Error: Precio y cantidad deben ser numéricos.")
        elif opcion == '2': 
            if inventario == []:
                print("el inventario esta vacio") 
            else:
                mostrarInventario(inventario)
        elif opcion == '3': 
            try: 
                if inventario == []: 
                    print("el inventario esta vacio") 
                else:
                    nombreABuscar = input("Nombre del producto a buscar: ") 
                    buscarProducto(inventario, nombreABuscar)
            except ValueError:
                print("Error: Entrada inválida.")
        elif opcion == '4':
            nombre = input("Nombre del producto a actualizar: ")
            nuevo_precio = input("Nuevo precio (dejar vacío para no cambiar): ")
            nueva_cantidad = input("Nueva cantidad (dejar vacío para no cambiar): ")
            actualizarProducto(inventario, nombre, nuevo_precio or None, nueva_cantidad or None)
        elif opcion == '5':
            nombre = input("Nombre del producto a eliminar: ")
            eliminarProducto(inventario, nombre)
        elif opcion == '6':
            calcularEstadisticas(inventario)
        elif opcion == '7':
            print("Saliendo del programa.")
            break
    except ValueError:
        print("Error: Entrada inválida. Por favor, ingrese un valor numérico cuando se requiera.")

 

