"""
Escribe una función que reciba un texto y retorne verdadero o
falso (Boolean) según sean o no palíndromos.
Un Palíndromo es una palabra o expresión que es igual si se lee
de izquierda a derecha que de derecha a izquierda.
NO se tienen en cuenta los espacios, signos de puntuación y tildes.
Ejemplo: Ana lleva al oso la avellana.
"""
def es_palindromo(cadena):
    cadena = cadena.replace(" ","")
    is_palindromo = True
    for i in range(0,len(cadena)):
        if cadena[i] == cadena[-(i+1)]:
            continue
        else:
            is_palindromo = False
            break
    if is_palindromo == True:
        return True
    else:
        return False

user_input = input("Ingrese una frase: ")
print(es_palindromo(user_input.lower()))