# Dado un árbol binario ordenado, retornar una lista de listas con los dígitos de cada número en el árbol, 
# manteniendo el orden de los elementos
class Nodo():
    def __init__(self,valor,izquierda = None, derecha = None):
        self.valor = valor
        self.izquierda = izquierda
        self.derecha = derecha

def organizado(arbol_binario):
    if arbol_binario == None:
        return []
    return organizado(arbol_binario.izquierda) + [[arbol_binario.valor]] + organizado(arbol_binario.derecha)

print(organizado(Nodo(30,Nodo(15,None,Nodo(50)),Nodo(20))))