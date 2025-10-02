"""
Crea una única función (importante que sólo sea una) que sea capaz
de calcular y retornar el área de un polígono.
- La función recibirá por parámetro sólo UN polígono a la vez.
- Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
- Imprime el cálculo del área de un polígono de cada tipo.
"""
#Opcion 1:
def areas_poligonos1():
    user_input = input("1 = Triangulo\n2 = Cuadrado\n3 = Rectangulo\nSelección? R = ")
    match int(user_input):
        case 1:
            b = int(input("Introduce la Base: "))
            a = int(input("Introduce la Altura: "))
            res = (b*a)/2
            print("El area del triangulo es:", res)
        case 2:
            l = int(input("Introduce el lado: "))
            res = l*l
            print("El area del cuadrado es:", res)
        case 3:
            b = int(input("Introduce la Base: "))
            a = int(input("Introduce la Altura: "))
            res = b*a
            print("El area del rectangulo es:", res)
        case _:
            print("No se seleccionó ninguno")
#areas_poligonos1()

#Opcion 2:
def areas_poligonos2(user_input):
    match user_input:
        case 1:
            b = int(input("Introduce la Base: "))
            a = int(input("Introduce la Altura: "))
            res = (b*a)/2
            print("El area del triangulo es:", res)
        case 2:
            l = int(input("Introduce el lado: "))
            res = l*l
            print("El area del cuadrado es:", res)
        case 3:
            b = int(input("Introduce la Base: "))
            a = int(input("Introduce la Altura: "))
            res = b*a
            print("El area del rectangulo es:", res)
        case _:
            print("No se seleccionó ninguno")

#user_input = int(input("1 = Triangulo\n2 = Cuadrado\n3 = Rectangulo\nSelección? R = "))
#areas_poligonos2(user_input)