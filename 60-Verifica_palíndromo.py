# Verifica palíndromo
# Faça uma função que recebe uma string e retorna True se ela for um palíndromo (é a mesma de trás para frente), ou False caso contrário. Por exemplo, a string 'roma é amor' é um palíndromo.
# Use fatiamento.
# Desafio 1: dá para fazer essa função com apenas 2 linhas de código.
# Desafio 2: resolva novamente sem usar fatiamento.
# O nome da sua função deve ser 'eh_palindromo'.

def eh_palindromo (text):
    rev_text = text[::-1]
    check = text == rev_text
        
    return check
