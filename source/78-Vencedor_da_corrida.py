# Vencedor da corrida
# Faça um programa que lê os nomes e o valor da aceleração de atletas digitados pelo usuário até que o nome digitado seja 'sair' (nesse caso o usuário digita 'sair' no nome e o programa não deve perguntar a aceleração). O programa deve então usar a função do exercício 77 (repita a função na sua solução) para imprimir o nome do vencedor e o seu tempo de conclusão no formato: 'O vencedor é NOME com tempo de conclusão de TEMPO s' onde NOME é o nome do vencedor e TEMPO é o seu tempo de conclusão.

from math import sqrt

def calculate_time (athletes_accelerations):
    times = {}
    
    for athlete, aceleration in athletes_accelerations.items():
        time = sqrt(2 * 100 / aceleration)

        times[athlete] = time
        
    return times


athletes = {}

while True:
    name = input("Nome do atleta? ")
    
    if not name == "sair":
        acceleration = int(input(f"Aceleração de {name}? "))
        
        athletes[name] = acceleration
        
    else:
        break
        
athletes_times = calculate_time(athletes)

winner_time = min(athletes_times.values())

for athlete, time in athletes_times.items():
    if time <= winner_time:
        print(f"O vencedor é {athlete} com tempo de conclusão de {winner_time} s")
