# Primos no intervalo
# Faça uma função que recebe dois números a e b e devolve uma lista com todos os números primos p tais que a≤p≤b em ordem crescente.
# O nome da sua função deve ser primos_entre.

def eh_primo (number):
    if number < 2 or number > 2 and number % 2 == 0:
        return False
    else:
        i = 3
        while i < number:
            if number % i == 0:
                return False
            i += 2

    return True


def primos_entre (a, b):
    primes = []
    
    for number in range(a, b):
        if eh_primo(number):
            primes.append(number)
            
    return primes
