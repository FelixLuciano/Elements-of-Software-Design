# Soma dos 100 primeiros termos
# Some os 100 primeiros termos da expressão abaixo usando while e imprima o resultado:
# 1 + \frac{1}{2} + \frac{1}{2^2} + \frac{1}{2^3} + \cdots + \frac{1}{2^{99}}

result = 0

i = 0
while i < 100:
    result += 1 / 2**i
    i += 1

print(result)
