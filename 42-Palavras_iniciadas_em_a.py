# Palavras iniciadas em "a"
# Crie um programa que pergunte palavras ao usuário e preencha uma lista. O programa deve parar com a palavra "fim". Ao final, imprima somente as palavras em que a primeira letra seja "a". Use um print por palavra.
# Dica: você pode acessar um único caractere de uma string da mesma maneira que acessamos um elemento de uma lista. Por exemplo:
# palavra = 'banana'
# primeira_letra = palavra[0]
# quinta_letra = palavra[4]
# print(palavra)
# print(primeira_letra)
# print(quinta_letra)
# O programa acima vai imprimir:
# banana
# b
# n

words = []

while True:
    word = input("Palavra?")
    
    if word == "fim":
        break
    else:
        words.append(word)

for word in words:
    if word[0] == "a":
        print(word)
