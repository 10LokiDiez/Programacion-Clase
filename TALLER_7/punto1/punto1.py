"""
1. Realice un programa para calcular diferentes áreas al menos 4 áreas de
figuras trigonométricas haciendo uso de clases y herencia se puede realizar
el modelamiento, deben encapsular todos los atributos y métodos, cuando
diseñen el set de cada atributo deben tener en cuenta dentro de este
método set que solo se deben ingresar números positivos.
"""
from math import pi

class Figuras:
    
    def area(self):
        print("Aqui se va a calcular el area de las figuras")
        
class Circulo(Figuras):
    __radio = 25
    
    def get_radio(self):
        return self.__radio
    
    def set_radio(self, new_radio):
        if new_radio > 0:
            self.__radio =  new_radio
    
    def area(self):
        print(f"El area de tu circulo es: {self.__radio **2 *pi}")
        
class Triangulo(Figuras):
    __base = 10
    __altura = 25
    
    def get_base(self):
        return self.__base
    
    def set_base(self, new_base):
        if new_base > 0:
            self.__base =  new_base
            
    def get_altura(self):
        return self.__altura
    
    def set_altura(self, new_altura):
        if new_altura > 0:
            self.__altura =  new_altura
    
    def area(self):
        print(f"El area de tu triangulo es: {(self.__base * self.__altura)/2}")
        
        
class Cuadrado(Figuras):
    __lado = 25
    
    def get_lado(self):
        return self.__lado
    
    def set_lado(self, new_lado):
        if new_lado > 0:
            self.__lado =  new_lado
    
    def area(self):
        print(f"El area de tu cuadrado es: {self.__lado **2}")
        
        
class Rectangulo(Figuras):
    __lado1 = 25
    __lado2 = 30
    
    def get_lado1(self):
        return self.__lado1
    
    def set_lado1(self, new_lado1):
        if new_lado1 > 0:
            self.__lado1 =  new_lado1
            
    def get_lado2(self):
        return self.__lado2
    
    def set_lado2(self, new_lado2):
        if new_lado2 > 0:
            self.__lado2 =  new_lado2
    
    def area(self):
        print(f"El area de tu rectangulo es: {self.__lado1 * self.__lado2}")
        
        
def main():
    # Prueba Circulo
    mi_circulo = Circulo()
    mi_circulo.set_radio(10)
    mi_circulo.area()

    # Prueba Triangulo
    mi_triangulo = Triangulo()
    mi_triangulo.set_base(5)
    mi_triangulo.set_altura(8)
    mi_triangulo.area()

    # Prueba Rectangulo
    mi_rectangulo = Rectangulo()
    mi_rectangulo.set_lado1(4)
    mi_rectangulo.set_lado2(6)
    mi_rectangulo.area()
    
    # Prueba de validación (intentar poner un número negativo)
    mi_cuadrado = Cuadrado()
    mi_cuadrado.set_lado(-5) # Esto no debería cambiar el valor por defecto (25) porque es negativo
    mi_cuadrado.area()
    
main()