"""
Crea una función que reciba un String de cualquier tipo y se encargue de
poner en mayúscula la primera letra de cada palabra.
- No se pueden utilizar operaciones del lenguaje que
  lo resuelvan directamente.
"""
def f_w_upper(cadenas):
    words = cadenas.split()
    res = ""
    for word in words:
        f_word = word[0].upper()
        r_word = word[1:]
        res+=(f_word+r_word)+" "
    return res

user_input = input("Ingresa cadena o palabra: ")
print(f_w_upper(user_input))
