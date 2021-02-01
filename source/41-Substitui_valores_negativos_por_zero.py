# Substitui valores negativos por zero
# Faça uma função que varre uma lista de inteiros e troca os elementos negativos por zero. Sua função recebe uma lista como argumento e deve retornar a lista com os valores substituídos.
# O nome da sua função deve ser 'zera_negativos'.

def zera_negativos (list):
    for i in range(0, len(list)):
        if list[i] < 0:
            list[i] = 0
            
    return list
