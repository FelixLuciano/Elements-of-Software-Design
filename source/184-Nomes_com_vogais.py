# Nomes com vogais
# Dada uma lista de nomes, conte quantos nomes começam com as vogais (A, E, I, O , U) e quantos nomes começam por outras letras. Crie uma função que retorne uma lista sendo que o primeiro elemento dela é o número de nomes que começam com vogais e o segundo por qualquer outra letra. Suponha que os nomes sempre começam com letras maiúsculas.
# Por exemplo para: ["André", "Carlos", "João", "Otavio", "Thiago"]
# A resposta deveria ser: [2, 3]
# O nome da sua função deve ser 'nomes_com_vogais'.

def nomes_com_vogais (names):
    count = [ 0, 0 ]

    for name in names:
        first_letter = name[0]

        if first_letter in ("A", "E", "I", "O", "U"):
            count[0] += 1
        else:
            count[1] += 1

    return count
