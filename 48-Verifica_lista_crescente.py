# Verifica lista crescente
# Faça uma função que recebe uma lista e decide se a lista é estritamente crescente. Em caso positivo a função deve devolver True, em caso negativo, False.
# O nome da sua função deve ser eh_crescente.

def eh_crescente (numbers):
    i = 0
    while(i < len(numbers) - 1):
        number = numbers[i]
        next_number = numbers[i + 1]

        if not number < next_number:
            return False

        i += 1
        
    return True
