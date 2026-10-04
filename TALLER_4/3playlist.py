"""
Cree una clase llamada Playlist que tenga:
- nombre_playlist
- canciones (lista)

Implemente el método __len__ para que al ejecutar:
len(mi_playlist)
se obtenga el número de canciones.

Pruebe agregando al menos 6 canciones.
"""
class Playlist:
    def __init__(self, nombre_playlist):
        self.nombre_playlist = nombre_playlist
        self.canciones = []
    
    def __len__(self):
        return len(self.canciones)
    
    def agregar_canciones(self, cancion):
        self.canciones.append(cancion)
    
def main():
    playlist1 = Playlist("MYFIRSTPLAYLIST")
    playlist1.agregar_canciones("Dile")
    playlist1.agregar_canciones("Quiero Bailar")
    playlist1.agregar_canciones("Dakiti")
    playlist1.agregar_canciones("Safaera")
    playlist1.agregar_canciones("Gasolina")
    playlist1.agregar_canciones("Ahora y Siempre")
    
    print(f"En la playlist hay: {len(playlist1)}")
    
if __name__ == "__main__":
    main()