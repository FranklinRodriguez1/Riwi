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

def buscarProducto(inventario, nombre):   
        nombre = nombre.lower()
        for producto in inventario:   
            if producto["nombre"].lower() == nombre:
                print(producto)   
                return
        print("producto no encontrado")
# sirve para actualizar un producto en el inventario

def actualizarProducto(inventario, nombre): 
    print("actualizando producto")  

# sirve para eliminar un producto del inventario
def eliminarProducto(inventario, nombre):
    print("eliminando producto") 

# sirve para calcular las estadisticas del inventario
def calcularEstadisticas(inventario):
    print("calculando estadisticas")  
