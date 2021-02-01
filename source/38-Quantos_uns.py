# Quantos uns?
# Escreva uma função que recebe um número e devolve a quantidade de vezes que o algarismo 1 ocorre nesse número. Ex: 1030110641 tem 4 ocorrências do algarismo 1.
# O nome da sua função deve ser `quantos_uns`.

def quantos_uns (value):
    number = str(value)

    count = 0
    for digit in number:
        if digit == "1":
            count += 1
            
    return count
