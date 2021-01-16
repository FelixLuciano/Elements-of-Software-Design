# Lista estritamente crescente
# Faça uma função que recebe uma lista de números e devolve outra lista contendo somente os números que formam uma sequência estritamente crescente a partir do primeiro elemento. Exemplos:
# - [1, 3, 2, 3, 4, 6, 5] deve devolver [1, 3, 4, 6]
# - [10, 1, 2, 3] deve devolver [10]
# - [10, 15, 11, 12, 13, 14] deve devolver [10, 15]
# - [1, 1, 2, 2, 3, 3] deve devolver [1, 2, 3]
# - [] deve devolver []
# O nome da sua função deve ser estritamente_crescente.

def estritamente_crescente (list):
    if len(list) <= 1:
        return list
    
    result = [ list[0] ]
    
    for number in list[1:]:
        if number > result[-1]:
            result.append(number)
            
    return result
