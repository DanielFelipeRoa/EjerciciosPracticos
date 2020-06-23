#Para una lista de listas retornar una lista de tuplas con el mayor, menor y la suma del mayor y menor de cada sublista

def grande(lista_enteros, mayor):
    if lista_enteros == []:
        return mayor
    elif lista_enteros[0] > mayor:
        return grande(lista_enteros[1:], lista_enteros[0])
    return grande(lista_enteros[1:], mayor)


def pequeño(lista_enteros, menor):
    if lista_enteros == []:
        return menor
    elif lista_enteros[0] < menor:
        return pequeño(lista_enteros[1:], lista_enteros[0])
    return pequeño(lista_enteros[1:], menor)


def suma(lista):
    return grande(lista, 0)+pequeño(lista, grande(lista, 0))


def mis_tuplas(lista, sobra):
    if lista != []:
        return mis_tuplas(lista[1:], sobra + [[grande(lista[0], 0), pequeño(lista[0], grande(lista[0], 0)), suma(lista[0])]])
    return sobra


def main(lista):
    return mis_tuplas(lista, [])


print(main([[3, 2, 1, 6], [2, 4, 7]]))