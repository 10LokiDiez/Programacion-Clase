"""
5. Cree una clase `Encuesta` que almacene respuestas de usuarios (edad, género,
ciudad, opinión). Guarde cada respuesta en un archivo distinto por ciudad. Muestre
estadísticas por género.
"""
import os
class Encuesta:
    
    def __init__(self,edad,genero,ciudad,opinion):
        self.edad = edad
        self.genero = genero
        self.ciudad = ciudad
        self.opinion = opinion
        
    def guardarArchivo(self):
        path_f=os.path.join(os.path.dirname(__file__), f"{self.ciudad.capitalize()+".txt"}")
        
        with open(path_f, "a", encoding="utf-8") as file:
            file.write(f"Edad: {self.edad} Genero: {self.genero} Ciudad: {self.ciudad} Opinion: {self.opinion}\n")
            
        print(f"Respuesta guardada en el archivo: {path_f}")
        
    @staticmethod
    def estadisGen(lista):
        total_respuesta = len(lista)
        conteo ={}
        for encuesta in lista:
            conteo[encuesta.genero] =conteo.get(encuesta.genero, 0) + 1
            
        for genero, cantidad in conteo.items():
            print(f"- {genero}:{cantidad} respuestas ({(cantidad / total_respuesta) * 100:.1f} %)")
            
        
def main():
    encuestas_recolectadas = [
        Encuesta(25, "Femenino", "Pereira", "Excelente servicio"),
        Encuesta(34, "Masculino", "Bogota", "Puede mejorar en los tiempos"),
        Encuesta(28, "Femenino", "Pereira", "Me gustó mucho la atención"),
        Encuesta(45, "Masculino", "Medellin", "Todo correcto"),
        Encuesta(22, "Masculino", "Pereira", "Precios muy altos")
    ]
    for encuenta in encuestas_recolectadas:
        encuenta.guardarArchivo()
    
    Encuesta.estadisGen(encuestas_recolectadas)
    
    
if __name__ == "__main__":
    main()
    
