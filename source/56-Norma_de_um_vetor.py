# Norma de um vetor
# Escreva uma função que recebe um vetor de dimensão arbitrária representado por uma lista e devolve a sua norma. Caso seja necessário, pesquise por norma ou módulo de um vetor no Google ;)
# O nome da sua função deve ser 'calcula_norma'.

from math import sqrt

def calcula_norma (vetores):
    soma = 0
    
    for vetor in vetores:
        soma += vetor ** 2
        
    return sqrt(soma)
