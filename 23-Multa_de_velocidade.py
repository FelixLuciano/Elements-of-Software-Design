# Multa de velocidade
# Escreva um programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse 80km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso exiba a multa, cobrando R$5,00 por km acima de 80. (Ex. 4.2 livro Nilo Ney).
# A multa deve ser apresentada com exatamente duas casas decimais. Se o usuário não foi multado, imprima: 'Não foi multado'.

speed = float(input("Velocidade do carro em kilometros?"))

if speed > 80:
    charge = (speed - 80) * 5.00
    print("{0:.2f}".format(charge))
else:
    print("Não foi multado")
