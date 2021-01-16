# Vencedor do jogo da velha
# Faça uma função que recebe um tabuleiro de jogo da velha e devolve o vencedor. O tabuleiro é representado por uma lista de listas como o mostrado a seguir:
#     [['X', 'O', 'X'], ['.', 'O', 'X'], ['O', '.', 'X']]
# Note que a lista acima é idêntica a:
#     [
#         ['X', 'O', 'X'],
#         ['.', 'O', 'X'],
#         ['O', '.', 'X']
#     ]
# Os jogadores são representados pelas letras maiúsculas 'X' e 'O'. Espaços em branco são representados pelo caractere '.'. Para vencer no jogo da velha, um jogador deve marcar todas as casas de uma mesma coluna, linha ou diagonal. No exemplo acima o 'X' é o vencedor, assim a função deve retornar o valor 'X', caso o 'O' seja o vencedor a função deve retornar 'O'. Caso não haja vencedor, a sua função deve retornar 'V'.
# Alguns exemplos:
# - Sua função deve retornar 'O' para as seguintes entradas:
#     [
#         ['X', 'O', 'O'],
#         ['.', 'O', 'X'],
#         ['O', '.', 'X']
#     ]
#     [
#         ['X', '.', 'X'],
#         ['O', 'O', 'O'],
#         ['.', 'O', 'X']
#     ]
# - Sua função deve retornar 'V' para o exemplo a seguir:
#     [
#         ['X', '.', 'X'],
#         ['X', 'O', 'O'],
#         ['O', 'X', 'O']
#     ]
# O nome da sua função deve ser 'verifica_jogo_da_velha'.
