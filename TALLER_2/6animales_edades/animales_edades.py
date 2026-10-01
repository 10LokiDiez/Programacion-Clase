"""
6. Animales y edades
- Crea una clase `Animal` con atributos: especie, nombre, edad.
- Genere una lista de animales.
- Implementa un método que calcule el promedio de edades.
- Guarda y lee el archivo `animales.txt` mostrando los animales que superan la edad
promedio.
"""
import os
class Animal:
    count = 0
    edades = 0
    
    def __init__(self, especie, nombre, edad):
        self.especie = especie
        self.nombre = nombre
        self.edad = edad
        Animal.count += 1
        Animal.edades += edad
        
    @classmethod
    def promedio(cls):
        return cls.edades/cls.count
        
    def guardar_animales(self, path_file):
        with open(path_file, "a") as file:
            file.write(f"{self.especie},{self.nombre},{self.edad}\n")
    
    @staticmethod
    def leer_archivo_may_prom(path_file):
        print("LISTA DE ANIMALES MAYORES DEL PROMEDIO")
        with open(path_file, "r") as file:
            text= file.read()
            for linea in text.split("\n"):
                if not linea:
                    continue
                if float((linea.split(","))[2]) > Animal.promedio():
                    print(linea)
        
        
def verificar_archivo(path_file):
    if os.path.exists(path_file):
        os.remove(path_file)
            
            
def main():
    
    path_file = os.path.join(os.path.dirname(__file__), "animales.txt")
    
    lista_animales = [
        Animal("Perro", "Lucas", 8),
        Animal("Gato", "Michi", 3),
        Animal("Loro", "Paco", 15),
        Animal("Tortuga", "Manuelita", 35),
        Animal("Hamster", "Bola de Nieve", 1),
        Animal("Conejo", "Tambor", 4)
    ]
    verificar_archivo(path_file)
    print(f"El promedio de edades de los animales es {Animal.promedio()}")
    for animal in lista_animales:
        animal.guardar_animales(path_file)
    
    Animal.leer_archivo_may_prom(path_file)
    
    
if __name__ == '__main__':
    main()       