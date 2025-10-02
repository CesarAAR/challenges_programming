"""
Crea un programa se encargue de transformar un número
decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
"""
def decimal_to_binary(user_input):
    numbers = ""
    binary = []
    while int(user_input) != 0:
        if user_input % 2 != 0:
            binary.append(1)
        else:
            binary.append(0)
        user_input/=2
    for i in range(0,len(binary)):
        numbers+=str(binary[-(i+1)])
    return numbers
user_input = int(input("Introduce un numero: "))
print(decimal_to_binary(user_input))