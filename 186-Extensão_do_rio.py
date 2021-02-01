# Extensão do rio
# Sua empresa foi contratada para desenvolver um software de cálculo da extensão de rios a partir de imagens de satélite. Faça uma função que recebe as coordenadas de um rio, como mostrado no exemplo a seguir, e devolve a sua extensão.
#Para calcular a extensão do rio devemos encontrar a distância entre os pontos. A distância entre dois pontos (x_1,y_1) e (x_2,y_2) é dada por:
# \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}
# Sua função receberá duas listas, uma com os valores de x e outra com os valores de y, ambas com a mesma quantidade de elementos. No exemplo acima, seriam as seguintes listas:
# - Coordenadas x: [275, 290, 310, 390, 480]
# - Coordenadas y: [75, 180, 120, 110, 150]
# Ainda nesse exemplo, o resultado esperado seria aproximadamente 348,42, pois:
# \sqrt{(290-275)^2 + (180-75)^2} + \sqrt{(310-290)^2 + (120-180)^2}+\sqrt{(390-310)^2 + (110-120)^2}+\sqrt{(480-390)^2 + (150-110)^2} = 348,42\dots
# O nome da sua função deve ser 'calcula_extensao'.

import math

def calcula_extensao (x_list, y_list):
    length = 0

    i = 0
    points = min(len(x_list), len(y_list))

    for i in range(0, points - 1):
        x1 = x_list[i]
        x2 = x_list[i + 1]
        y1 = y_list[i]
        y2 = y_list[i + 1]

        base = x2 - x1
        height = y2 - y1
        distance = math.hypot(base, height)

        length += distance

    return length
