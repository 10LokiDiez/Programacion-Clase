"""
Cree una clase llamada Vector2D con:
- x
- y

Implemente el método __add__ para que al sumar dos vectores se obtenga un nuevo vector.
Ejemplo: (2,3) + (4,1) = (6,4).
"""

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"x: {self.x} y:{self.y}"
p1 = Vector2D(2,3)
p2 = Vector2D(4,1)

print(p1+p2)