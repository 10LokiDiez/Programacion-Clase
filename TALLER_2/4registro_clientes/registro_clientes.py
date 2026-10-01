"""
4. Registro de clientes
- Crea una clase `Cliente` con al menos 5 atributos (id, nombre, edad, ciudad, saldo).
- Implemente un método que guarde los clientes en `clientes.txt`.
- Otro método que lea el archivo y muestre solo los clientes con saldo negativo.
"""
import os

class Cliente:
    id = 0
    def __init__(self, nombre, edad, ciudad, saldo):
        Cliente.id += 1
        self.id = Cliente.id
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad
        self.saldo = saldo

    def guardar_cliente(self):
        path_file = os.path.join(os.path.dirname(__file__), "clientes.txt")
        
        with open(path_file, "a") as file:
            file.write(f"{self.id},{self.nombre},{self.edad},{self.ciudad},{self.saldo}\n")
            
            
    @staticmethod
    def leer_saldo_negativo():
        path_file = os.path.join(os.path.dirname(__file__), "clientes.txt")
        
        with open(path_file, "r") as file:
            texto = file.read()
            for linea in texto.split("\n"):
                if not linea:
                    continue
                if float((linea.split(","))[4]) <0:
                    print(linea)
def verificar_archivo():
    if os.path.exists(os.path.join(os.path.dirname(__file__), "clientes.txt")):
        os.remove(os.path.join(os.path.dirname(__file__), "clientes.txt")) 
            
def main():
    lista_de_clientes = [
        Cliente("Simon", 28, "Cali", -150000.0),
        Cliente("Andrea", 32, "Medellin", 500000.0),
        Cliente("Carlos", 22, "Bogota", -45000.5),
        Cliente("Mariana", 40, "Pereira", 1200000.0)
    ]
    verificar_archivo()
    for cliente in lista_de_clientes:
        cliente.guardar_cliente()
        
    Cliente.leer_saldo_negativo()

if __name__ == "__main__":
    main()