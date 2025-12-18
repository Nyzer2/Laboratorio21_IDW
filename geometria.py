import math
class Figura:
    def perimetro(self):
        pass
    def area(self):
        pass
class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def perimetro(self):
        return (self.base * 2) + (self.altura * 2)
    def area(self):
        return self.altura * self.base
class Triangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def perimetro(self):
        lado = math.sqrt((self.base ** 2) + (self.altura ** 2))
        return lado + self.base + self.altura
    def area(self):
        return self.base * self.altura / 2
class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    def perimetro(self):
        return math.pi * self.radio * 2
    def area(self):
        return math.pi * (self.radio ** 2)