# Primeira ocorrência de cada caractere
# Faça uma função que recebe uma string e devolve um dicionário com o índice da primeira ocorrência de cada caractere na string. Exemplo:
# Entrada: 'abracadabra'
# Saída: {'a': 0, 'b': 1, 'r': 2, 'c': 4, 'd': 6}
# O nome da sua função deve ser primeiras_ocorrencias.

def primeiras_ocorrencias (text):
    characters = {}
    
    for index, character in enumerate(text):
        if not character in characters:
            characters[character] = index
    
    return characters
