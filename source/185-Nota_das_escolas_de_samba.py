# Nota das escolas de samba
# Você foi contratado para implementar o sistema de apuração das notas do Carnaval de São Paulo.
# Neste ano existem 9 quesitos a serem avaliados e cada quesito conta com 4 avaliações.
# Dentre as 4 notas de cada quesito, a nota de menor valor é eliminada.
# A nota final da escola de samba é a soma simples de todas as notas que não foram eliminadas.
# Calcule a nota individual de cada escola através de uma função que receba uma lista que conterá outras 9 listas com as 4 avaliações.
# por exemplo:
# tom_maior = [[9.9, 9.9, 10, 9.9], [10, 9.9, 9.8, 10], [10, 10, 10, 10], [10, 10, 10, 10], [10, 9.9, 9.9, 10], [9.9, 10, 10, 10], [10, 10, 9.9, 9.9], [0.0, 9.9, 10, 9.9], [10, 9.8, 10, 10]]
# A nota da escola Tom Maior é: 269.3
# O nome da sua função deve ser 'calcula_escola'.

def calcula_escola (issues):
    final_score = 0

    for points in issues:
        score = 0

        for point in points:
            score += point

        score -= min(points)
        final_score += score

    return final_score
