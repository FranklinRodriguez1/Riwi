# Objetivo: Crear, recorrer, modificar y eliminar elementos en listas.

#     Lista de frutas. 
frutas = ["manzana", "banana", "cereza"]
print("Frutas iniciales:", frutas)
#     Agregar y eliminar frutas. 
frutas.append(input("Ingresa una fruta para agregar: "))  
print(f"estos son las frutas en el inventario{frutas}") 
frutaDelete = input("ingresa una fruta que quieras eliminar de lo contrario escribe x")

#     Buscar un elemento en la lista. 
frutaABuscar = input("ingresa una fruta para buscar=> ") 
for i in frutas: 
    if i == frutaABuscar: 
        print(f"el producto {i} ya se encuentra registrado") 
        
     

# ____________________________________________
#     Lista de números y promedio.
numeros = [10, 20, 30, 40, 50] 
promedio  = sum(numeros)/len(numeros)
print(f"el promedio de {numeros} es: {promedio}") 

# #     Números pares: guardar solo los pares.  
# def imparImpar (): #FUNCION PARA DEVOLVER PARES E IMPARES
#     numbers = [73, 24, 67, 52, 19, 88, 45, 90, 33, 12] 
#     pares = [] 
#     impares =[]
#     for i in numbers: 
#         if i % 2 == 0:
#             pares.append(i) 
#         else:
#             impares.append(i)   
#     print(f" estos son los numeros pares {pares}")
#     print(f"estos son los numeros impares {impares}")
# #_____________________________________________________
# for i in range(1, 21):
#     if i % 2 == 0:
#         numeros_pares.append(i)
#     Eliminar duplicados.
# listaConDuplicados = [5, 6, 70, 5, 3, 1, 2, 8, 9, 9, 9, 8, ] 
# sinDuplicados =list(set(listaConDuplicados))
# ordenado = sorted(sinDuplicados, reverse=True)
# print(ordenado)