# Junta nome e sobrenome
# Faça uma função que recebe duas listas, uma de nomes e outra com os respectivos sobrenomes, e devolve uma nova lista com os nomes e sobrenomes em uma única string. Coloque exatamente um espaço entre o nome e o sobrenome.
# O nome da sua função deve ser junta_nome_sobrenome.

def junta_nome_sobrenome (nomes, sobrenomes):
    nomes_sobrenomse = []
    
    i = 0
    while i < len(nomes):
        nome_sobrenome = nomes[i] + " " + sobrenomes[i]
        
        nomes_sobrenomse.append(nome_sobrenome)
        
        i += 1
        
    return nomes_sobrenomse
