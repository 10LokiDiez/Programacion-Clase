"""
10. Desarrolle una clase `SistemaNotas` para manejar múltiples estudiantes y sus
calificaciones. Implemente métodos para calcular promedios por materia y guardar los
mejores estudiantes en un archivo.

"""

import os

class Estudiante:
    def __init__(self, id_estudiante, nombre):
        self.id_estudiante = id_estudiante
        self.nombre = nombre
        self.notas = {}

    def agregar_nota(self, materia, nota):
        if materia not in self.notas:
            self.notas[materia] = []
        self.notas[materia].append(nota)

    def obtener_promedio_general(self):
        todas_las_notas = []
        for notas_materia in self.notas.values():
            todas_las_notas.extend(notas_materia)
        
        if not todas_las_notas:
            return 0
        return sum(todas_las_notas) / len(todas_las_notas)


class SistemaNotas:
    def __init__(self):
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    def calcular_promedio_materia(self, materia):
        notas_materia = []
        for estudiante in self.estudiantes:
            if materia in estudiante.notas:
                notas_materia.extend(estudiante.notas[materia])
                
        if not notas_materia:
            return 0
        return sum(notas_materia) / len(notas_materia)

    def guardar_mejores_estudiantes(self, umbral=4.0, nombre_archivo="mejores_estudiantes.txt"):
        mejores = [est for est in self.estudiantes if est.obtener_promedio_general() >= umbral]
        path_file = os.path.join(os.path.dirname(__file__), nombre_archivo)
        with open(path_file, "w", encoding="utf-8") as archivo:
            archivo.write("ID,Nombre,Promedio General\n")
            for est in mejores:
                archivo.write(f"{est.id_estudiante},{est.nombre},{est.obtener_promedio_general():.2f}\n")

def main():
    sistema = SistemaNotas()
    
    est1 = Estudiante("001", "Laura Martinez")
    est1.agregar_nota("Matematicas", 4.5)
    est1.agregar_nota("Matematicas", 4.8)
    est1.agregar_nota("Ciencias", 4.0)
    
    est2 = Estudiante("002", "Pedro Gomez")
    est2.agregar_nota("Matematicas", 3.2)
    est2.agregar_nota("Ciencias", 3.5)
    
    est3 = Estudiante("003", "Sofia Castro")
    est3.agregar_nota("Matematicas", 5.0)
    est3.agregar_nota("Ciencias", 4.6)
    est3.agregar_nota("Historia", 4.8)
    
    sistema.agregar_estudiante(est1)
    sistema.agregar_estudiante(est2)
    sistema.agregar_estudiante(est3)
    
    promedio_mates = sistema.calcular_promedio_materia("Matematicas")
    print(f"Promedio general en Matemáticas: {promedio_mates:.2f}")
    
    sistema.guardar_mejores_estudiantes(umbral=4.2)
if __name__ == "__main__":
    main()
    