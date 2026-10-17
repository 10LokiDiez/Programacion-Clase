"""
2. Haciendo uso el siguiente diagrama:

Implemente:
• Crea al menos un objeto de cada subclase y añádelos a una lista llamada vehículos.
• Realiza una función llamada catalogar() que reciba la lista de vehículos y los recorra
mostrando el nombre de su clase y sus atributos.
• Modifica la función catalogar() para que reciba un argumento optativo ruedas,
haciendo que muestre únicamente los que su número de ruedas concuerde con el
valor del argumento. También debe mostrar un mensaje "Se han encontrado {}
vehículos con {} ruedas:" únicamente si se envía el argumento ruedas. Ponla a
prueba con 0, 2 y 4 ruedas como valor.

"""
class Vehiculo:
    def __init__(self, color, numllantas):
        self.color = color
        self.numllantas = numllantas

class Coche(Vehiculo):
    def __init__(self, color, numllantas, velocidad, cilindrada):
        super().__init__(color, numllantas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
        
    def __str__(self):
        return f"Coche: Color: {self.color}, Numero de llantas: {self.numllantas}, Velocidad: {self.velocidad} km/h, Cilindrada: {self.cilindrada} cc"
class Camioneta(Coche):
    def __init__(self, color, numllantas, velocidad, cilindrada, carga):
        super().__init__(color, numllantas, velocidad, cilindrada)
        self.carga = carga
        
    def __str__(self):
        return f"Camineta: Color: {self.color}, Numero de llantas: {self.numllantas}, Velocidad: {self.velocidad} km/h, Cilindrada: {self.cilindrada} cc, Carga: {self.carga}"
        
class Bicicleta(Vehiculo):
    def __init__(self, color, numllantas, tipo):
        super().__init__(color, numllantas)
        self.tipo = tipo
    
    def __str__(self):
        return f"Bicicleta: Color: {self.color}, Numero de llantas: {self.numllantas}, Tipo: {self.tipo}"
        
class Motocicleta(Bicicleta):
    def __init__(self, color, numllantas, tipo, velocidad, cilindrada):
        super().__init__(color, numllantas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
        
    def __str__(self):
        return f"Motocicleta: Color: {self.color}, Numero de llantas: {self.numllantas}, Tipo: {self.tipo}, Velocidad: {self.velocidad} km/h, Cilindrada: {self.cilindrada} cc"

def catalogar(lista, ruedas = None):
    if ruedas == None:
        for obj in lista:
            print(obj)
    else:
        count = 0
        for obj in lista:
            if obj.numllantas == ruedas:
                print(obj)
                count += 1
        print(f"Se han encontrado {count} vehículos con {ruedas} ruedas:")
    
         
def main():
    coche1 = Coche("Azul", 4, 140, 2500)
    camioneta1 = Camioneta("Rojo", 4, 120, 2500, 1700)
    bicicleta1 = Bicicleta("Amarillo",2,"Urbana")
    moto1 = Motocicleta("Negro",2,"Deportiva",135,1000)
    vehiculos = [coche1,camioneta1,bicicleta1,moto1]
    print("\nCATALOGO NORMAL")
    catalogar(vehiculos)
    print("\nCATALOGO CON RUEDAS")
    catalogar(vehiculos, 4)
    
if __name__ == "__main__":
    main()
        
