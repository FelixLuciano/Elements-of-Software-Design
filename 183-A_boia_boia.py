# A boia boia?
# Você foi contratado para uma fábrica de boias de piscina.
# As boias fabricadas têm sempre o formato de um toróide (torus), que é definido pelo raio interno da boia (R) e o raio da seção transversal dela (r). As boias possuem um peso (P) medido por uma balança.
# Sua função é descobrir se a boia vai "boiar" ou não. Considere que a densidade da água para a temperatura ambiente de 997 kg/m³ ou 0,997 g/cm³ e qualquer coisa com densidade menor ou igual a esse valor irá boiar. Lembre-se que a densidade é calculada como o peso dividido pelo volume.
# Para calcular o volume de um toróide (torus) use a seguinte equação:
# 2{\pi^2}R{r^2}
# Crie uma função que receba o peso da boia (P), o raio interno da boia (R) e o raio da seção transversal (r). Os valores do peso (P) serão dados em Kg e os valores dos raios (R) e (r) em centímetros. Se a boia boiar a função deverá retornar True, caso contrário deverá retornar False.
# O nome da sua função deve ser 'will_it_float'.

import math

water_density = 0.997 # in g/m³

def will_it_float (weight, radius_R, radius_r):
    weight_in_grams = weight * 1000
    volume = 2 * math.pi**2 * radius_R * radius_r**2
    density = weight_in_grams / volume

    if density > water_density:
        return False
    else:
        return True
