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

def verifica_linha (character, line):
    return all([letter == character for letter in line])

def verifica_jogo_da_velha (table):
    # Itera cada letra
    for character in ("X", "O"):
        # Itera linhas do tabuleiro
        for line in table:
            # Verifica se alguma linha está preenchida somente com uma letra
            if verifica_linha(character, line):
                return character
        
        # Itera colunas do tabuleiro
        for column_i in range(len(table[0])):
            # Extrai coluna da tabela
            column = [line[column_i] for line in table]
            
            # Verifica se alguma coluna está preenchida somente com uma letra
            if verifica_linha(character, column):
                return character

        # Extrai diagonais da tabela
        diagonal_1 = [line[i] for i, line in enumerate(table)]
        diagonal_2 = [line[-i-1] for i, line in enumerate(table)]
            
        
        # Verifica se alguma diagonal está preenchida somente com uma letra
        if verifica_linha(character, diagonal_1) or verifica_linha(character, diagonal_2):
            return character

    # Retorna velha se nenhuma condição for satisfeita
    return "V"

# Feedback do professor:
# "Solução muito elegante. Parabéns!"
