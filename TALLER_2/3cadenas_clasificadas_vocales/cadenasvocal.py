"""
3. Cadenas clasificadas por vocales
- Crea una clase `Cadena` con un atributo texto.
- Genere una lista de 15 cadenas.
- Implemente un método que ordene primero las cadenas que empiezan con vocal y
luego las demás.
- Guarde la lista ordenada en `cadenas.txt`.
"""

import os

class Cadena:
    def __init__(self,texto):
        self.texto = texto
        
    @staticmethod
    def ordenar_lista(lista):
        vocales = "aeiouAEIOU"
        lista_vocales = [cadena for cadena in lista if cadena.texto[0] in vocales]
        lista_sin_vocales = [cadena for cadena in lista if cadena.texto[0] not in vocales]
        return lista_vocales + lista_sin_vocales
    
def guardar_lista(lista):
    path_file = os.path.join(os.path.dirname(__file__), "cadenas.txt")
    
    with open(path_file, "w") as file:
        for frase in lista:
            file.write(f"{frase.texto} ")

def main():
    lista_de_cadenas = [
        Cadena("Avion"),
        Cadena("Casa"),
        Cadena("Elefante"),
        Cadena("Perro"),
        Cadena("Isla"),
        Cadena("Mesa"),
        Cadena("Oso"),
        Cadena("Libro"),
        Cadena("Uva"),
        Cadena("Carro"),
        Cadena("Arbol"),
        Cadena("Gato"),
        Cadena("Escuela"),
        Cadena("Papel"),
        Cadena("Iglesia")
    ]
    
    Cadena.ordenar_lista(lista_de_cadenas)
    guardar_lista(lista_de_cadenas)
    

if __name__ == "__main__":
    main()