# Classificador de triângulos
# Faça uma função que recebe os lados de um triângulo e retorna se ele é equilátero, isósceles ou escaleno. Sua função deve retornar a string "equilátero", "isósceles", ou "escaleno". Assuma que os lados do triângulo são válidos.
# O nome da sua função deve ser classifica_triangulo.

def classifica_triangulo (a, b, c):
    if a == b and b == c:
        return "equilátero"
    elif a == b or a == c or b == c:
        return "isósceles"
    else:
        return "escaleno"
