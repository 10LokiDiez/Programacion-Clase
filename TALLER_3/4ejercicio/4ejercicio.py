"""
4. Diseñe una clase `Vehículo` que guarde marca, modelo, año, tipo y placa. Incluya un
método para guardar en archivo solo los vehículos del año actual y otro para leerlos.
"""
import os

class Vehiculo:
    def __init__(self, marca,modelo,year,tipo,placa):
        self.marca = marca
        self.modelo = modelo
        self.year = year
        self.tipo = tipo
        self.placa = placa
        
    @staticmethod
    def guardarArchivo(path_file, mis_carros):
        with open(path_file, "w", encoding="utf-8") as file:
            for carro in mis_carros:
                file.write(f"{carro.marca},{carro.modelo},{carro.year},{carro.tipo},{carro.placa}\n")
                
    @staticmethod
    def leerYearActual(path_file):
        with open(path_file, "r", encoding="utf-8") as file:
            lineas = file.readlines()
            for modelo in lineas:
                datos = modelo.strip().split(',')
                if datos[2] == "2026":
                    for dato in datos:
                        print(f"{dato} ", end="")
                print()
            
def main():
    path_file = os.path.join(os.path.dirname(__file__), "carros.txt")
    mis_carros = [
        Vehiculo("Toyota", "Corolla", 2026, "Sedán", "ABC-123"),
        Vehiculo("Ford", "Fiesta", 2015, "Hatchback", "XYZ-987"),
        Vehiculo("Mazda", "CX-5", 2026, "SUV", "DEF-456"),
        Vehiculo("Honda", "Civic", 2022, "Sedán", "GHI-789")
    ]
    Vehiculo.guardarArchivo(path_file, mis_carros)
    Vehiculo.leerYearActual(path_file)
if __name__ == "__main__":
    main()