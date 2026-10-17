"""
1. Realice un programa en el que podamos observar los atributos de las clases
inspiradas en el siguiente gráfico, se debe implementar herencia simple y se
deben guardar la información de cada vehículo en uno o varios archivos para
poder listarlos cuando se necesiten, el programa también debe contar con los
siguientes métodos:

- Métodos Vehículo:
a. Debe mostrar información dependiendo del vehículo (camión, moto,
automóvil) de cuantos años aproximadamente le pueden durar las llantas esto
también sujeto a tres tipos de marcas.
b. tipo de combustible que se recomienda usar para el vehículo que se elija
(ACPM, Extra, Corriente).

- Métodos Coche:
a. Mostrar que tiempo se tomaría cada vehículo en llegar desde Pereira a
diferentes lugares en Colombia (mínimo 5 lugares).
b. debe mostrar cuanto gastaría al mes en combustible cada automóvil
suponiendo que cada uno hace viajes de 1000 km mensuales, ustedes pueden
consultar precios actuales para parametrizar el combustible.

"""
import os
class Vehiculo:
    def __init__(self, color, numllantas):
        self.color = color
        self.numllantas = numllantas
        
    def duracion_llantas(self, marca):
        print("Por favor, especifica el tipo de vehiculo (Coche, Moto o Camion) para calcular la duracion exacta de las llantas...")
        
    def tipo_cilindraje(self):
        print("Te recomendamos especificar el tipo de vehiculo para darte una recomendacion exacta de combustible...")

class Coche(Vehiculo):
    def __init__(self, color, numllantas, velocidad, cilindrada):
        super().__init__(color, numllantas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
        
    def duracion_llantas(self, marca):
        marca = marca.lower()
        if marca == "michelin":
            print(f"Estas llantas {marca.title()} pueden durar 4 años")
        elif marca == "goodyear":
            print(f"Estas llantas {marca.title()} pueden durar 3.5 años")
        elif marca == "pirelli":
            print(f"Estas llantas {marca.title()} pueden durar 3 años")
        else:
            print(f"No se reconoce {marca.title()}")
            
    
    def recomendar_cilindraje(self):
        if self.cilindrada >= 2000:
            print(f"La recomendacion es que sea Extra por su cilindraje {self.cilindrada} cc")
        elif self.cilindrada > 0:
            print(f"La recomendacion es que sea Corriente por su cilindraje {self.cilindrada} cc")
        else:
            print("No se reconoce el cilindraje")
            
    def destinos_tiempo_llegada(self, destinos):
        for destino in destinos: 
            print(f"Para el destino {destino} se demora {destinos[destino]/self.velocidad:.2f} h")
        
    def gasto_combustible(self):
        kmgalon = 40
        galonmes = 1000/ kmgalon
        print(f"""
              Los precios son:
Gasolina: {15600*galonmes:,}COP
Extra: {18000*galonmes:,}COP""")
        
    def guardar_carro(self):
        with open((os.path.join((os.path.dirname(__file__)),"vehiculos.txt")), "a", encoding="utf-8") as file:
            file.write(f"{self.color},{self.numllantas},{self.velocidad},{self.cilindrada}")
def main():
    destinos = {"Armenia": 45,
                "Manizales": 50,
                "Cali": 210,
                "Medellin": 215,
                "Bogota": 320,}
    mi = Vehiculo("red", 4)
    mi.duracion_llantas("es")
    carro1 = Coche("red", 4, 100, 5000)
    carro1.duracion_llantas("Michelin")
    carro1.destinos_tiempo_llegada(destinos)
    carro1.guardar_carro()
    carro1.gasto_combustible()
    
if __name__ == "__main__":
    main()
        
