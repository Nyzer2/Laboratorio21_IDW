from geometria import Rectangulo, Circulo, Triangulo
figuras=[
    Rectangulo(8,5),
    Triangulo(5,7),
    Circulo(6)
]
for figura in figuras:
    print(f"{type(figura).__name__}: Area ={figura.area():.2f}, Perimetro ={figura.perimetro():.2f}")