# Conta ocorrências de palavras
# Faça uma função que recebe uma lista de palavras e retorna um dicionário onde as chaves são as palavras, e o valor é a contagem de cada palavra. Por exemplo, se a lista for
# ['abobora', 'chuchu', 'abobora', 'abobora', 'chuchu']
# a função deve retornar
# {'chuchu': 2, 'abobora': 3}
# O nome da sua função deve ser conta_ocorrencias.

def conta_ocorrencias (palavras):
    ocorrencias = {}
    
    for palavra in palavras:
        if palavra in ocorrencias:
            ocorrencias[palavra] += 1
        else:
            ocorrencias[palavra] = 1

    return ocorrencias
