# Empréstimo bancário
# Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar. O valor da prestação mensal não pode ser superior a 30% do salário. Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar. (Ex. 4.9 livro Nilo Ney)
# Seu programa deve imprimir somente 'Empréstimo não aprovado' ou 'Empréstimo aprovado'.

price = float(input("O valor da casa?"))
salary = float(input("Qual o salário?"))
time = float(input("quantidade de anos a pagar?"))

deferments = time * 12
deferred = price / deferments

if deferred / salary > 30/100:
    print("Empréstimo não aprovado")
else:
    print("Empréstimo aprovado")
