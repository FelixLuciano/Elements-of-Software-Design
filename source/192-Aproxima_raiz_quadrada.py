# Aproxima raiz quadrada
# Faça uma função que recebe um número inteiro n e devolve o número inteiro mais próximo da sua raíz quadrada. Para isso você deve testar todos os números inteiros i a partir de 1 até que i elevado ao quadrado seja maior ou igual a n. A resposta será i-1 ou i. Dentre as duas opções, devolva o valor cujo quadrado seja mais próximo de n. Alguns exemplos:
# - Para n = 40, 7 é o primeiro número cujo quadrado (49) é maior ou igual a n. Assim, devemos avaliar os números 6 e 7 e escolher a opção cujo quadrado está mais próximo de 40. A resposta da sua função deve ser então o número 6, pois 36 é mais próximo de 40 do que 49.
# - Para n = 120, 11 é o primeiro número cujo quadrado (121) é maior ou igual a n. Assim, devemos avaliar os números 10 e 11 e escolher a opção cujo quadrado está mais próximo de 120. A resposta da sua função deve ser então o número 11, pois 121 é mais próximo de 120 do que 100.
# O nome da sua função deve ser 'aproxima_raiz'.

def aproxima_raiz (number):
    x1 = 1
    x1_squared = 1
    
    # Encontra valor de x1 tal que seu quadrado seja maior ou igual à number
    while x1_squared < number:
        x1 += 1
        x1_squared = x1**2
        
    x2 = x1 - 1
    x2_squared = x2**2
    
    # Encontra a enferença entre as raízes e o número
    x1_difference = abs(x1_squared - number)
    x2_difference = abs(x2_squared - number)
    
    # Encontra a raiz mais próxima com a raíz de menor diferença
    if x1_difference < x2_difference:
        closer_root = x1
    else:
        closer_root = x2
        
    return closer_root

# Feedback do professor:
# "O código está bem claro. Parabéns!"
