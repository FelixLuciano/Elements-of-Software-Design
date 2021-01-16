# Lista para dicionário
# Faça uma função que recebe duas listas com o mesmo tamanho e devolve um dicionário cujas chaves são os elementos da primeira lista e os valores são os elementos da segunda lista. Para pensar: para a resolução deste exercício faz diferença saber qual o tipo dos valores guardados nas listas?
# O nome da sua função deve ser 'monta_dicionario'.

def monta_dicionario (keys, values):
    items = zip(keys, values)
    dictionary = {}
    
    for key, value in items:
        dictionary[key] = value
        
    return dictionary
