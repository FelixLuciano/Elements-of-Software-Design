# Série de Fibonacci
# Faça uma função que recebe um número inteiro n e devolve uma lista contendo os n primeiros números da sequência de Fibonacci. O n-ésimo número da sequência de Fibonacci, definido como F_n, é dado por:
# F_n = F_{n-1} + F_{n-2}
# Com valores iniciais: F_1=1 e F_2=1.
# 1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,...
# O nome da sua função deve ser 'calcula_fibonacci'.

def calcula_fibonacci (length):
    fibo = [1, 1]
    
    while len(fibo) < length:
        fibo_n = fibo[-1] + fibo[-2]
        
        fibo.append(fibo_n)
        
    return fibo[0:length]
