 # ___________________________ 


#     # Mayor de edad. 
# edad = int(input("¿vamos a validar tu edad?")) 
# if edad >= 18 :
#     print("Eres mayor de edad") 
# else:
#     ("no eres mayor de edad")

#     # Número positivo, negativo o cero.
# numeroPosNeg = float(input("Introduce cualquier número y te diré si es positivo o negativo")) 
# if numeroPosNeg > 0 :
#     print(f"el numero {numeroPosNeg} es positivo") 
# elif numeroPosNeg == 0:
#     print(f"el numero {numeroPosNeg} es nuetro")
# else:
#     print(f"el numero {numeroPosNeg} es negativo")
#     # validar si el numero es par o impar. 
# numeroParOImpar = int(input("ingresa un numero para validar si es par o impar "))
# if numeroParOImpar % 2 == 0:
#     print("el numero ingreso es par")    
# else:
#     print("el numero ingresado es impar")


#     # Calculadora básica con +, -, *, /.   
# print("---------------------Calculadora Basica---------------------")
# valor1 = int(input("ingresa primer valor => "))
# valor2 = int(input("ingresa segundo valor => ")) 

# operacion = input("¿que operacion desea realizar ( +, -, *, /)?") 
# while True:
#     if operacion == "+":
#         result = valor1 + valor2 
#         print(f"el resultado de la operacion es de {result}") 

#     elif operacion == "-":
#         result = valor1 - valor2  
#         print(f"el resultado de la operacion es de {result}")  
#     elif operacion == "*":
#         result = valor1 * valor2 
#         print(f"el resultado de la operacion es de {result}")  
#     elif operacion == "/":
#         result = valor1 / valor2 
#         print(f"el resultado de la operacion es de {result}")  
#     else:
#         print("debes elegir una operacion valida intenta de nuevo")
#         break 

#     # Clasificador de notas (Excelente, Aprobado, Reprobado). 
# nota = int(input("ingresa tus notas a clasificar (1 - 5)")) 
# if nota == 5: 
#     print("Felicidades eres excelente") 
# elif nota == 3:
#     print("Felicidades estas aprobado")
# else:
#     print("Estas reprobado")
    # Comparador de tres números: mayor y menor. 
print("bienvenido al comparador de numeros")
comparar1 = int(input("ingresa primer numero a comparar => "))
comparar2 = int(input("ingresa segundo numero a comparar => "))
comparar3 = int(input("ingresa tercer numero a comparar => ")) 
numerosOrdenado =[comparar1, comparar2, comparar3]    
numerosOrdenado.sort(reverse=True)
print(f"{numerosOrdenado[0]} es mayor que {numerosOrdenado[1]} y a su vez este mismo es mayor que {numerosOrdenado[2]}")

