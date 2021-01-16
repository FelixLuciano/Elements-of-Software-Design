# Jogo de aventura
# Em um jogo de aventura, o dano causado por um personagem é igual à sua força total. A força total é a soma da força do personagem com os adicionais de força dos equipamentos. Um personagem é representado por um dicionário como o mostrado a seguir (ATENÇÃO: este é apenas um exemplo):
#     {
#         'nome': 'Herói',
#         'força': 4,
#         'vida': 25,
#         'equipamentos': [
#             {
#                 'nome': 'Martelo Mortal',
#                 'força': 15, 
#             },
#             {
#                 'nome': 'Luva Leve',
#                 'força': 2, 
#             },
#         ],
#     }
# Neste exemplo, o dano causado pelo personagem seria 4+15+2=21. Considere outro exemplo:
#     {
#         'nome': 'Outro Herói',
#         'força': 18,
#         'vida': 42,
#         'equipamentos': [],
#     }
# Neste caso, o dano causado pelo personagem seria 18, pois a lista de equipamentos está vazia. Faça uma função que recebe um dicionário representando os atributos de um personagem e retorna o dano causado por ele.
# O nome da sua função deve ser calcula_dano.