class Data:

def invertir_lista(self, lista):

    lista_invertida = []
    for i in range(len(lista) - 1, -1, -1):
        lista_invertida.append(lista[i])
    return lista_invertida

def buscar_elemento(self, lista, elemento):

    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return -1

def eliminar_duplicados(self, lista):

    lista_sin_duplicados = []
    for item in lista:
        if item not in lista_sin_duplicados:
            lista_sin_duplicados.append(item)
    return lista_sin_duplicados

def merge_ordenado(self, lista1, lista2):

    i, j = 0, 0
    lista_ordenada = []
    
    while i < len(lista1) and j < len(lista2):
        if lista1[i] < lista2[j]:
            lista_ordenada.append(lista1[i])
            i += 1
        else:
            lista_ordenada.append(lista2[j])
            j += 1
    
    while i < len(lista1):
        lista_ordenada.append(lista1[i])
        i += 1
        
    while j < len(lista2):
        lista_ordenada.append(lista2[j])
        j += 1

    return lista_ordenada

    
def rotar_lista(self, lista, k):

    if not lista:
        return []
    
    k = k % len(lista)
    return lista[-k:] + lista[:-k]

    
def encuentra_numero_faltante(self, lista):
    
    n = len(lista) + 1
    suma_total = n * (n + 1) // 2
    suma_lista = sum(lista)
    
    return suma_total - suma_lista


def es_subconjunto(self, conjunto1, conjunto2):

    for elemento in conjunto1:
        if elemento not in conjunto2:
            return False
    return True

    
def implementar_pila(self):
    pila = []
    return {
        "push": lambda x: pila.append(x),
        "pop": lambda: pila.pop() if pila else None,
        "peek": lambda: pila[-1] if pila else None,
        "is_empty": lambda: len(pila) == 0
    }

def implementar_cola(self):
    cola = []
    return {
        "enqueue": lambda x: cola.append(x),
        "dequeue": lambda: cola.pop(0) if cola else None,
        "peek": lambda: cola[0] if cola else None,
        "is_empty": lambda: len(cola) == 0
    }

def matriz_transpuesta(self, matriz):
    return [[fila[i] for fila in matriz] for i in range(len(matriz[0]))]
