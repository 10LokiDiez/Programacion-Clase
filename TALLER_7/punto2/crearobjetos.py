from classes import Coche, Camioneta,Bicicleta,Motocicleta

def crear_objetos():
    coche1 = Coche("Azul", 4, 140, 2500)
    camioneta1 = Camioneta("Rojo", 4, 120, 2500, 1700)
    bicicleta1 = Bicicleta("Amarillo", 2, "Urbana")
    moto1 = Motocicleta("Negro", 2, "Deportiva", 135, 1000)
    
    return [coche1, camioneta1, bicicleta1, moto1]