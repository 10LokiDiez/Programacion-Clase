"""
2. Diseñe y modele un problema de cotidianidad con herencia múltiple,
implementando las siguientes características:
a. Debe tener al menos dos clases principales.
b. Debe tener al menos 5 subclases.
c. Las clases principales deben tener cada una al menos 5 atributos.
d. Entre todas las clases principales y subclases deben diseñar al menos 7
métodos.
e. Se debe crear una lista para almacenar los objetos creados para probar
las clases y subclases.

f. Guarde la información que crea necesaria en un archivo para este
programa.
"""
class Dispositivo:

    def __init__(self, marca, modelo, numero_serie,
                 consumo_energia, estado="Apagado"):

        self.marca = marca
        self.modelo = modelo
        self.numero_serie = numero_serie
        self.consumo_energia = consumo_energia
        self.estado = estado

class Conectividad:

    def __init__(self, wifi=True, bluetooth=False,
                 direccion_ip="No asignada",
                 nombre_red="Sin red",
                 estado_conexion="Desconectado"):

        self.wifi = wifi
        self.bluetooth = bluetooth
        self.direccion_ip = direccion_ip
        self.nombre_red = nombre_red
        self.estado_conexion = estado_conexion

class TelevisorInteligente(Dispositivo, Conectividad):

    def __init__(self, marca, modelo, numero_serie,
                 consumo_energia, estado="Apagado",
                 wifi=True, bluetooth=False,
                 direccion_ip="No asignada",
                 nombre_red="Sin red",
                 estado_conexion="Desconectado",
                 tamano_pantalla=55, canal_actual=1):

        Dispositivo.__init__(
            self, marca, modelo, numero_serie,
            consumo_energia, estado
        )

        Conectividad.__init__(
            self, wifi, bluetooth, direccion_ip,
            nombre_red, estado_conexion
        )

        self.tamano_pantalla = tamano_pantalla
        self.canal_actual = canal_actual

class ParlanteInteligente(Dispositivo, Conectividad):

    def __init__(self, marca, modelo, numero_serie,
                 consumo_energia, estado="Apagado",
                 wifi=True, bluetooth=False,
                 direccion_ip="No asignada",
                 nombre_red="Sin red",
                 estado_conexion="Desconectado",
                 volumen=50, reproduciendo=False):

        Dispositivo.__init__(
            self, marca, modelo, numero_serie,
            consumo_energia, estado
        )

        Conectividad.__init__(
            self, wifi, bluetooth, direccion_ip,
            nombre_red, estado_conexion
        )

        self.volumen = volumen
        self.reproduciendo = reproduciendo

class BombilloInteligente(Dispositivo, Conectividad):

    def __init__(self, marca, modelo, numero_serie,
                 consumo_energia, estado="Apagado",
                 wifi=True, bluetooth=False,
                 direccion_ip="No asignada",
                 nombre_red="Sin red",
                 estado_conexion="Desconectado",
                 intensidad=100, color="Blanco"):

        Dispositivo.__init__(
            self, marca, modelo, numero_serie,
            consumo_energia, estado
        )

        Conectividad.__init__(
            self, wifi, bluetooth, direccion_ip,
            nombre_red, estado_conexion
        )

        self.intensidad = intensidad
        self.color = color

class CamaraSeguridad(Dispositivo, Conectividad):

    def __init__(self, marca, modelo, numero_serie,
                 consumo_energia, estado="Apagado",
                 wifi=True, bluetooth=False,
                 direccion_ip="No asignada",
                 nombre_red="Sin red",
                 estado_conexion="Desconectado",
                 resolucion="1080p", grabando=False):

        Dispositivo.__init__(
            self, marca, modelo, numero_serie,
            consumo_energia, estado
        )

        Conectividad.__init__(
            self, wifi, bluetooth, direccion_ip,
            nombre_red, estado_conexion
        )

        self.resolucion = resolucion
        self.grabando = grabando


class TermostatoInteligente(Dispositivo, Conectividad):

    def __init__(self, marca, modelo, numero_serie,
                 consumo_energia, estado="Apagado",
                 wifi=True, bluetooth=False,
                 direccion_ip="No asignada",
                 nombre_red="Sin red",
                 estado_conexion="Desconectado",
                 temperatura_actual=22,
                 temperatura_objetivo=22):

        Dispositivo.__init__(
            self, marca, modelo, numero_serie,
            consumo_energia, estado
        )

        Conectividad.__init__(
            self, wifi, bluetooth, direccion_ip,
            nombre_red, estado_conexion
        )

        self.temperatura_actual = temperatura_actual
        self.temperatura_objetivo = temperatura_objetivo
