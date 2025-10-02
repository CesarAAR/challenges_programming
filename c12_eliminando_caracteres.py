"""
Crea una función que reciba dos cadenas como parámetro (str1, str2)
e imprima otras dos cadenas como salida (out1, out2).
- out1 contendrá todos los caracteres presentes en la str1 pero NO
  estén presentes en str2.
- out2 contendrá todos los caracteres presentes en la str2 pero NO
  estén presentes en str1.
"""
def delete_characters(str1,str2):
    out1 = ""
    out2 = ""
    for i in range(0,len(str1)):
        if str1[i] in str2:
            continue
        else:
            out1+=str1[i]
    for j in range(0, len(str2)):
        if str2[j] in str1:
            continue
        else:
            out2+=str2[j]
    return out1, out2

str1 = input("Ingresa la primera cadena: ")
str2 = input("Ingresa la segunda cadean: ")

print(delete_characters(str1.lower(),str2.lower()))