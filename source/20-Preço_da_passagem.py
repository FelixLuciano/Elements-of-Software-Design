# Preço da passagem
# Escreva um programa que pergunta a distância que um passageiro deseja percorrer em km. Seu programa deve imprimir o preço da passagem, cobrando R$0.50 por km para viagens de até 200km e R$0.45 por quilômetro extra para viagens mais longas. (Adaptado do ex. 4.6 livro Nilo Ney).
# O resultado deve ser impresso com exatamente duas casas decimais.

distance = float(input("Qual a distância, em quilometros, da sua viagem?"))
price = distance

if distance <= 200:
    price *= 0.50
else:
    price = (price - 200) * 0.45 + 200 * 0.50

print("{0:.2f}".format(price))
