# Objetivo: Crear, recorrer, modificar y eliminar elementos en listas.

#     Lista de frutas. 
frutas = ["manzana", "banana", "cereza"]
print("Frutas iniciales:", frutas)
#     Agregar y eliminar frutas. 
frutas.append(input("Ingresa una fruta para agregar: ")) 

#     Buscar un elemento en la lista. 
frutaABuscar = input("ingresa una fruta para buscar=> ")
#     Lista de números y promedio.  
numeros = [10, 20, 30, 40, 50] 
promedio  = sum(numeros)/len(numeros)
print(f"el promedio de {numeros} es: {promedio}")
#     Números pares: guardar solo los pares. 
numeros_pares = [] 
for i in range(1, 21):
    if i % 2 == 0:
        numeros_pares.append(i)
#     Eliminar duplicados.
listaConDuplicados = [5, 6, 70, 5, 3, 1, 2, 8, 9, 9, 9, 8, ] 
sinDuplicados =list(set(listaConDuplicados))
ordenado = sorted(sinDuplicados, reverse=True)
print(ordenado)