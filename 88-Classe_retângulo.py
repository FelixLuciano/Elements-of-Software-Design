# Classe retângulo
# Crie uma classe Retangulo, com um construtor (__init__) que recebe dois pontos e os armazena como atributos:
# - Ponto do canto inferior esquerdo
# - Ponto do canto superior direito
# Cada ponto é um objeto do tipo Ponto, como definido à seguir:
# class Ponto:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
# Assuma que a classe Ponto já está definida, você só precisa implementar a classe Retangulo.
# Sua classe Retangulo deve possuir dois métodos sem argumentos adicionais (lembre-se que métodos sempre recebem self):
# 1. calcula_perimetro(self): calcula o perímetro do retângulo;
# 2. calcula_area(self): calcula a área do retângulo.

class Retangulo:
    def __init__ (self, point_1, point_2):
        self.x1 = point_1.x
        self.y1 = point_1.y
        self.x2 = point_2.x
        self.y2 = point_2.y
        
    def calcula_perimetro (self):
        return 2 * self.width + 2 * self.height
    
    def calcula_area (self):
        return self.width * self.height
        
    @property
    def width (self):
        return self.x2 - self.x1
        
    @property
    def height (self):
        return self.y2 - self.y1
