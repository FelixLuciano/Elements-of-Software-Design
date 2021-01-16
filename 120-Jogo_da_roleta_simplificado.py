# Jogo da roleta simplificado
# Faça um programa em Python que implementa o jogo da roleta simplificado, o usuário começa com 100 dinheiros, e o programa fica em loop até que o dinheiro acabe:
# - O programa mostra a quantidade de dinheiro disponível (obrigatório o uso de print)
# - O usuário aposta um valor (se o valor for zero o programa para)
# - Posteriormente o programa pergunta se a aposta é em um número ou paridade (par/ímpar)
#   - Se o usuário digitar a opção 'n' o usuário digita o número de 1 a 36, caso ganhe ele recebe 35 vezes o que apostou. Por exemplo, se ele tinha 100 e apostou 10 ele passará a ter 100+35⋅10=450, se ganhar, ou 100−10=90, se perder.
#   - Se o usuário digitar a opção 'p' o usuário escolhe se par (opção 'p') ou ímpar (opção 'i'), caso ganhe ele recebe o mesmo que apostou. Por exemplo, se ele tinha 100 e apostou 10 ele passará a ter 100+10=110, se ganhar, ou 100−10=90, se perder.
# - Será feito um sorteio de 0 (zero) a 36 (trinta e seis) e na sequência o pagamento das apostas
# Utilize a função random.randint.

import random

moneys = 100

def is_odd (number):
    return bool(number % 2)

while moneys > 0:
    print(moneys)
    
    bid = int(input("Aposta? "))
    bet = None

    if bid == 0:
        break
              
    bet_type = input("Número ou padrade? (n/p) ")
              
    if bet_type == "n":
        bet = int(input("Número? "))
                 
    elif bet_type == "p":
        bet = input("Par ou Ímpar? (p/i) ")
                 
    else:
        continue
                 
    match = random.randint(0, 36)
                 
    if bet_type == "n" and bet == match:
        bid *= 35
    elif bet_type == "p":
        if is_odd(match) and bet != "i" or not is_odd(match) and bet != "p":
          bid *= -1
    else:
        bid *= -1

    moneys += bid
    
print(moneys)
