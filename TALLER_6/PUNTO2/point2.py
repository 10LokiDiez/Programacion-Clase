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

import os
class Dispositivo:

    def __init__(self, marca, modelo, numero_serie,
                 consumo_energia, estado="Apagado"):

        self.marca = marca
        self.modelo = modelo
        self.numero_serie = numero_serie
        self.consumo_energia = consumo_energia
        self.estado = estado

    def encender(self):
        self.estado = "Encendido"
        print(f"{self.modelo} esta encendido.")

    def apagar(self):
        self.estado = "Apagado"
        print(f"{self.modelo} esta apagado.")

    def mostrar_informacion(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Numero de serie: {self.numero_serie}")
        print(f"Consumo de energía: {self.consumo_energia} W")
        print(f"Estado: {self.estado}")

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

    def conectar(self, nombre_red=None, direccion_ip=None):

        if nombre_red is not None:
            self.nombre_red = nombre_red

        if direccion_ip is not None:
            self.direccion_ip = direccion_ip

        self.estado_conexion = "Conectado"
        print(f"Dispositivo conectado a la red {self.nombre_red}.")

    def desconectar(self):
        self.estado_conexion = "Desconectado"
        print("Dispositivo desconectado de la red.")

    def comprobar_conexion(self):
        return self.estado_conexion == "Conectado"

    def mostrar_conexion(self):
        print(f"Wi-Fi disponible: {self.wifi}")
        print(f"Bluetooth disponible: {self.bluetooth}")
        print(f"Dirección IP: {self.direccion_ip}")
        print(f"Nombre de la red: {self.nombre_red}")
        print(f"Estado de conexión: {self.estado_conexion}")

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

    def cambiar_canal(self, canal):
        if canal > 0:
            self.canal_actual = canal
            print(f"Canal cambiado al {canal}.")
        else:
            print("El canal debe ser mayor que cero.")

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

    def cambiar_intensidad(self, intensidad):
        if 0 <= intensidad <= 100:
            self.intensidad = intensidad
            print(f"Intensidad ajustada al {intensidad}%.")
        else:
            print("La intensidad debe estar entre 0 y 100.")
            
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

def guardar_datos(path, dispositivos):
    with open(path, "w", encoding="utf-8") as archivo:
        for dispositivo in dispositivos:
            archivo.write("\n-------------------------\n")
            archivo.write(f"Marca: {dispositivo.marca}\n")
            archivo.write(f"Modelo: {dispositivo.modelo}\n")
            archivo.write(f"Numero de serie: {dispositivo.numero_serie}\n")
            archivo.write(f"Consumo de energia: {dispositivo.consumo_energia}\n")
            archivo.write(f"Estado: {dispositivo.estado}\n")
            archivo.write(f"Wi-Fi: {dispositivo.wifi}\n")
            archivo.write(f"Bluetooth: {dispositivo.bluetooth}\n")
            archivo.write(f"Direccion IP: {dispositivo.direccion_ip}\n")
            archivo.write(f"Nombre de red: {dispositivo.nombre_red}\n")
            archivo.write(f"Estado de conexion: {dispositivo.estado_conexion}\n")
    

def main():
    path = os.path.join(os.path.dirname(__file__), "dispositivos.txt")
    dispositivos = [
        TelevisorInteligente("Samsung", "QLED", "TV001", 120),
        ParlanteInteligente("JBL", "Flip", "PA001", 30),
        BombilloInteligente("Philips", "Hue", "BO001", 10),
        CamaraSeguridad("Xiaomi", "C200", "CA001", 15),
        TermostatoInteligente("Google", "Nest", "TE001", 25)
    ]

    for dispositivo in dispositivos:
        print("\n-------------------------")
        dispositivo.mostrar_informacion()
        dispositivo.mostrar_conexion()


    guardar_datos(path, dispositivos)

if __name__ == "__main__":
    main()