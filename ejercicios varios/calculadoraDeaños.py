# from datetime import datetime 
 
# añoActual = datetime.now().year
# print("bienvenido a la calculadora de años")  
# añoNacimiento = input("coloca el año en el que naciste => ")  
# print(f"gracias por compartir la informacion este año cumples { 2025 - int(añoNacimiento)} años") 

lenguajes_programacion = [
    "Python",
    "Java",
    "C",
    "C++",
    "C#",
    "JavaScript",
    "TypeScript",
    "PHP",
    "Ruby",
    "Swift",
    "Kotlin",
    "Go",
    "Rust",
    "Scala",
    "Perl",
    "Objective-C",
    "R",
    "Dart",
    "Visual Basic",
    "MATLAB",
    "Lua",
    "Haskell",
    "Elixir",
    "Julia",
    "Fortran",
    "COBOL",
    "Shell",
    "SQL",
    "Assembly",
    "Prolog",
    "Erlang",
    "F#",
    "Groovy",
    "Scheme",
    "Ada",
    "Delphi",
    "Lisp"
]

lengToSearh = input("¿que lenguaje quieres buscar? => ") 
if lengToSearh in lenguajes_programacion:
    print("tenemos disponible dicho lenguaje") 
    response = input('¿Deseas aplicar al curso de dicho lenguaje? ') 
    if response == "si":
        name = input("ingresa tu nombre =>")
        phone = input("ingresa tu numero de telefono =>") 
        print("hemos guardado tu informacion nos pondremos en contacto contigo mas adelante") 
    if response == "no":
        print("¡Gracias por tu interés!")
        
else:
    print("no tenemos disponible dicho lenguaje")
# print(lang.index("go"))    