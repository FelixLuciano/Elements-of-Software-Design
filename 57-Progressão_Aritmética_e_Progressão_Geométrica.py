# Progressão Aritmética e Progressão Geométrica
# Escreva uma função que recebe uma lista de números e devolve "PA", se ela for uma progressão aritmética, "PG", se for uma progressão geométrica, e "NA" se não for nenhuma das duas. Caso a sequência seja tanto uma PA quanto uma PG, devolva "AG".
# O nome da sua função deve ser 'verifica_progressao'.

def verifica_PA (progressao):
    for i, a1 in enumerate(progressao[:-2]):
        a2 = progressao[i + 1]
        a3 = progressao[i + 2]

        K = a2 - a1
        an = a2 + K

        if not an == a3:
            return False

    return True

def verifica_PG (progressao):
    for i, a1 in enumerate(progressao[:-2]):
        a2 = progressao[i + 1]
        a3 = progressao[i + 2]

        if a1 == 0 or a2 == 0:
          return False

        q = a2 / a1
        an = a2 * q

        if not an == a3:
          return False

    return True

def verifica_progressao (progressao):
    is_PA = verifica_PA(progressao)
    is_PG = verifica_PG(progressao)
          
    if is_PA and is_PG:
        return "AG"
    elif is_PA:
        return "PA"
    elif is_PG:
        return "PG"
    else:
        return "NA"
