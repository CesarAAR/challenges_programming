"""
Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 100.
"""
def is_primo():
    primo = []
    for i in range(2,101):
        b_primo = True
        for j in range(2,i):
            if i % j == 0:
                b_primo = False
                break
            else:
                continue
        if b_primo == True:
            primo.append(i)
    return primo
print(is_primo())