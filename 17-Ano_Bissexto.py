# Ano Bissexto
# Escreva uma função que recebe um número representando um ano e devolve True se um ano é bissexto e False caso contrário.
# O nome da sua função deve ser eh_bissexto.

def eh_bissexto (year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0
