import math
class Figura:
    def perimetro(self):
        pass
    def area(self):
        pass

class Rectangulo:
    def __init__(self,base,altura):
        self.base=base
        self.altura=altura
    def perimetro(self):
        return (self.base*2)+(self.altura*2)
    def area(self):
        return self.altura*self.base

class Triangulo:
    def __init__(self,base,altura):
        self.base=base
        self.altura=altura
    def perimetro(self):
        lado=math.sqrt((self.base**2)+(self.altura**2))
        return lado+self.base +self.altura
    def area(self):
        return self.base*self.altura/2
    
class Circulo:
    def __init__(self,radio):
        self.radio=radio
    def perimetro(self):
        return math.pi*self.radio*2
    def area(self):
        return math.pi*(self.radio**2)

figuras=[
    Rectangulo(8,5),
    Triangulo(5,7),
    Circulo(6)
]
for figura in figuras:
    print(f"{type(figura).__name__}: Area ={figura.area():.2f}, Perimetro ={figura.perimetro():.2f}")