# Redução no tempo de vida de um fumante
# Escreva um programa que calcule a redução de tempo de vida de um fumante a partir do número de cigarros. Pergunte quantos cigarros ele fuma por dia e há quantos anos fuma. Imprima o tempo de vida perdido em dias. Considere que um cigarro rouba 10 minutos de expectativa de vida.

cigarrette = int(input("Quantos cigarros você fuma por dia?"))
time = int(input("Há quantos anos você fuma?"))

time_per_cigarrette = 10 / 60 / 24  # 10 minutes in days
days_in_year = 365

lost_time = cigarrette * time * days_in_year * time_per_cigarrette

print(lost_time)
