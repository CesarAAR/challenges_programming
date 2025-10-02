"""
Crea un programa que invierta el orden de una cadena de texto
sin usar funciones propias del lenguaje que lo hagan de forma automática.
- Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""
#Opcion 1:
def invertir_cadenas1():
    user_input = input("Introduce una cadena: ")
    cadena = ""
    for i in range(0,len(user_input)):
        cadena +=user_input[-(i+1)]
    print(cadena)
#invertir_cadenas1()

#Opcion 2:
def invertir_cadenas2(user_input):
    cadena = ""
    for i in range(0,len(user_input)):
        cadena +=user_input[-(i+1)]
    print(cadena)
user_input = input("Introduce una cadena: ")
invertir_cadenas2(user_input)