"""
Cree una clase llamada Libro con los atributos:
- titulo
- autor

Implemente __str__ para que al imprimir el objeto aparezca:
"El principito" escrito por Antoine de Saint-Exupéry

Cree 5 libros y guárdelos en una lista.
Luego imprima todos los libros usando un bucle.
"""
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    
    def __str__(self):
        return f"\"{self.titulo}\" escrito por {self.autor}"
    
def main():
    libros = [Libro("Cien años de soledad","Gabriel Garcia Márquez"),
              Libro("Don Quijote de la Mancha","Miguel de Cervantes"),
              Libro("1984","George Orwell"),
              Libro("Orgullo y prejuicio","Jane Austen"),
              Libro("La Odisea","Homero")]
    
    for libro in libros:
        print(libro)
if __name__ == "__main__":
    main()