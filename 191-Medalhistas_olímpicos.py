# Medalhistas olímpicos
# Nos jogos olímpicos os esportistas são organizados em uma lista de dicionários. Nesse dicionário existe os campos: nome, nacionalidade, ouro, prata, bronze. Nome e nacionalidade são strings e ouro, prata e bronze são valores numéricos inteiros com a quantidade de medalhas que o esportista ganhou.
# Faça uma função que varre essa lista de dicionários e retorna a nacionalidade que possui mais medalhas de ouro. (suponha que não pode haver empate de países com a mesma quantidade de medalhas de ouro, um país sempre terá mais medalhas)
# Por exemplo, sua função deve retornar 'Norte Americano' para a lista (atenção: este é apenas um exemplo):
#     [{
#         'nome': ' Michael Phelps',
#         'nacionalidade': 'Norte Americano',
#         'ouro': 23, 'prata': 3, 'bronze': 2,
#     },
#     {
#         'nome': 'Larisa Latynina',
#         'nacionalidade': 'Russo',
#         'ouro': 9, 'prata': 5, 'bronze': 4,
#     },
#     {
#         'nome': 'Nikolai Andrianov',
#         'nacionalidade': 'Russo',
#         'ouro': 7, 'prata': 5, 'bronze': 3,
#     },
#     {
#         'nome': 'Boris Shakhlin',
#         'nacionalidade': 'Russo',
#         'ouro': 7, 'prata': 4, 'bronze': 2,
#     },
#     {
#         'nome': 'Jenny Thompson',
#         'nacionalidade': 'Norte Americano',
#         'ouro': 8, 'prata': 3, 'bronze': 1,
#     }]
# O nome da sua função deve ser 'mais_medalhas'.
