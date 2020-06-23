#Armar una lista de listas con los enteros formados por los múltiplos de 3 de los dígitos de los enteros de una lista
def digito_inicial(num):
    if num >= 10:
        return digito_inicial(num//10) + [3*(num%10)]
    return [3*num]

def lista_final(lista, sobra):
    if lista != []:
        return lista_final(lista[1:],sobra + [digito_inicial(lista[0])])
    return sobra
def main(lista):
    return lista_final(lista,[])

print(main([237, 458, 691]))
