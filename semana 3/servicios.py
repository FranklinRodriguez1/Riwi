# sirve para agregar produdctos al inventario
import time
from os import system

def spiner():  
    system("clear")
    aviso = "cargando..."
    print(aviso)  
    time.sleep(0.4) 
    system("clear")
    aviso = "cargando.."
    print(aviso) 
    time.sleep(0.4) 
    system("clear")
    aviso = "cargando." 
    print(aviso)
    time.sleep(0.4)
    system("clear")
    aviso = "cargando"
    print(aviso) 
    time.sleep(0.4)  
    system("clear")

    

def agregarProductos (inventario, nombre, precio, cantidad):
    spiner() # llama a la funcion spiner para que muestre la animacion de carga
    producto ={"nombre":str(nombre).lower(), "precio": int(precio), "cantidad": int(cantidad)}
    inventario.append(producto) 
    print(f"el producto {nombre} ha sido agregado al inventario")

def mostrarInventario(inventario):  
    spiner() # llama a la funcion spiner para que muestre la animacion de carga
    print(f"en el inventario se encuentran los siguientes productos \n"\
          "\n" \
          f"{inventario}")
# sirve para buscar un producto en el inventario 

def buscarProducto(inventario, nombre): 
    for producto in inventario:
        if producto["nombre"] == nombre.lower():
            print(f"el producto {nombre} ha sido encontrado en el inventario")
            print(f" el producto {nombre} no se encuentra en el inventario y esta en la posicion {inventario.index(producto)} del inventario {producto}")
            return
# sirve para actualizar un producto en el inventario

def actualizarProducto(inventario, nombre): 
    print("actualizando producto")  

# sirve para eliminar un producto del inventario
def eliminarProducto(inventario, nombre):
    print("eliminando producto") 

# sirve para calcular las estadisticas del inventario
def calcularEstadisticas(inventario):
    print("calculando estadisticas")  
