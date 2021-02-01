# Celsius para Fahrenheit
# Faça uma função que converte temperaturas em Celsius para Fahrenheit.
# O nome da sua função deve ser celsius_para_fahrenheit.

def transform_scale (x_0, y_0, x_1, y_1):
  delta_x = x_1 - x_0
  delta_y = y_1 - y_0
  m = delta_y / delta_x

  return lambda x: m * (x - x_0) + y_0


celsius_para_fahrenheit = transform_scale(0, 32, 100, 212)
