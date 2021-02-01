# Quantidade de primos no intervalo
# Escreva uma função que recebe dois números a e b e devolve a quantidade de números de primos p tais que a≤p≤b.
# O nome da sua função deve ser primos_entre.

def eh_primo (num):
    if num < 2 or num > 2 and num % 2 == 0:
        return False
    else:
        i = 3
        while i < num:
            if num % i == 0:
                return False
            i += 2

    return True


def primos_entre (a, b):
    count = 0
    number = a

    while number <= b:
        if eh_primo(number):
            count += 1
        number += 1

    return count
