# Capitaliza string
# Escreva uma função que recebe uma string e devolve a versão capitalizada dessa string, ou seja, devolve a mesma string com a primeira letra maiúscula.
# Observação: você não pode usar a função capitalize() do Python.
# Dica: use o upper() e fatiamento.
# O nome da sua função deve ser 'capitaliza'.

def capitaliza (text):
    capitalized = text[0].upper()
    capitalized += text[1:]
    
    return capitalized
