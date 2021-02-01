# Calcula fatorial
# Escreva uma função que recebe um número n e devolve o valor de n! = 1 ⋅ 2 ⋅ 3 ⋅ ⋯ ⋅n.
# O nome da sua função deve ser `fatorial`.

def fatorial (n):
    result = 1
    
    while n > 1:
        result *= n
        n -= 1
        
    return result
