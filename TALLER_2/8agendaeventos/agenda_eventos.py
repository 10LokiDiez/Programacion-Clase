"""
8. Agenda de eventos
- Crea una clase `Evento` con atributos: título, fecha, hora, lugar y responsable.
- Permita registrar varios eventos y guardarlos en `agenda.txt`.
- Implemente un método que lea el archivo y muestre solo los eventos programados
para la próxima semana.
"""
import os
from datetime import datetime, timedelta

class Evento:
    id = 0
    def __init__(self, titulo, fecha, hora, lugar, responsable):
        Evento.id += 1
        self.id = Evento.id
        self.titulo = titulo
        self.fecha = fecha  # Formato YYYY-MM-DD
        self.hora = hora
        self.lugar = lugar
        self.responsable = responsable

    def guardar_agenda(self, path_file):
        with open(path_file, "a") as file:
            file.write(f"{self.id},{self.titulo},{self.fecha},{self.hora},{self.lugar},{self.responsable}\n")

    @staticmethod
    def leer_proxima_semana(path_file):
        hoy = datetime.now().date()
        proxima_semana = hoy + timedelta(days=7)

        print("--- EVENTOS PROXIMA SEMANA ---")
        with open(path_file, "r") as file:
            text = file.read()
            for linea in text.split("\n"):
                if not linea:
                    continue
                codigo, titulo, fecha_str, hora, lugar, responsable = linea.split(",")
                fecha_evento = datetime.strptime(fecha_str, "%Y-%m-%d").date()

                if hoy <= fecha_evento <= proxima_semana:
                    print(f"ID: {codigo} | Titulo: {titulo} | Fecha: {fecha_str} | Hora: {hora} | Lugar: {lugar} | Resp: {responsable}")


def verificar_archivo(path_file):
    if os.path.exists(path_file):
        os.remove(path_file)


def main():
    path_file = os.path.join(os.path.dirname(__file__), "agenda.txt")

    # Fechas dinámicas para pruebas reales de la próxima semana
    hoy = datetime.now().date()

    lista_eventos = [
        Evento("Reunion de Equipo", str(hoy + timedelta(days=2)), "09:00", "Sala A", "Carlos"),
        Evento("Presentacion Proyecto", str(hoy + timedelta(days=5)), "14:00", "Auditorio", "Ana"),
        Evento("Taller Python", str(hoy + timedelta(days=10)), "11:00", "Lab 2", "Simon"),
        Evento("Revision Trimestral", str(hoy + timedelta(days=15)), "16:00", "Sala B", "Mariana")
    ]

    verificar_archivo(path_file)

    for evento in lista_eventos:
        evento.guardar_agenda(path_file)

    Evento.leer_proxima_semana(path_file)


if __name__ == '__main__':
    main()