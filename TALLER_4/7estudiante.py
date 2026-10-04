"""
Cree una clase llamada Estudiante con:
- nombre
- codigo

Implemente el método __eq__ para que dos estudiantes sean iguales si tienen el mismo
código.
Pruebe comparando varios objetos con ==.

"""

class Estudiante:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo
        
    def __eq__(self, other):
        return self.codigo == other.codigo
        
es1 = Estudiante("Simon", 1089933667)
es2 = Estudiante("Juan", 1089933667)

if es1 == es2:
    print("Los codigos de los estudiantes son iguales")
else:
    print("No son iguales")
