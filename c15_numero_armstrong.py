"""
Escribe una función que calcule si un número dado es un número de Armstrong
(o también llamado narcisista).
Si no conoces qué es un número de Armstrong, debes buscar información
al respecto.

Definición:
número entero igual a la suma de sus propios dígitos, 
cada uno elevado a la potencia del número total de dígitos
Por ejemplo, 153 es un número de Armstrong porque tiene tres dígitos y 
1³ + 5³ + 3³ = 1 + 125 + 27 = 153
"""

def num_armstrong(num):
    elevate = len(num)
    res = 0
    for i in range(0,elevate):
        res += ((int(num[i])**elevate))
    if res == int(num):
        return True
    else: 
        return False

user_input = input("Ingrese numero: ")
print(num_armstrong(user_input))

