# Calcula ângulo de refração
# A lei de Snell-Descartes define que a relação entre o ângulo de incidência e o ângulo de refração de um raio de luz atravessando de um meio para o outro é inversamente proporcional a razão dos índices de refração dos meios, que é dado pela seguinte fórmula:
# \frac{n_1}{n_2} = \frac{sen(\theta_2)}{sen(\theta_1)}
# Faça uma função que recebe os valores de n_1, n_2 e θ_1 e retorna o valor do θ_2. Os valores passados de n_1, n_2 são adimensionais, já os valores de θ1 e θ2 deverão ser recebidos e retornados em graus.
# O nome da sua função deve ser 'snell_descartes'.

import math

def snell_descartes (n1, n2, tetta1):
    sin_tetta1 = math.sin(math.radians(tetta1))
    sin_tetta2 = n1 / n2 * sin_tetta1
    
    return math.degrees(math.asin(sin_tetta2))

