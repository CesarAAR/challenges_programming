"""
/*
Crea un programa que sea capaz de transformar texto natural a código
morse y viceversa.
- Debe detectar automáticamente de qué tipo se trata y realizar
  la conversión.
- En morse se soporta raya "—", punto ".", un espacio " " entre letras
  o símbolos y dos espacios entre palabras "  ".
"""
def to_morse(user_input):
    morse = {
        "a": ".-",
        "b": "-...",
        "c": "-.-.",
        "d": "-..",
        "e": ".",
        "f": "..-.",
        "g": "--.",
        "h": "....",
        "i": "..",
        "j": ".---",
        "k": "-.-",
        "l": ".-..",
        "m": "--",
        "n": "-.",
        "o": "---",
        "p": ".--.",
        "q": "--.-",
        "r": ".-.",
        "s": "...",
        "t": "-",
        "u": "..-",
        "v": "...-",
        "w": ".--",
        "x": "-..-",
        "y": "-.--",
        "z": "--..",
        
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",

        " ": "  ",
    }
    res = ""
    for i in range(0,len(user_input)):
        res+=morse[user_input[i]]+" "
    return res
user_input = input("Introduce una palabra o frase: ")
print(to_morse(user_input.lower()))