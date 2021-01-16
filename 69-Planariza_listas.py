# Planariza listas
# Faça uma função que recebe uma lista de listas e devolve uma lista simples composta por todos os elementos das listas originais.
# Exemplo: [[1, 2, 3], [4, 5, 6], [7, 8], [9], [10]] deve devolver [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
# O nome da sua função deve ser junta_listas.

def junta_listas (list_of_list):
    new_list = [item for inner_list in list_of_list for item in inner_list]
    
    return new_list
