# Objetivo: Crear, recorrer, modificar y eliminar elementos en listas.
frutas = ["manzana", "banana", "cereza"]

while True:    
    # Lista de frutas.  
    option = input("¿Que Deseas Hacer?\n"
    "1 . Ver listado de frutas \n" 
    "2 . Agregar frutas\n" 
    "3 . Eliminar frutas \n" 
    "4 . Buscar una fruta dentro de la lista\n" 
    "5 . Salir \n") 
    #mostrar frutas 
    if int(option) == 1:
        print(frutas)  
    # Agregar frutas
    if int(option) == 2:
        frutas.append(input("Ingresa una fruta para agregar: "))   
        print("fruta Agregada") 
        for i in frutas:
            print(i)   
    # eliminar frutas. 
    if int(option) == 3:
        frutaDelete = input("ingresa una fruta que quieras eliminar de lo contrario escribe x") 
        for i in frutas: 
            if frutaDelete == i:
                frutas.remove(i)  
                print("Elemento eliminado") 
                print(f"objetos en inventario {i}")
    #     # Buscar un elemento en la lista. 
    if int(option) == 4:
        frutaABuscar = input("ingresa una fruta para buscar=> ") 
        for i in frutas: 
            if i == frutaABuscar: 
                print(f"el producto {i} ya se encuentra registrado")  
    if int(option) == 5: 
        print("¡¡Que tengas feliz dia!!")
        break

# Lista de números y promedio.
# numeros = [10, 20, 30, 40, 50] 
# promedio  = sum(numeros)/len(numeros)
# print(f"el promedio de {numeros} es: {promedio}") 

# #     Números pares: guardar solo los pares.  
# def imparImpar i(): #FUNCION PARA DEVOLVER PARES E IMPARES
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
#         numerospares.append(i)
#     # Eliminar duplicados.
# listaConDuplicados = [5, 6, 70, 5, 3, 1, 2, 8, 9, 9, 9, 8, ] 
# sinDuplicados =list(set(listaConDuplicados))
# ordenado = sorted(sinDuplicados, reverse=True)
# print(ordenado)