# Calcula soma
# Escreva um programa que pergunta números para o usuário e, depois que o usuário digita o número 0 (zero), imprime a soma.

result = 0

is_asking = True
while is_asking:
    number = float(input("Número? "))
    
    if number == 0:
        break
    
    result += number

print(result)
