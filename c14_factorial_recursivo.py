"""
Escribe una función que calcule y retorne el factorial de un número dado
de forma recursiva.
"""

def factorial(num):
    num = int(num)
    if num == 1:
        return 1
    else:
        return num * factorial(num-1)

user_input = input("Ingrese un numero: ")
print(factorial(user_input))