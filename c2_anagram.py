"""
Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
- Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.
"""
def is_anagram():
    first_input = input("Enter first word: ")
    second_input = input("Enter second word: ")
    f = first_input.lower()
    s = second_input.lower()
    if len(f) == len(s):
        i = 0
        while i < len(s):
            if f[i] == s[-(i+1)]:
                i+=1
            else:
                return False
        return True
    else:
        print("The words aren't anagrams")

print(is_anagram())