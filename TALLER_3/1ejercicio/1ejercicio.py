"""
1. Cree una clase llamada `Libro` con atributos como título, autor, año, editorial y
género. Incluya métodos para mostrar la información del libro, guardar los datos en un
archivo y buscar libros por autor.

"""
import os

class Libro:
    lista_de_libros = []
    def __init__(self, titulo,autor,year, editorial, genero):
        self.titulo = titulo
        self.autor = autor
        self.year = year
        self.editorial = editorial
        self.genero = genero
        Libro.lista_de_libros.append(self)
        
    def __str__(self):
        return f"El libro {self.titulo} del autor {self.autor} es del año {self.year}, es de la editorial {self.editorial} y el del genero {self.genero}"
    
    @classmethod
    def guardar_datos(cls, pathf):
        lineas = [ str(linea) + "\n" for linea in cls.lista_de_libros]
        with open(pathf, "w", encoding="utf-8") as file:
            file.writelines(lineas)
            print("DATOS GUARDADOS")
    
    @classmethod
    def buscar_libro(cls,autor_bus):
        encontrados = []
        for libro in cls.lista_de_libros:
            if libro.autor.lower() == autor_bus.lower():
                encontrados.append(libro)
                print(libro)
        
        if not encontrados:
            print("No hay libros de este autor")
        return encontrados
        
    
def main():
    #path
    path_file = os.path.join(os.path.dirname(__file__), "archivo_de_libros.txt")
    
    #diferentes instancias
    libro1 = Libro("Cien años de soledad", "Gabriel Garcia Marquez", 1967, "Sudamericana", "Realismo mágico")
    libro2 = Libro("El coronel no tiene quien le escriba", "Gabriel García Márquez", 1961, "Aguilar", "Ficción")
    libro3 = Libro("1984", "George Orwell", 1949, "Secker & Warburg", "Distopía")
    
    #info de los libros
    print(libro1)
    print(libro2)
    print(libro3)
    
    #metodo guardar los datos
    Libro.guardar_datos(path_file)
    
    #metodo para buscar por autor en el libro
    Libro.buscar_libro("Gabriel Garcia Marquez")
    
if __name__ == "__main__":
    main()