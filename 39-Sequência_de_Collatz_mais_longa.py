# Sequência de Collatz mais longa
# Considere a seguinte sequência iterativa definida para os números inteiros positivos:
# \begin{align}
# n &\rightarrow n/2 (n\text{ é par}) \\
# n & \rightarrow 3n+1 (n\text{ é ímpar})
# \end{align}
# Usando a regra acima e começando com o número 13, geramos a seguinte sequência:
# 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
# Percebe-se que essa sequência (começando em 13 e terminando em 1) contém 10 termos. Apesar de ainda não ter sido provado (Problema de Collatz), acredita-se que a sequência sempre termina em 1, independentemente do número inicial.
# Faça um programa que determina qual número positivo inicial menor que 1000 gera a sequência de Collatz mais longa. Seu programa deve imprimir esse número.
# Nota: Uma vez que a sequência começa os números podem passar de 1000.
# Adaptado de https://projecteuler.net/problem=14

def is_odd (number):
    return bool(number % 2)

max_n = 0
count = 0

n0 = 0
n = n0

while n0 < 1000:
    counting = 0

    n0 += 1
    n = n0

    while n > 1:
        if is_odd(n):
            n = 3 * n + 1
        else:
            n = n / 2
        
        counting += 1

    if counting > count:
        max_n = n0
        count = counting

print(max_n)
