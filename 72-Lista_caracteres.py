# Lista caracteres
# Faça uma função que recebe uma string e devolve uma lista contendo os caracteres dessa string, sem repetição. Ex: 'abacate' deve devolver ['a', 'b', 'c', 't', 'e'].
# O nome da sua função deve ser 'lista_caracteres'.

def lista_caracteres (string):
    characters = []

    for character in string:
        if not character in characters:
            characters.append(character)

    return characters
