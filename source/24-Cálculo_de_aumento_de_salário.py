# Cálculo de aumento de salário
# Escreva uma função que recebe o salário atual do funcionário e calcule o valor do aumento. Para salários superiores a R$1.250,00, calcule um aumento de 10%. Para inferiores ou iguais, de 15% (Adaptado do ex. 4.4 livro Nilo Ney).
# O nome da sua função deve ser calcula_aumento.

def calcula_aumento(salary):
    rise = salary
    
    if salary <= 1250:
        rise *= 15/100
    else:
        rise *= 10/100
        
    return rise
