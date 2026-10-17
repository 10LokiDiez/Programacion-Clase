"""
3. Define una clase base Figura con un método area().
Implementa subclases Rectangulo, Triangulo y Circulo que sobrescriban el método
area() con la fórmula correspondiente.
Crea objetos de cada clase y guarda sus áreas en una lista. Luego recórrela
mostrando qué tipo de figura es y cuánto mide su área.
"""
from math import pi
class Figura:
    def area(self):
        pass
    
class Rectangulo(Figura):
    def __init__(self, lado1, lado2):
        self.lado1 = lado1
        self.lado2 = lado2
        
    def area(self):
        return self.lado1 * self.lado2
    
class Triangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
    def area(self):
        return (self.base/2) * self.altura
    
class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
        
    def area(self):
        return self.radio **2 * pi

def main():
    triangulo1 = Triangulo(4,2)
    triangulo2 = Triangulo(8,4)
    triangulo3 = Triangulo(3,3)
    rectangulo1 = Rectangulo(4,2)
    rectangulo2 = Rectangulo(8,4)
    rectangulo3 = Rectangulo(3,3)
    circulo1 = Circulo(5)
    circulo2 = Circulo(15)
    circulo3 = Circulo(50)
    
    figuras = [triangulo1,triangulo2,triangulo3,rectangulo1,rectangulo2,rectangulo3,circulo1,circulo2,circulo3]
    
    area = []
    
    for figura in figuras:
        area.append(figura.area())
        
    print("IMPRIMIR AREAS CON FIGURA")
    i = 0
    for figura in figuras:
        print(figura.__class__.__name__, area[i])
        i += 1
    

    
if __name__ =="__main__":
    main()