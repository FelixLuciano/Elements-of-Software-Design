# Lista de números invertida
# Crie um programa que pede ao usuário que digite números inteiros positivos e armazene-os em uma lista, até que o usuário digite um número negativo ou zero. Em seguida, imprima os números digitados na ordem reversa.

list = []

while True:
    str_number = input("Number? ")
    number = int(str_number)
    
    if number <= 0:
        break
    else:
        list.append(number)

for number in reversed(list):
    print(number)
