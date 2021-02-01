# Movimento retilíneo uniforme
# Faça uma função que calcule a posição de um objeto em movimento retilíneo uniforme em um instante t, com posição inicial s0 e velocidade v:
# s = f(t, s_0, v) = s_0 + vt
# O nome da sua função deve ser calcula_posicao.

def calcula_posicao (time, space_0, speed):
    space = space_0 + speed * time
    return space
