# sirve para agregar produdctos al inventario
import time
from os import system 
from os import name

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
            

