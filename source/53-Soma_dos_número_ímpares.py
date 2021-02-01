# Soma dos número ímpares
# Faça uma função que recebe uma lista de números e devolve a soma dos números ímpares contidos nela.
# O nome da sua função deve ser soma_impares.

def is_odd (number):
    return number % 2 == 1

def soma_impares (numbers):
    result = 0
    
    for number in numbers:
        if is_odd(number):
            result += number
            
    return result
