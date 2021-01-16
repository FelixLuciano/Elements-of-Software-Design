# Distância entre dois pontos
# Faça uma função que recebe 4 números, x1, y1, x2, y2, e devolve a distância entre os pontos (x1,y1) e (x2,y2).
# O nome da sua função deve ser distancia_euclidiana.

import math

def distancia_euclidiana (x1, y1, x2, y2):
    delta_x = abs(x2 - x1)
    delta_y = abs(y2 - y1)
    distance = math.sqrt(delta_x**2 + delta_y**2)

    return distance
