"""
2. Haga uso del punto 2 del taller 5 para realizar lo siguiente:
a. Encapsular todos los atributos y métodos
b. Diseñar los métodos set y get correspondientes.
c. Implementando modularidad debe tener en un archivo las clases, en
otro archivo los objetos y en otro archivo el llamado a los métodos o
atributos de dichos objetos, si dicha ruta no se puede implementar
proponga una posible solución.

"""
class Vehiculo:
    def __init__(self, color, numllantas):
        self.__color = color
        self.__numllantas = numllantas 

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def get_numllantas(self):
        return self.__numllantas

    def set_numllantas(self, numllantas):
        self.__numllantas = numllantas
        
class Coche(Vehiculo):
    def __init__(self, color, numllantas, velocidad, cilindrada):
        super().__init__(color, numllantas)
        self.__velocidad = velocidad
        self.__cilindrada = cilindrada
        
    def get_velocidad(self):
        return self.__velocidad

    def set_velocidad(self, velocidad):
        self.__velocidad = velocidad

    def get_cilindrada(self):
        return self.__cilindrada

    def set_cilindrada(self, cilindrada):
        self.__cilindrada = cilindrada
        
    def __str__(self):
        return f"Coche: Color: {self.get_color()}, Numero de llantas: {self.get_numllantas()}, Velocidad: {self.get_velocidad()} km/h, Cilindrada: {self.get_cilindrada()} cc"
    
class Camioneta(Coche):
    def __init__(self, color, numllantas, velocidad, cilindrada, carga):
        super().__init__(color, numllantas, velocidad, cilindrada)
        self.__carga = carga
    
    def get_carga(self):
        return self.__carga

    def set_carga(self, carga):
        self.__carga = carga
        
    def __str__(self):
        return f"Camioneta: Color: {self.get_color()}, Numero de llantas: {self.get_numllantas()}, Velocidad: {self.get_velocidad()} km/h, Cilindrada: {self.get_cilindrada()} cc, Carga: {self.get_carga()}"
class Bicicleta(Vehiculo):
    def __init__(self, color, numllantas, tipo):
        super().__init__(color, numllantas)
        self.__tipo = tipo
    
    def get_tipo(self):
        return self.__tipo

    def set_tipo(self, tipo):
        self.__tipo = tipo

    def __str__(self):
        return f"Bicicleta: Color: {self.get_color()}, Numero de llantas: {self.get_numllantas()}, Tipo: {self.get_tipo()}"
    
class Motocicleta(Bicicleta):
    def __init__(self, color, numllantas, tipo, velocidad, cilindrada):
        super().__init__(color, numllantas, tipo)
        self.__velocidad = velocidad
        self.__cilindrada = cilindrada

    def get_velocidad(self):
        return self.__velocidad

    def set_velocidad(self, velocidad):
        self.__velocidad = velocidad

    def get_cilindrada(self):
        return self.__cilindrada

    def set_cilindrada(self, cilindrada):
        self.__cilindrada = cilindrada

    def __str__(self):
        return f"Motocicleta: Color: {self.get_color()}, Numero de llantas: {self.get_numllantas()}, Tipo: {self.get_tipo()}, Velocidad: {self.get_velocidad()} km/h, Cilindrada: {self.get_cilindrada()} cc"
