# Número igual ao índice
# Faça uma função que recebe uma lista de números e devolve uma lista com os números que são iguais ao índice no qual eles se encontram. Exemplos:
# - [1, 3, 2, 4] deve retornar [2]
# - [0, 10, 2, 30, 4] deve retornar [0, 2, 4]
# - [5, 4, 3, 2, 1] deve retornar uma lista vazia
# O nome da sua função deve ser numero_no_indice.

def numero_no_indice (list):
    result = []
    
    for i in range(0, len(list)):
        item = list[i]
        
        if i == item:
            result.append(item)
            
    return result
