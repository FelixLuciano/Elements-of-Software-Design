# Custo do churrasco
# Um grupo de amigos gosta de fazer churrasco no final de semana e registra os custos do churrasco em um arquivo CSV onde cada linha contém o nome de um item de despesa, a quantidade consumida deste item e o seu custo unitário. Por exemplo, o arquivo texto poderia conter o seguinte conteúdo:
# - Carvão,2,9.90
# - Refrigerante,3,8.35
# - Picanha,2,69.80
# - Linguiça,2,15.98
# - Coxinha da Asa,2,12.39
# - Contra Filé,3,25.98
# Neste exemplo foram consumidos 2 sacos de carvão a R$9,90 cada, 3 garrafas de refrigerante a R$8,35 cada, e assim por diante. Faça um programa que lê um arquivo chamado churras.txt, não necessariamente igual ao exemplo acima, e imprime o valor total dos custos do churrasco.

total = 0

with open("churras.txt") as file:
    content = file.readlines()
    
    for line in content:
        item, quantity, price = line.split(",")
        item_total = int(quantity) * float(price)

        total += item_total

print(total)

