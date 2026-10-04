"""
Cree una clase llamada Persona con los atributos:
- nombre
- edad
Implemente el método __str__ para que al imprimir el objeto se muestre:
Nombre: Carlos - Edad: 25
Luego cree 3 objetos y muéstrelos usando print().

"""
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def __str__(self):
        return f"Nombre: {self.nombre} - Edad: {self.edad}"
    
    
def main():
    persona1 = Persona("Carlos", 25)
    persona2 = Persona("Simon", 20)
    persona3 = Persona("Juanita", 23)
    
    print(persona1)
    print(persona2)
    print(persona3)
    
if __name__ == "__main__":
    main()