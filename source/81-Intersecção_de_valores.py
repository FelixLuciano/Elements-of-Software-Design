# Intersecção de valores
# Faça uma função que recebe dois dicionários e devolve uma lista contendo os valores que estão presentes em ambos os dicionários.
# O nome da sua função deve ser 'interseccao_valores'.

def interseccao_valores (*dictionaryes):
    values = [values for dictionary in dictionaryes for values in dictionary.values()]
    
    return values
