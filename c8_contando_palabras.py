"""
Crea un programa que cuente cuantas veces se repite cada palabra
y que muestre el recuento final de todas ellas.
- Los signos de puntuación no forman parte de la palabra.
- Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
- No se pueden utilizar funciones propias del lenguaje que
lo resuelvan automáticamente.
"""
def count_words():
    user_input = input("Introduce una frase: ")
    words = user_input.lower().split()
    repeat_words = []
    res = []
    for i in range(0,len(words)):
        count = 0
        if words[i] in repeat_words:
            continue
        else:
            for j in range(0,len(words)):
                if words[i] == words[j]:
                    count+=1
                else:
                    continue
            res.append([words[i],count])
            repeat_words.append(words[i])
    return res
print(count_words())