# Remove vogais
# Faça uma função que recebe uma string composta somente por letras minúsculas e a devolve removendo as vogais.
# O nome da sua função deve ser 'remove_vogais'.

def remove_vogais (text):
    no_vogals = ""

    for character in text:
        if not character in "aeiouAEIOU":
            no_vogals += character
    
    return no_vogals
