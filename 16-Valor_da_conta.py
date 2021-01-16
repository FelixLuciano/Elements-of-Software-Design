# Valor da conta
# Escreva um programa que pergunta para o usuário o valor da conta do restaurante e imprime: "Valor da conta com 10%: R$ X.YZ", onde X.YZ é um número com exatamente duas casas decimais.

valor = float(input('Qual o valor da conta?'))
gorjeta = valor * 10/100 # 10% do valor

valor += gorjeta

print('Valor da conta com 10%: R$ {0:.2f}'.format(valor))
