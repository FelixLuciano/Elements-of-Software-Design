# Ponto contido no círculo
# Crie uma classe chamada Circulo que tem na construção (no init ) um ponto como centro e um float como raio. Adicione um método contem(self, ponto) que avalia se um ponto está dentro da área do círculo ou não.
# Pontos são representados por objetos da classe Ponto, especificada a seguir. Você não precisa implementar a classe Ponto.
# class Ponto:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

from math import hypot

class Circulo:
    def __init__ (self, origin, radius):
        self.origin = origin
        self.radius = radius
        
    def distancia (self, point):
        width = point.x - self.origin.x
        height = point.y - self.origin.y
        distance = hypot(width, height)
                         
        return distance
    
    def contem (self, point):
        return self.distancia(point) <= self.radius
