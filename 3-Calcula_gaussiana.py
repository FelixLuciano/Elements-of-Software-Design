# Calcula gaussiana
# Faça uma função que recebe 3 números reais como argumento: x, μ (mi) e σ (sigma). Essa função deve retornar o valor da seguinte fórmula:
# f(x, \mu, \sigma) = \frac{1}{\sigma\sqrt{2\pi}}e^{(-0,5(\frac{x-\mu}{\sigma})^2)}
# O nome da sua função deve ser calcula_gaussiana.

import math

def calcula_gaussiana (x, mi, sig):
    a = 1 / (sig * math.sqrt(2 * math.pi))
    b = math.e ** (((x - mi) / sig) ** 2 / -2 )
    
    return a * b
