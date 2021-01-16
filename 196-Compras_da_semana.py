# Compras da semana
# Faça uma função que recebe um dicionário de receitas e uma lista de pratos que serão preparados na semana e devolve um dicionário contendo a quantidade de cada ingrediente a ser comprado. As chaves do dicionário de receitas são nomes de pratos e os valores são dicionários que, por sua vez, possui chaves que representam os nomes dos ingredientes e os valores são quantidades. Um exemplo é apresentado a seguir:
#     {
#         'Bolo de chocolate': {
#             'Leite': 0.25,
#             'Óleo': 0.25,
#             'Ovo': 2.0,
#             'Farinha': 0.5,
#             'Açúcar': 0.2,
#             'Achocolatado': 0.3
#         },
#         'Bolinho de chuva': {
#             'Óleo': 1.0,
#             'Leite': 0.3,
#             'Ovo': 3.0,
#             'Farinha': 0.6,
#             'Açúcar': 0.3
#         },
#         'Mingau': {
#             'Açúcar': 0.1,
#             'Maizena': 0.1,
#             'Leite': 0.25
#         }
#     }
# Para a lista de pratos ['Bolinho de chuva', 'Bolo de chocolate', 'Bolinho de chuva'] sua função deve retornar o seguinte dicionário (a ordem dos itens não importa):
#     {
#         'Leite': 0.85,
#         'Óleo': 2.25,
#         'Ovo': 8.0,
#         'Farinha': 1.7,
#         'Açúcar': 0.8,
#         'Achocolatado': 0.3
#     }
# O nome da sua função deve ser 'compras_da_semana'.
