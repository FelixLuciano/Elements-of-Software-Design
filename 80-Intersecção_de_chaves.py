# Intersecção de chaves
# Faça uma função que recebe dois dicionários e devolve uma lista contendo as chaves que estão presentes em ambos os dicionários.
# O nome da sua função deve ser 'interseccao_chaves'.

def interseccao_chaves (dictionary_1, dictionary_2):
    keys = [*dictionary_1.keys(), *dictionary_2.keys()]
    
    return keys
