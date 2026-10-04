"""
Cree una clase llamada Curso con:
- nombre_curso
- estudiantes (lista de objetos Estudiante)

Implemente:
- __len__ → cantidad de estudiantes
- __str__ → mostrar lista de estudiantes
- __eq__ → dos cursos son iguales si 
           tienen el mismo número de estudiantes.

Pruebe:
len(curso1)
print(curso1)
curso1 == curso2
"""

class Curso:
    def __init__(self, nombre_curso, estudiantes):
        self.nombre_curso = nombre_curso
        self.estudiantes = estudiantes

    def __len__(self):
        return len(self.estudiantes)
    
    def __str__(self):
        cadena = ""
        for estudiante in self.estudiantes:
            cadena = cadena + estudiante + " "
        return cadena
    
    def __eq__(self, otro):
        return len(self.estudiantes) == len(otro.estudiantes)
    
curso1 = Curso("PrimeroA", ["Juan","Pereira","Simon","Juanita"])
curso2 = Curso("PrimeroB", ["Martin","Samuel","Jose","Santiago"])

print(len(curso1))
print(curso1)
print(curso1 == curso2)
