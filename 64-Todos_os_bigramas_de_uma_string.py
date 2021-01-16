# Todos os bigramas de uma string
# Escreva uma função que recebe uma string e devolve uma lista com todos os seus bigramas. Um bigrama é qualquer sequência de dois caracteres. Ex: para a string 'babador' a sua função deve devolver a lista ['ba', 'ab', 'ad', 'do', 'or']. Note que cada bigrama deve aparecer somente uma vez na lista.
# Curiosidade: bigramas são usados em sistemas de entrada de texto (teclados) para predizer a próxima letra mais provável.
# O nome da sua função deve ser 'acha_bigramas'.

def acha_bigramas (text):
    bigrams = []
    
    for i in range(len(text[:-1])):
        bigram = text[i:i+2]
        
        if not bigram in bigrams:
            bigrams.append(bigram)
        
    return bigrams
