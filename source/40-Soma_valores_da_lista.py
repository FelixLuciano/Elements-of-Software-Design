# Soma valores da lista
# Faça uma função que recebe uma lista de números reais e retorna a soma de seus valores.
# O nome da sua função deve ser soma_valores.

def soma_valores (list):
    result = 0
    
    for item in list:
        result += item
    
    return result
