"""
Cree una clase llamada EquipoFutbol con:
- nombre_equipo
- jugadores (lista)

Implemente __len__ para que al usar len() 
se obtenga la cantidad de jugadores del equipo.

Luego cree dos equipos y muestre cuántos jugadores tiene cada uno.
"""
class EquipoFutbol:
    def __init__(self, nombre_equipo):
        self.nombre_equipo = nombre_equipo
        self.jugadores = []
    
    def __len__(self):
        return len(self.jugadores)

    def agregar_jugador(self, cancion):
        self.jugadores.append(cancion)
    
def main():
    equipo1 = EquipoFutbol("Barca")
    equipo1.agregar_jugador("Lamine Yamal")
    equipo1.agregar_jugador("Pedri")
    equipo1.agregar_jugador("Fermin")
    equipo1.agregar_jugador("Cubarsi")
    equipo1.agregar_jugador("Raphinha")
    
    equipo2 = EquipoFutbol("Real Madrid")
    equipo2.agregar_jugador("Vinicius")
    equipo2.agregar_jugador("Mbappe")
    equipo2.agregar_jugador("Coutois")
    equipo2.agregar_jugador("Arda Guller")
    
    
    print(f"En el equipo {equipo1.nombre_equipo} hay: {len(equipo1)} jugadores")
    print(f"En el equipo {equipo2.nombre_equipo} hay: {len(equipo2)} jugadores")
    
if __name__ == "__main__":
    main()
