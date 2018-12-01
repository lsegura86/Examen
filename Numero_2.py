import string
import random

# Metodo generador de lista de palabras
def generador_palabras(tam_lista, num_palabra):
    lista = []
    alfabeto = string.ascii_letters

    while len(lista) < tam_lista:
        palabra = ''
        alfabeto = string.ascii_letters
        while len(palabra) < num_palabra:
            p = (random.choice(string.ascii_letters))
            if p not in palabra:
                if len(palabra) == 0:
                    palabra += p
                else:
                    if alfabeto.index(palabra[-1]) - alfabeto.index(p) != -1:
                        palabra += p
        lista.append(palabra)
        palabra = ''
    return lista

# Probar generador de palabras
print(generador_palabras(5,10))
print(generador_palabras(2,7))