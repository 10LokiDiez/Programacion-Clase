"""
8. Cree una clase “Triangulo” donde me calcule área, perímetro y un método que me
diga que tipo de triangulo es.
"""
import math
class Triangulo:
    def __init__(self,lado1,lado2,lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        
    def perimetroTria(self):
        return self.lado1 + self.lado2 + self.lado3
    
    def tipoTria(self):
        if self.lado1 == self.lado2 == self.lado3:
            return "Equilatero"
        elif self.lado1 == self.lado2 != self.lado3 or self.lado1 != self.lado2 == self.lado3 or self.lado1 != self.lado2 == self.lado3:
            return "Isosceles"
        else:
            return "Escaleno"
    
    def areaTria(self):
        s = self.perimetroTria() / 2
        a = math.sqrt(s*(s-self.lado1)*(s-self.lado2)*(s-self.lado3))
        return a
    
    
def main():
    t1 = Triangulo(5, 5, 5)
    t2 = Triangulo(5, 5, 8)
    t3 = Triangulo(3, 4, 5)
    
    print(f"El perimetro del triangulo 1 es: {t1.perimetroTria()}")
    print(f"El perimetro del triangulo 2 es: {t2.perimetroTria()}")
    print(f"El perimetro del triangulo 3 es: {t3.perimetroTria()}")
    print(f"Es un triangulo {t1.tipoTria()}")
    print(f"Es un triangulo {t2.tipoTria()}")
    print(f"Es un triangulo {t3.tipoTria()}")
    print(f"El area del triangulo 1 es: {t1.areaTria():.2f}")
    print(f"El area del triangulo 2 es: {t2.areaTria():.2f}")
    print(f"El area del triangulo 3 es: {t3.areaTria():.2f}")
    
    
if __name__ == "__main__":
    main()