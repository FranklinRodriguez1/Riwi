
    # Crea un archivo inventario.py.
    # Declara variables para nombre (string), precio (float) y cantidad (int).
    # Solicita al usuario estos datos con la función input().
    # Asegúrate de que el precio y la cantidad se conviertan correctamente a sus tipos numéricos usando float() e int().
    # Si el usuario ingresa un valor inválido, muestra un mensaje y vuelve a pedirlo.
productosInventario = [] 


def inventario ():   
    while True: 
        try:
            opcion = int(input("¿Que deseas hacer? \n"
            "1. agregar producto \n"
            "2. visualizar inventario \n" \
            "3. validar costo total"
            "5. Salir del programa \n"))
            if opcion == 1:  
                producto = {
                    "nombre" : input("ingresa tu nombre"), 
                    "precio": int(input("ingresa precio")),
                    "cantidad": int(input("ingresa la cantidad")) } 
                productosInventario.append(producto) 
                print(productosInventario) 
            if opcion == 2:  
                if not productosInventario : 
                    print("no hay elementos en el inventario") 
                else:
                    print(productosInventario) 
                if opcion == 3:
                    break
            if opcion == 5: 
                break
        except ValueError:
            print("ingresa una opcion valida")        
inventario() 

