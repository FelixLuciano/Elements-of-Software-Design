# Conta ocorrências de letras
# Faça uma função que recebe uma string e retorna um dicionário onde cada chave é uma letra da string, e cada valor é o número de ocorrências desta letra. Por exemplo, se passamos a string "banana nanica", a função devolve o dicionário:
# {'b': 1, 'a': 5, 'n': 4, ' ': 1, 'i': 1, 'c': 1}
# Nota importante: em geral as chaves do dicionário não estão ordenadas!
# O nome da sua função deve ser 'conta_letras'.

def conta_letras (texto):
    ocorrencias = {}
    
    for letra in texto:
        if letra in ocorrencias:
            ocorrencias[letra] += 1
        else:
            ocorrencias[letra] = 1

    return ocorrencias
