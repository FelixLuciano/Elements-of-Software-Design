# Palavra mais frequente
# Faça uma função que recebe uma lista de palavras e retorna a palavra mais frequente. Por exemplo, para a lista
# ['abobora', 'chuchu', 'abobora', 'abobora', 'chuchu’]
# sua função deve retornar 'abobora'.
# Dica: se você não resolveu o exercício 146. Conta ocorrências de palavras, resolva-o primeiro e utilize-o como função auxiliar para este exercício (cole o código nesta solução).
# O nome da sua função deve ser 'mais_frequente'.

def mais_frequente (palavras):
    ocorrencias = {}
    
    for palavra in palavras:
        if palavra in ocorrencias:
            ocorrencias[palavra] += 1
        else:
            ocorrencias[palavra] = 1
            
    maior_ocorrencia = max(ocorrencias.values())
                           
    for palavra, ocorrencia in ocorrencias.items():
        if ocorrencia == maior_ocorrencia:
            return palavra
