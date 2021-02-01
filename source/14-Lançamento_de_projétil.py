# Lançamento de projétil
# Faça uma função que calcule a distância alcançada por um projétil lançado com velocidade v em um ângulo θ, de uma altura y0. A distância é dada pela fórmula:
# d = \frac{v^2}{2g}\left(1 + \sqrt{1 + \frac{2gy_0}{v^2(\sin(\theta))^2}}\right)\sin(2\theta)
# Use g=9.8.
# O nome da sua função deve ser calcula_distancia_do_projetil.

import math


gravity = 9.8

def calcula_distancia_do_projetil (speed, phi, height):
    energy = speed**2 / gravity / 2
    sin_phi_squared = math.sin(phi)**2
    sin_2phi = math.sin(phi * 2)
    crazy = math.sqrt(gravity * height / speed**2 / sin_phi_squared * 2 + 1) + 1
    
    distance = energy * crazy * sin_2phi
    return distance

