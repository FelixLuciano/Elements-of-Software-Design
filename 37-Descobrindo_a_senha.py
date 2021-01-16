# Descobrindo a senha
# Escreva um programa que pergunta uma palavra para o usuário até que ele acerte a senha ("desisto"). Quando o usuário acertar a senha, imprima "Você acertou a senha!".

password = ""
while password != "desisto":
    password = input("Senha? ")
    
print("Você acertou a senha!")
