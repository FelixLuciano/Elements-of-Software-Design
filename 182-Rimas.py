# Rimas
# Você está desenvolvendo um sistema de classificação de poemas. Na etapa atual do desenvolvimento é necessário classificar o tipo de rimas em uma estrofe. Utilizaremos 4 tipos de rimas: alternada, interpolada, emparelhada e outra. As rimas dependem apenas da última sílaba de cada verso. Veja a seguir alguns exemplos (as letras no final de cada linha representam uma sílaba e não fazem parte):
# - Rima alternada (ABAB):
#     “Cheguei, chegaste. Vinhas fatigada A
#     E triste, e triste e fatigado eu vinha; B
#     Tinhas a alma de sonhos povoada A
#     E a alma de sonhos povoada eu tinha.” B
#     -- Olavo Bilac
# - Rima interpolada (ABBA):
#     “Para canto de amor tenros cuidados. A
#     Tomo entre voz, ó montes, o instrumento; B
#     Ouvi pois o meu fúnebre lamento; B
#     Se é que compaixão dos animados.” A
#     -- Cláudio Manuel da Costa
# - Rima emparelhada (AABB):
#     “Manhã de junho ardente. Uma encosta escavada A
#     seca, deserta e nua, à beira de uma estrada A
#     Terra ingrata, onde a urze a custo desabrocha B
#     bebendo o sol, comendo o pé, mordendo a rocha.” B
#     -- Guerra Junqueiro
# Se uma rima não pertencer a nenhuma das categorias acima ela é classificada como "outra". Faça uma função que recebe 4 sílabas (a última de cada verso) e devolve a classificação da rima. Utilizando os exemplos acima, teríamos:
# - A chamada classifica_rima("ada", "inha", "ada", "inha") deve devolver "alternada"
# - A chamada classifica_rima("ados", "mento", "mento", "ados") deve devolver "interpolada"
# - A chamada classifica_rima("ada", "ada", "rocha", "rocha") deve devolver "emparelhada"
# - A chamada classifica_rima("ados", "mento", "mento", "inha ") deve devolver "outra"
# - A chamada classifica_rima("ada", "ada", "ada", "ada") deve devolver "outra"
# O nome da sua função deve ser 'classifica_rima'.

def classifica_rima (*rima):
    if rima[0] == rima[2] and rima[1] == rima[3] and not rima[0] == rima[1]:
        return "alternada"
    elif rima[0] == rima[1] and rima[2] == rima[3] and not rima[0] == rima[2]:
        return "emparelhada"
    elif rima[0] == rima[3] and rima[1] == rima[2] and not rima[0] == rima[1]:
        return "interpolada"
    else:
        return "outra"

# Feedback do professor:
# "Não precisava receber como *args. Como o código sempre assume que são exatamente 4 argumentos, os erros seriam mais claros se fossem recebidos 4 argumentos explicitamente."
