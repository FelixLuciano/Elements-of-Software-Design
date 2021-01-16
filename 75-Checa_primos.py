# Checa primos
# Faça uma função que recebe uma lista de números e devolve um dicionário no qual as chaves são os números da lista e os valores são um booleano indicando se aquele número é primo ou não.
# O nome da sua função deve ser 'verifica_primos'.

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

def verifica_primos (number_list):
    is_prime = {}
    
    for number in number_list:
        is_prime[number] = eh_primo(number)
        
    return is_prime
