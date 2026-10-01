
"""
2. Conteo de palabras en frases
- Diseñe una clase `Frase` con atributos: texto y autor.
- Crea una lista de frases (una lista de objetos, cada objeto va a ser una instancia de
la clase Frase).
- Implemente un método que cuente cuántas veces aparece una palabra clave en
todas las frases.
- Guarde los resultados en `frases.txt`.
"""

import os

class Frase:
    def __init__(self, texto, autor):
        self.texto = texto
        self.autor = autor
    
    def contador_de_palabra_clave(self, clave):
        count = 0
        for palabra in self.texto.split():
            if clave == palabra:
                count += 1
        return count
    
    @staticmethod
    def contador_total(lista,clave):
        tot = 0
        for frase in lista:
            tot += frase.contador_de_palabra_clave(clave)
        return tot
        
        
    
def guardar_resultados(clave, suma):
    path_file = os.path.join(os.path.dirname(__file__), "frases.txt")
    
        
    with open(path_file, "a") as file:
        file.write(f"Hay {suma} '{clave}' en las frases\n")
    
    
    
def main():
    lista_de_frases = [Frase("No esperes a que todo sea perfecto . Empieza ahora y hazlo posible", "Simon Diez"),
                       Frase("La mejor manera de empezar es dejar de hablar y comenzar a hacer","Walt Disney"),
                       Frase("No importa lo lento que vayas , siempre y cuando no te detengas", "Confucio")]
    
    clave = input("Ingrese la palabra que desea buscar: ")
    suma = Frase.contador_total(lista_de_frases, clave)
    
    print (f"Hay {suma} '{clave}' en las frases")
    guardar_resultados(clave, suma)


if __name__ == "__main__":
    main()