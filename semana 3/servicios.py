# sirve para agregar produdctos al inventario
import time
from os import system 
from os import name
import csv
# def spiner():   
#     system("clear")
#     aviso = "cargando..."
#     print(aviso)  
#     time.sleep(0.4) 
#     system("clear")
#     aviso = "cargando.."
#     print(aviso) 
#     time.sleep(0.4) 
#     system("clear")
#     aviso = "cargando." 
#     print(aviso)
#     time.sleep(0.4)
#     system("clear")
#     aviso = "cargando"
#     print(aviso) 
#     time.sleep(0.4)  
#     system("clear") esta era mi funcion real de spiner pero no funcionaba en windows asi que hice esta otra
def spiner():   # funcion spiner que funciona en windows y linux
    comando_clear = "cls" if name == "nt" else "clear" #detecta el sistema operativo para usar el comando adecuado
    aviso_list = ["cargando...", "cargando..", "cargando.", "cargando"]
    
    for aviso in aviso_list: #este for es para dar la ilusion de cargaa se crea una lista con los diferentes estados de carga y se itera sobre ella
        system(comando_clear)
        print(aviso)
        time.sleep(0.4)
    system(comando_clear)
    
def validarInventario(inventario):
    if inventario == []:
        print("el inventario esta vacio")
        return True
    return False

def agregarProductos (inventario, nombre, precio, cantidad):
    spiner() # llama a la funcion spiner para que muestre la animacion de carga
    producto ={
        "nombre":str(nombre).lower(), 
        "precio": int(precio), 
        "cantidad": int(cantidad)}
    inventario.append(producto) 
    print(f"el producto {nombre} ha sido agregado al inventario")

def mostrarInventario(inventario):  
    spiner() # llama a la funcion spiner para que muestre la animacion de carga
    for element in inventario:
        print(f"nombre: {element["nombre"]} precio: {element["precio"]} cantidad: {element["cantidad"]} ")
# sirve para buscar un producto en el inventario 
def buscarProducto(inventario, nombreABuscar):     
        for producto in inventario: 
            if producto["nombre"].lower() == nombreABuscar.lower(): 
                print(f"producto encontrado: nombre: {producto['nombre']} precio: {producto['precio']} cantidad: {producto['cantidad']}")
                return
        print("producto no encontrado")
# sirve para actualizar un producto en el inventario

def actualizarProducto( nombre, inventario): 
    for producto in inventario: 
        if producto["nombre"].lower() == nombre.lower(): 
            print(f"producto encontrado: nombre: {producto['nombre']} precio: {producto['precio']} cantidad: {producto['cantidad']}")  
            nuevo_precio = int(input("ingresa el nuevo precio: "))
            nueva_cantidad = int(input("ingresa la nueva cantidad: ")) 

            producto["precio"] = nuevo_precio 
            producto["cantidad"] = nueva_cantidad
            print(f"el producto {nombre} ha sido actualizado a precio: {nuevo_precio} cantidad: {nueva_cantidad}") 
        else:
            print("producto no encontrado")
            return

# sirve para eliminar un producto del inventario
def eliminarProducto(inventario, nombre): 
    for producto in inventario: 
        if nombre.lower() == producto["nombre"].lower(): 
            spiner()
            inventario.remove(producto)  
            print(f"el producto {nombre} ha sido eliminado del inventario") 
            return
    print("producto no encontrado")  

# sirve para calcular las estadisticas del inventario
def calcularEstadisticas(inventario):  
    if not inventario:
        print("el inventario esta vacio")
        return 
    else:
        banco_total = 0
        for producto in inventario: 
            banco_total += int(producto["precio"]) * int(producto["cantidad"])
            spiner() 
            print(f"el inventario tiene {len(inventario)} elementos y el valor total es de: {banco_total}")




def guardarCSV(ruta, inventario):
    if not inventario:
        print("El inventario está vacío, no hay nada para guardar.")
        return
    try:
        with open(ruta, "w", newline="", encoding="utf-8") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(["nombre", "precio", "cantidad"])  # encabezado

            for producto in inventario:
                escritor.writerow([
                    producto["nombre"],
                    producto["precio"],
                    producto["cantidad"]
                ])

        spiner()
        print(f"Inventario guardado correctamente en {ruta}")

    except Exception as e:
        print(f"Ocurrió un error al guardar el archivo: {e}")


def cargarCSV(ruta, inventario):
    productos_cargados = []
    filas_invalidas = 0

    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            lector = csv.reader(archivo)
            encabezado = next(lector, None) #esto obtiene la primera fila del archivo

            # Validar encabezado obligatorio
            if encabezado != ["nombre", "precio", "cantidad"]:
                print("Error: El encabezado del CSV es inválido.")
                return inventario

            # Procesar filas
            for fila in lector:
                if len(fila) != 3:
                    filas_invalidas += 1
                    continue

                nombre, precio, cantidad = fila
                
                try:
                    precio = float(precio)
                    cantidad = int(cantidad)

                    if precio < 0 or cantidad < 0:
                        raise ValueError

                    productos_cargados.append({
                        "nombre": nombre.lower(),
                        "precio": precio,
                        "cantidad": cantidad
                    })

                except ValueError:
                    filas_invalidas += 1

    except FileNotFoundError:
        print("Error: archivo no encontrado.")
        return inventario
    except UnicodeDecodeError:
        print("Error: problema con la codificación del archivo.")
        return inventario
    except Exception as e:
        print(f"Error inesperado: {e}")
        return inventario

    # Decidir acción con el inventario
    print("\nArchivo leído correctamente.")
    print(f"Productos válidos encontrados: {len(productos_cargados)}")
    print(f"Filas inválidas omitidas: {filas_invalidas}")

    opcion = input("¿Sobrescribir inventario actual? (S/N): ").strip().upper()

    if opcion == "S":
        inventario = productos_cargados
        accion = "Sobrescritura"
    else:
        accion = "Fusión"
        for nuevo in productos_cargados:
            existe = False
            for actual in inventario:
                if actual["nombre"] == nuevo["nombre"]:
                    actual["cantidad"] += nuevo["cantidad"]  
                    actual["precio"] = nuevo["precio"]        
                    existe = True
                    break
            if not existe:
                inventario.append(nuevo)

    spiner()
    print("\nResumen de carga:")
    print(f"Productos cargados: {len(productos_cargados)}")
    print(f"Filas inválidas: {filas_invalidas}")
    print(f"Acción realizada: {accion}")

    return inventario

