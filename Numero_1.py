#Metodo para ordenar la lista
def ordenar_lista(lista):
    return sorted(lista, key=len, reverse=True)

# Probando el metodo definido
lista = ['a', 'zc', 'def', 'z', 'ef']
print(ordenar_lista(lista))

