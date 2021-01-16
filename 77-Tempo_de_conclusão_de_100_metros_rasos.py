# Tempo de conclusão de 100 metros rasos
# Faça uma função que recebe um dicionário de atletas em uma corrida de 100 metros rasos e devolve um dicionário cujas chaves são os nomes dos atletas e os valores são os respectivos tempos de conclusão da prova. As chaves do dicionário de atletas são strings e os valores são a sua aceleração. Dica: assuma movimento retilíneo uniformemente variado com velocidade inicial 0.
# O nome da sua função deve ser 'calcula_tempo'.

from math import sqrt

def calcula_tempo (acelerations):
    times = {}
    
    for athlete, aceleration in acelerations.items():
        time = sqrt(2 * 100 / aceleration)

        times[athlete] = time
        
    return times
