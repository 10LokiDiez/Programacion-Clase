#voy a utilizar esta libreria para el uso de fechas y ser exato en las fechas de creacion
from datetime import datetime
import os
"""
a. Para cada clase debe diseñar al menos 6 atributos.
c. Debe de crear un método para calcular la antigüedad de todas las
entidades en el diseño.
d. Dependiendo de cada tipo de profesor debe diseñar al menos tres
materias acordes con el rango de cada uno y se deben visualizar en
pantalla por medio de un método.
e. Guarde la información que crea necesaria en un archivo para este
programa.
"""


class PersonalUniversitario:
    def __init__(self, cedula, nombre, apellido, correo, fecha_nacimiento, direccion, fecha_registro = None):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.fecha_nacimiento = fecha_nacimiento
        self.direccion = direccion
        if fecha_registro is None:
            self.fecha_registro = datetime.now()
        else:
            self.fecha_registro = fecha_registro
        
    """
    c. Debe de crear un método para calcular la antigüedad de todas las
    entidades en el diseño.
    """    
    def antiguedad(self):
        hoy = datetime.now()
        diff = hoy - self.fecha_registro
        
        return f"Dias: {diff.days}"
        

class Profesor(PersonalUniversitario):
    def __init__(self, cedula, nombre, apellido, correo, fecha_nacimiento, direccion,
                 codDocente, facultad, salario, tipo, horas_trabajadas, oficina):
        #No se puede usar super() porque hay herencia multiple, por lo que se debe llamar a los constructores de las clases padre de manera explicita
        PersonalUniversitario.__init__(self, cedula, nombre, apellido, correo, fecha_nacimiento, direccion)
        self.codDocente = codDocente
        self.facultad = facultad
        self.salario = salario
        self.tipo = tipo
        self.horas_trabajadas = horas_trabajadas
        self.oficina = oficina
    """
    b. Para las clases profesor debe realizar un método en donde se pueda
    calcular el sueldo mensual dependiendo de las horas que trabaja y del
    tipo de profesor que sea
    """
    
    def calcular_sueldo_mensual(self) :
        tipo_profesor = self.tipo.lower().strip()
        if tipo_profesor == "planta":
            return self.salario * self.horas_trabajadas * 1.5
        elif tipo_profesor == "catedratico":
            return self.salario * self.horas_trabajadas * 1.2
        elif tipo_profesor == "transitorio":
            return self.salario * self.horas_trabajadas
        else:
            return 0.0    
        
    """
    d. Dependiendo de cada tipo de profesor debe diseñar al menos tres
    materias acordes con el rango de cada uno y se deben visualizar en
    pantalla por medio de un método.
    """    
    def materias(self):
        tipo_profesor = self.tipo.lower().strip()
        print("Las materias son las siguientes:")
        if tipo_profesor == "planta":
            print("  Estructuras de Datos\n  Bases de Datos\n  Ingeniería de Software")
        elif tipo_profesor == "catedratico":
            print("  Inteligencia Artificial\n  Desarrollo Web  \n  Seguridad Informática")
        elif tipo_profesor == "transitorio":
            print("  Programación I\n  Sistemas Operativos  \n  Redes de Computadores")
        else:
            print("Invalido") 

class Alumno(PersonalUniversitario):
    def __init__(self, cedula, nombre, apellido, correo, fecha_nacimiento, direccion,
                 codAlumno, semestre, carrera, promedio, creditos_aprobados, creditos_matriculados):
        PersonalUniversitario.__init__(self, cedula, nombre, apellido, correo, fecha_nacimiento, direccion)
        self.codAlumno = codAlumno
        self.semestre = semestre
        self.carrera = carrera
        self.promedio = promedio
        self.creditos_aprobados = creditos_aprobados
        self.creditos_matriculados = creditos_matriculados
        

class ProfesorAyudante(Profesor,Alumno):
    def __init__(self, cedula, nombre, apellido, correo, fecha_nacimiento, direccion,
                 codDocente, facultad, salario, tipo, horas_trabajadas, oficina,
                 codAlumno, semestre, carrera, promedio, creditos_aprobados, creditos_matriculados,
                 codProfesorAyudante, materia_asignada, profesor_titular, fecha_inicio, fecha_fin, evaluacion_desempeno):
        
        #No se puede usar super() porque hay herencia multiple, por lo que se debe llamar a los constructores de las clases padre de manera explicita
        Profesor.__init__(self, cedula, nombre, apellido, correo, fecha_nacimiento, direccion, 
                           codDocente, facultad, salario, tipo, horas_trabajadas, oficina)
        Alumno.__init__(self, cedula, nombre, apellido, correo, fecha_nacimiento, direccion,
                         codAlumno, semestre, carrera, promedio, creditos_aprobados, creditos_matriculados)
        self.codProfesorAyudante = codProfesorAyudante
        self.materiaAsignada = materia_asignada
        self.profesorTitular = profesor_titular
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.evaluacion_desempeno = evaluacion_desempeno

def guardar_profesor(profesor, path):
    with open(path, "a", encoding="utf-8") as archivo:
        archivo.write("=== PROFESOR ===\n")
        archivo.write(f"Cedula: {profesor.cedula}\n")
        archivo.write(f"Nombre: {profesor.nombre}\n")
        archivo.write(f"Apellido: {profesor.apellido}\n")
        archivo.write(f"Correo: {profesor.correo}\n")
        archivo.write(f"Fecha de nacimiento: {profesor.fecha_nacimiento}\n")
        archivo.write(f"Direccion: {profesor.direccion}\n")
        archivo.write(f"Codigo docente: {profesor.codDocente}\n")
        archivo.write(f"Facultad: {profesor.facultad}\n")
        archivo.write(f"Salario: {profesor.salario}\n")
        archivo.write(f"Tipo: {profesor.tipo}\n")
        archivo.write(f"Horas trabajadas: {profesor.horas_trabajadas}\n")
        archivo.write(f"Oficina: {profesor.oficina}\n")
        archivo.write(f"Fecha de registro: {profesor.fecha_registro.isoformat()}\n")
        archivo.write("\n")

def guardar_alumno(alumno, path):
    with open(path, "a", encoding="utf-8") as archivo:
        archivo.write("=== ALUMNO ===\n")
        archivo.write(f"Nombre: {alumno.nombre} {alumno.apellido}\n")
        archivo.write(f"Cedula: {alumno.cedula}\n")
        archivo.write(f"Codigo: {alumno.codAlumno}\n")
        archivo.write(f"Carrera: {alumno.carrera}\n")
        archivo.write(f"Semestre: {alumno.semestre}\n")
        archivo.write(f"Promedio: {alumno.promedio}\n")
        archivo.write(f"Fecha de registro: {alumno.fecha_registro.isoformat()}\n")
        archivo.write("\n")
        
def guardar_profesor_ayudante(ayudante, path):
    with open(path, "a", encoding="utf-8") as archivo:
        archivo.write("=== PROFESOR AYUDANTE ===\n")
        archivo.write(f"Nombre: {ayudante.nombre} {ayudante.apellido}\n")
        archivo.write(f"Cedula: {ayudante.cedula}\n")
        archivo.write(f"Codigo: {ayudante.codProfesorAyudante}\n")
        archivo.write(f"Materia asignada: {ayudante.materiaAsignada}\n")
        archivo.write(f"Profesor titular: {ayudante.profesorTitular}\n")
        archivo.write(f"Fecha de inicio: {ayudante.fecha_inicio}\n")
        archivo.write(f"Fecha de registro: {ayudante.fecha_registro.isoformat()}\n")
        archivo.write("\n")
        
        
def main():
    path = os.path.join(os.path.dirname(__file__), "profesores.txt")
    path_alumnos = os.path.join(os.path.dirname(__file__), "alumnos.txt")
    path_ayudantes = os.path.join(os.path.dirname(__file__), "profesores_ayudantes.txt")
    profesor = Profesor(
        "12345",
        "Carlos",
        "Perez",
        "carlos@utp.edu.co",
        "1990-05-20",
        "Pereira",
        "DOC001",
        "Ingenieria",
        50000,
        "planta",
        20,
        "Oficina 101"
    )
    profesor2 = Profesor(
            "23412345",
            "Simon",
            "Diez",
            "simon@utp.edu.co",
            "2006-04-26",
            "Pereira",
            "DOC011",
            "Ingenieria de Sistemas",
            500000,
            "catedratico",
            23,
            "Oficina 104"
        )
    print(f"Sueldo mensual: {profesor2.calcular_sueldo_mensual()}")
    profesor2.materias()
    print(profesor2.antiguedad())
    guardar_profesor(profesor,path)
    guardar_profesor(profesor2,path)
    
    alumno = Alumno(
        "98765",
        "Ana",
        "Gomez",
        "ana@utp.edu.co",
        "2005-03-15",
        "Pereira",
        "EST001",
        4,
        "Ingenieria de Sistemas",
        4.5,
        60,
        18
    )

    guardar_alumno(alumno, path_alumnos)

    ayudante = ProfesorAyudante(
        "45678",
        "Laura",
        "Martinez",
        "laura@utp.edu.co",
        "2004-08-12",
        "Pereira",
        "DOC020",
        "Ingenieria",
        30000,
        "transitorio",
        10,
        "Oficina 105",
        "EST020",
        5,
        "Ingenieria de Sistemas",
        4.6,
        80,
        20,
        "AYU001",
        "Bases de Datos",
        "Carlos Perez",
        "2026-02-01",
        "2026-11-30",
        "Excelente"
    )

    guardar_profesor_ayudante(ayudante, path_ayudantes)

if __name__ == "__main__":
    main()
