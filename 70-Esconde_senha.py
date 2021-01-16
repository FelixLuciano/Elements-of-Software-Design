# Esconde senha
# Faça uma função que recebe uma senha (string) e devolve uma string do mesmo tamanho da senha formada somente por asteriscos ('*').
# O nome da sua função deve ser esconde_senha.

def esconde_senha (password):
    length = len(password)
    hidden = "*" * length
    
    return hidden
