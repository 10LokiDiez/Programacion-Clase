"""
Cree una clase llamada Biblioteca que contenga:
- lista de libros

Implemente:
- __len__ → cantidad de libros
- __add__ → permitir unir dos bibliotecas.
La nueva biblioteca debe contener todos los libros de ambas.
"""

class Biblioteca:
    def __init__(self, lista_libros):
        self.lista_libros = lista_libros
        
    def __add__(self, other):
        return Biblioteca(self.lista_libros + other.lista_libros)
                          
    def __len__(self):
        return len(self.lista_libros)
    
b1 = Biblioteca(["1984","El Principito","Cien años de soledad" ])
b2 = Biblioteca(["Don Quijote de la Mancha","Orgullo y prejuicio" ]) 

print(len(b1))                      
b3 =b1 + b2

print(b3.lista_libros)