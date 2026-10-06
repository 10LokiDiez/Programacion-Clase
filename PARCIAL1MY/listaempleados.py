"""
2. Sistema de Gestión de Empleados
Crea una aplicación de gestión de empleados. Debes crear las siguientes clases:
"""
"""

Clase Empleado:
• Atributos:

o Nombre (cadena de texto)
o ID (entero)
o Salario Base (flotante)
o Años de Experiencia (entero)

• Métodos:

o Constructor para inicializar todos los atributos.
o Un método calcular_salario() que retorne el salario total del empleado. El salario total se 
calcula sumando un bono al salario base que depende de los años de experiencia:
▪ Entre 0 y 2 años: bono de 5% del salario base.
▪ Entre 3 y 5 años: bono de 10% del salario base.
▪ Más de 5 años: bono de 15% del salario base.
o Un método para representar al empleado en formato de texto.
"""
import os
class Empleado:
    def __init__(self, id, nombre, salario, years):
        self.id = id
        self.nombre = nombre
        self.salario = salario
        self.years = years
    
    def calcular_salario(self):
        if self.years > 5:
            bono = 0.15
        elif self.years >= 3:
            bono = 0.10
        else:
            bono = 0.05
        return self.salario + (self.salario * bono)
        
    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Salario Base: {self.salario:.2f}, Años de experiencia {self.years}, Salario Total {self.calcular_salario():.2f}"

"""
Clase GestorEmpleados:

• Atributos:
o Una lista de empleados.

• Métodos:
o agregar_empleado(empleado: Empleado): Agrega un empleado a la lista.
o eliminar_empleado(id: int): Elimina un empleado de la lista según su ID.
o buscar_empleado(id: int): Busca y devuelve un empleado por su ID.
o editar_empleado(id: int): Busca un empleado y deja editar la informacion que se quiera del empleado,
luego se debe actualizar el archivo donde esta guardada la información.
o mostrar_empleados(): Muestra todos los empleados de la lista junto con sus salarios totales.
o guardar_empleados(archivo: str): Guarda la lista de empleados en un archivo.
o cargar_empleados(archivo: str): Carga la lista de empleados desde un archivo.
"""

class GestorEmpleados:
    def __init__(self):
        self.lista = []
        
    def agregar_empleado(self,empleado):
        self.lista.append(empleado)
        
    def eliminar_empleado(self,id):
        encontro = False
        for empleado in self.lista:
            if empleado.id == id:
                self.lista.remove(empleado)
                print("Se elimino el empleado")
                encontro = True
                break
        if encontro == False:
            print("No se encontro el empleado")
            
    #o buscar_empleado(id: int): Busca y devuelve un empleado por su ID.
    def buscar_empleado(self, id):
        encontro = False
        for empleado in self.lista:
            if empleado.id == id:
                return empleado
        if encontro == False:
            return            
    
    #o mostrar_empleados(): Muestra todos los empleados de la lista junto con sus salarios totales.
    def mostrar_empleados(self):
        for empleado in self.lista:
            print(empleado)
    
    # guardar_empleados(archivo: str): Guarda la lista de empleados en un archivo.
    def guardar_empleados(self, path_file):
        with open(path_file, "w", encoding="utf-8") as file:
            for empleado in self.lista:
                file.write(f"{empleado.id},{empleado.nombre},{empleado.salario},{empleado.years}\n")
    
    # o cargar_empleados(archivo: str): Carga la lista de empleados desde un archivo.        
    def cargar_empleados(self, path_file):
        if not os.path.exists(path_file):
            print("Archivo no encontrado")
            return
        with open(path_file, "r", encoding="utf-8") as file:
            lineas = file.readlines()
        for linea in lineas:
            id, nombre, salario, years=linea.strip().split(",")
            self.agregar_empleado(Empleado(int(id),nombre,float(salario),int(years)))
            
    #o editar_empleado(id: int): Busca un empleado y deja editar la informacion que se quiera del empleado,
    #luego se debe actualizar el archivo donde esta guardada la información.
    def editar_empleado(self,id,path_file):
        if not os.path.exists(path_file):
            print("Archivo no encontrado")
            return
        empleado = self.buscar_empleado(id)
        if empleado == None:
            return
        while True:
            print(f"1. ID : {empleado.id}")
            print(f"2. Nombre : {empleado.nombre}")
            print(f"3. Salario : {empleado.salario:.2f}")
            print(f"4. Años de experiencia: {empleado.years}")
            print(f"5. Salir ")
            print("Que informacion quiere editar(1-5)? ")
            edicion = int(input("Ingrese un numero: "))
            if  1 <= edicion <= 5:
                print("Dato Valido")
                break
            else:
                print("Dato Erroneo")
                continue
        match edicion:
            case 1:
                new_id = int(input("Ingrese el nuevo ID del usuario: "))
                if self.buscar_empleado(new_id) == None:
                    empleado.id = new_id
                    print(f"El ID de {empleado.nombre} fue editado exitosamente")
                else:
                    print("Este ID ya lo tiene otro usuario")
            case 2:
                new_nombre = input("Ingrese el nuevo nombre del usuario: ")
                empleado.nombre = new_nombre
                print(f"El Nombre de {empleado.id} fue editado exitosamente")
                
            case 3:
                new_salario = float(input("Ingrese el nuevo salario del usuario: "))
                empleado.salario = new_salario
                print(f"El salario de {empleado.nombre} fue editado exitosamente")
                
            case 4:
                new_years = int(input("Ingrese los nuevos años de de experiencia del usuario: "))
                empleado.years = new_years
                print(f"Los años de experiencia de {empleado.nombre} fueron editado exitosamente")
                
            case 5:
                print("Saliendo de la edicion de datos...")
                
            case _:
                print("ERROR")
                
        self.guardar_empleados(path_file)
        print("Saliendo de la edicion de datos...")
            
"""
Requerimiento adicional: Implementa un sistema de menús que permita al
usuario interactuar con la clase GestorEmpleados, agregar empleados,
eliminarlos, buscar por ID y ver la lista de empleados y sus salarios, para este
ejercicio puede implementar archivos de texto plano.
"""
def agregar_empleado_menu(gestorempleados, path_file):
    print("------ AGREGAR EMPLEADO -----")
    id = int(input("Ingresa un ID UNICO para el empleado: "))
    if gestorempleados.buscar_empleado(id) != None:
        print("El ID ya lo tiene otro usuario")
    else:
        nombre = input("Ingresa un nombre para el empleado: ")
        salario = float(input("Ingresa un salario para el empleado: "))
        years = int(input("Ingresa los años de experiencia del empleado: "))
        gestorempleados.agregar_empleado(Empleado(id,nombre,salario,years))
        gestorempleados.guardar_empleados(path_file)
        print("Empleado Agregado con exito")
        
        

def menu(path_file):
    print("----- BIENVENIDO AL SISTEMA GESTOR DE EMPLEADOS -----")
    gestorempleados = GestorEmpleados()
    ca = input("Le recomendamos antes de empezar cargar los empleados creados en el archivo(s/n): ").lower()
    if ca == "s":
        gestorempleados.cargar_empleados(path_file)
    else:
        with open(path_file, "w") as file:
            pass
    while True:
        print("-" * 50)
        print("1. Agregar Empleado")
        print("2. Eliminar Empleado")
        print("3. Buscar Empleado por ID")
        print("4. Editar Empleado")
        print("5. Ver Lista de Empleados y sus Salarios")
        print("6. Salir del Programa")
        opcion = int(input("Ingresa la opcion que desea: "))
        
        if  1 <= opcion <= 6:
            print("Dato Valido")
        else:
            print("Dato Erroneo")
            continue

        match opcion:
            case 1:
                agregar_empleado_menu(gestorempleados, path_file)
            case 2:
                print("------ ELIMINAR EMPLEADO -----")
                id = int(input("Ingresa un ID del empleado: "))
                gestorempleados.eliminar_empleado(id)
                gestorempleados.guardar_empleados(path_file)
                
            case 3:
                print("------ BUSCAR EMPLEADO -----")
                id = int(input("Ingresa un ID del empleado: "))
                value = gestorempleados.buscar_empleado(id)
                if value != None:
                    print(value)
                else:
                    print("No se encontro el empleado")
            case 4:
                print("------ EDITAR EMPLEADO -----")
                id = int(input("Ingresa un ID del empleado: "))
                gestorempleados.editar_empleado(id,path_file)
            case 5:
                print("------ VER LISTA DE EMPLEADOS -----")
                gestorempleados.mostrar_empleados()
            case 6:
                print("Saliendo del programa...")
                break
            case _:
                print("Opcion Invalida, Intente de nuevo")
        
def main():
    path_file = os.path.join(os.path.dirname(__file__), "listaempleados.txt")
    print(path_file)
    menu(path_file)
    
main()