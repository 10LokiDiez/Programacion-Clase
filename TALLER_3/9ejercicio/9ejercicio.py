"""
9. Diseñe una clase `Empresa` que maneje empleados, sus salarios, bonificaciones y
descuentos. Incluya métodos para generar reportes en archivos separados por
departamentos.

"""

import os

class Empleados:
    def __init__(self, id_empleado, nombre, departamento, salario):
        self.id_empleado = id_empleado
        self.nombre = nombre
        self.departamento = departamento
        self.salario = salario
        self.bonificaciones = 0
        self.descuentos = 0
    
    def agregar_descuento(self, num):
        self.descuentos += num
        
    def agregar_bonificacion(self, monto):
        self.bonificaciones += monto
    
    def calcular_salario_neto(self):
        return self.salario + self.bonificaciones - self.descuentos
    
    def obtener_estadisticaso(self):
        return f"{self.id_empleado},{self.nombre},{self.departamento},{self.salario:.2f},{self.bonificaciones:.2f},{self.descuentos:.2f},{self.calcular_salario_neto():.2f}"

class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def generar_reportes_por_departamento(self):            
        path_file = os.path.join(os.path.dirname(__file__))
        empleados_por_departamento = {}
        for empleado in self.empleados:
            if empleado.departamento not in empleados_por_departamento:
                empleados_por_departamento[empleado.departamento] = []
            empleados_por_departamento[empleado.departamento].append(empleado)
            
        for departamento, lista_empleados in empleados_por_departamento.items():
            nombre_archivo = f"reporte_{departamento.replace(' ', '_').lower()}.txt"
            ruta = os.path.join(path_file, nombre_archivo)
            
            with open(ruta, "w", encoding="utf-8") as archivo:
                archivo.write("ID,Nombre,Departamento,Salario Base,Bonificaciones,Descuentos,Salario Neto\n")
                for empleado in lista_empleados:
                    archivo.write(empleado.obtener_estadisticaso() + "\n")


def main():
    empresa = Empresa("Tech S.A.")
    
    emp1 = Empleados("001", "Ana Gomez", "IT", 2000)
    emp1.agregar_bonificacion(300)
    
    emp2 = Empleados("002", "Luis Perez", "IT", 2500)
    emp2.agregar_descuento(100)
    
    emp3 = Empleados("003", "Carlos Ruiz", "Ventas", 1500)
    emp3.agregar_bonificacion(500)
    
    empresa.agregar_empleado(emp1)
    empresa.agregar_empleado(emp2)
    empresa.agregar_empleado(emp3)
    
    empresa.generar_reportes_por_departamento()
    
    
if __name__ == "__main__":
    main()