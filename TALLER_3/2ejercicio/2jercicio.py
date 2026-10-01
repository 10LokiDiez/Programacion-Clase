"""
2. Diseñe una clase `Estudiante` con atributos como nombre, código, carrera, edad y
promedio. Implemente métodos para calcular si el estudiante aprueba (promedio >=
3.0), y guardar los datos en un archivo.
"""
import os
class Estudiante:
    def __init__(self, nombre, codigo, carrera, edad, promedio):
        self.nombre = nombre
        self.codigo = codigo
        self.carrera = carrera
        self.edad = edad
        self.promedio = promedio
        
    def __str__(self):
        return f"{self.nombre} con codigo: {self.codigo}, estudiando {self.carrera}, cuenta con una edad de {self.edad}, promedio {self.promedio}. Estado:{self.aprobo()}"
        
    def aprobo(self):
        if self.promedio >= 3:
            return "Aprobado"
        else:
            return "Reprobado"

    def guardar_datos(self, path):
        with open(path, "a", encoding="utf-8") as file:
            file.write(str(self) + "\n")
        
        
def main():
    path_file = os.path.join(os.path.dirname(__file__), "archivo_de_estudiantes.txt")
    
    open(path_file, "w").close()
    
    estudiante1 = Estudiante("Ana Gómez", "101", "Ingeniería de Sistemas", 20, 4.5)
    estudiante2 = Estudiante("Carlos Ruiz", "102", "Derecho", 22, 2.8)
    estudiante3 = Estudiante("María López", "103", "Medicina", 21, 3.8)
    estudiante4 = Estudiante("Juan Pérez", "104", "Administración", 23, 2.9)
    estudiante5 = Estudiante("Sofía Castro", "105", "Arquitectura", 19, 4.2)
    estudiantes = [estudiante1, estudiante2, estudiante3, estudiante4, estudiante5]
    for estudiante in estudiantes:
        estudiante.guardar_datos(path_file)
        
if __name__ == "__main__":
    main()