"""
6. Implemente una clase `NotaMusical` con atributos como nombre, frecuencia y
duración. Guarde en un archivo las notas mayores a cierta frecuencia. Añada un
método que simule la ejecución de la nota (texto).
"""
import os
class NotaMusical:
    
    def __init__ (self, nombre, frecuencia, duracion):
        self.nombre = nombre
        self.frecuencia = frecuencia
        self.duracion = duracion
        
    def reproducir(self):
        print(f"Sonando: {self.nombre} con frecuencia {self.frecuencia} Hz  durante {self.duracion} segundos")
        
    @staticmethod
    def guardarAltas(melodias, maxim):
        ruta_archivo = os.path.join(os.path.dirname(__file__), "melodias.txt")
        with open(ruta_archivo, "w", encoding="utf-8") as file:
            for melodia in melodias:
                if melodia.frecuencia > maxim:
                    file.write(f"{melodia.nombre}, {melodia.frecuencia}, {melodia.duracion}\n")
        
def main():
    melodia = [
        NotaMusical("Do", 261.63, 1.0),
        NotaMusical("Mi", 329.63, 0.5),
        NotaMusical("Sol", 392.00, 0.5),
        NotaMusical("La", 440.00, 2.0),
        NotaMusical("Do agudo", 523.25, 1.5)
    ]
    NotaMusical.guardarAltas(melodia,350.0)
    
    for music in melodia:
        music.reproducir()

if __name__ == "__main__":
    main()