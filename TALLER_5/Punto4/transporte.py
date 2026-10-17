"""
4. Crea una clase base Transporte con atributos capacidad y tarifa.
Subclases: Bus, Taxi y Metro, cada una sobrescribe un método
calcular_pasaje(km) que determine el costo según la distancia recorrida.
Ejemplo:
Bus: tarifa fija + (100 * km)
Taxi: (500 * km)
Metro: tarifa fija sin importar los km
Crea varios transportes y muestra el costo de un trayecto de 10 km para cada uno
usando polimorfismo.

"""

class Transporte:
    def __init__(self, capacidad, tarifa):
        self.capacidad = capacidad
        self.tarifa = tarifa
    
    def calcular_pasaje(self, distancia):
        pass
    
class Bus(Transporte):
    def __init__(self, capacidad, tarifa):
        super().__init__(capacidad, tarifa)

    def calcular_pasaje(self, distancia):
        print(f"El pasaje tiene un costo de ${self.tarifa + (100*distancia):,}")
    
    
class Taxi(Transporte):
    def __init__(self, capacidad, tarifa):
        super().__init__(capacidad, tarifa)

    def calcular_pasaje(self, distancia):
        print(f"El pasaje tiene un costo de ${500*distancia:,}")
    
    
class Metro(Transporte):
    def __init__(self, capacidad, tarifa):
        super().__init__(capacidad, tarifa)
        
    def calcular_pasaje(self, distancia):
        print(f"El pasaje tiene un costo de ${self.tarifa:,}")
        
        
def main():
    taxi1 = Taxi(4, 0)
    bus1 = Bus(40, 2000)
    bus2 = Bus(42, 2300)
    bus3 = Bus(50, 2500)
    metro1 = Metro(100, 3000)
    listaTransporte = [taxi1, bus1, bus2, bus3, metro1]
    for transporte in listaTransporte:
        print(f"{transporte.__class__.__name__}:")
        transporte.calcular_pasaje(10)
        
if __name__ == "__main__":
    main()
