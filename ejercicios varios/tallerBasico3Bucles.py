import random
# Objetivo: Dominar for y while, control de iteraciones y sumatorias.
 
#     Contar del 1 al 10. 
for i in range(1, 11):
    print(i)
#     Sumatoria del 1 al n.
n = int(input("ingresa un numero para sumar hasta ese numero => "))
suma = 0
for i in range(1, n + 1):
    suma += i
print(f"La suma del todos los numeros del 1 al {n} es: {suma}")
#     Tabla de multiplicar.  
nume = int(input("ingresa un numero para ver su tabla de multiplicar")) 
for i in range(1, 11): 
    print(f"{nume} x {i} = {nume * i}")  
#     Contador regresivo con while. 
num = int(input("ingresa un numero para hacer un conteo regresivo => "))
while num >= 0:
    print(num)
    num -= 1    
#     Adivina el número (usar random).   
numero_secreto = random.randint(1, 15)
adivina = None
while adivina != numero_secreto:
    adivina = int(input("Adivina el número entre 1 y 15: "))
    if adivina < numero_secreto:
        print("Demasiado bajo.")
    elif adivina > numero_secreto:
        print("Demasiado alto.")
print("¡Felicidades! Adivinaste el número.")
#     Sumar hasta que el usuario escriba 0. 
total = 0
while True:
    numero = int(input("Ingresa un número para sumar (0 para terminar): "))
    if numero == 0:
        break
    total += numero
print(f"La suma total es: {total}")
