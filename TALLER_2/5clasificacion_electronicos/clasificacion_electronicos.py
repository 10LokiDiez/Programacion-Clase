""""
5. Clasificación de objetos electrónicos
- Crea una clase `Electrodomestico` con atributos: nombre, marca, consumo (en
watts).
- Implemente un método que clasifique los objetos como “bajo consumo” (<500W) o
“alto consumo” (>=500W).
- Guarda el inventario en `electrodomesticos.txt`.
"""
import os
class Electrodomestico:
    def __init__(self, nombre, marca, consumo):
        self.nombre = nombre 
        self.marca = marca
        self.consumo = consumo
    

    def clasificacion(self):
        if self.consumo < 500:
            return f"bajo consumo"
        else:
            return f"alto consumo"
        
    def guardar_inventario(self):
        path_file = os.path.join(os.path.dirname(__file__), "electrodomesticos.txt")
        with open(path_file, "a") as file:
            file.write(f"{self.nombre} , {self.marca}, {self.clasificacion()}, {self.marca}, {self.consumo}W\n")
    
def verificar_archivo():
    if os.path.exists(os.path.join(os.path.dirname(__file__), "electrodomesticos.txt")):
        os.remove(os.path.join(os.path.dirname(__file__), "electrodomesticos.txt"))
        
def main():
    lista_electrodomesticos = [
        Electrodomestico("Televisor LED", "Samsung", 120),
        Electrodomestico("Nevera Ejecutiva", "LG", 250),
        Electrodomestico("Microondas", "Panasonic", 800),
        Electrodomestico("Licuadora", "Oster", 450),
        Electrodomestico("Ventilador de Torre", "Whirlpool", 100),
        Electrodomestico("Aspiradora", "Electrolux", 950)
    ]
    verificar_archivo()
    for electrodomestico in lista_electrodomesticos:
        electrodomestico.guardar_inventario()
        print(f"{electrodomestico.nombre} ({electrodomestico.marca}) - {electrodomestico.consumo}W -> Clasificacion: {electrodomestico.clasificacion()}")

    
if __name__ == '__main__':
    main()