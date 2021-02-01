# Maior primo menor que N
# Escreva uma função que recebe um número inteiro n e devolve o maior número primo menor ou igual a n. Caso não haja nenhum número primo que se encaixe nessa situação (ex: números negativos), devolva -1. Dica: Escreva uma função auxiliar que devolve True se o número é primo e False caso contrário.
# O nome da sua função deve ser maior_primo_menor_que.

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

def maior_primo_menor_que (num):
    while num > 0:
        if eh_primo(num):
            return num
        num -= 1
    return -1
