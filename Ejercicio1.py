#Retornar un entero con los últimos dígitos de una lista de enteros
def ult_num(lista_enteros, value):
    if lista_enteros == []:
        return value
    return ult_num(lista_enteros[1:], (value*10)+(lista_enteros[0] % 10))

print(ult_num([435, 864, 524], 0))