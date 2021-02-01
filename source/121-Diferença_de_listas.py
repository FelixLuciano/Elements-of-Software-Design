# Diferença de listas
# # Faça uma função que recebe 2 listas e retorna uma nova lista com os elementos da primeira lista que não estão na segunda lista.
# Exemplo: para a entrada lista1 = [2, 7, 3.1, 'banana'] e lista2 = [2, 'banana', 'carro'] sua função deve devolver a lista [7, 3.1].
# Atenção, esse é só um exemplo, sua função deve conseguir lidar com quaisquer listas de entrada e não apenas com as do exemplo.
# O nome da sua função deve ser subtracao_de_listas.

def subtracao_de_listas (list1, list2):
    subtracted_list = []
    
    for item1 in list1:
        has_in_list2 = False
        
        for item2 in list2:
            if item1 == item2:
                has_in_list2 = True
                
        if not has_in_list2:
            subtracted_list.append(item1)

    return subtracted_list
