# Inverte dicionário
# Escreva uma função que recebe um dicionário cujas chaves são nomes de pessoas (strings) e os valores são suas respectivas idades (números inteiros). A função deve devolver um novo dicionário cujas chaves são idades e os valores são listas de strings com os nomes das pessoas que têm aquela idade. Exemplo:
# Entrada: {'Ana': 19, 'Bruno': 18, 'João': 19}
# Saída: {18: ['Bruno'], 19: ['Ana', 'João']}
# O nome da sua função deve ser inverte_dicionario.

def inverte_dicionario (dictionary):
    inverted = dict()
    
    for key, value in dictionary.items():
        new_key = str(value)
        
        if not new_key in inverted:
            inverted[new_key] = list()

        inverted[new_key].append(key)
        
    return inverted
