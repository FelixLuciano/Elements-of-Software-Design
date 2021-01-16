# Mês para número
# Crie um programa que pergunta o nome do mês e imprime o número do mês (use os nomes dos meses com letra minúscula).

month = input("month? ")

months = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro", ]

num = months.index(month) + 1

print(num)
