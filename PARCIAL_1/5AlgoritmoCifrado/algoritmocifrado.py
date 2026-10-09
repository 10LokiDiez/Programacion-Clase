"""
5. Implementar el algoritmo de cifrado y descifrado cesar haciendo uso de
POO, archivos y listas.
Para este algoritmo se deja documentación en la sección de “Parcial I”.

"""
class CesarCifDes:
    abclist = ["a", "b", "c", "d", "e", "f",
               "g", "h", "i", "j", "k", "l",
               "m", "n", "o", "p", "q", "r",
               "s", "t", "u", "v", "w", "x",
               "y", "z"]
    
    #estado "normal", "codificado"
    def __init__(self,palabra,llave,estado):
        self.palabra = palabra
        self.llave = llave
        self.estado = estado
    
    def cifrado(self, path_file):
        enclist = self.abclist.copy()
        for _ in range(self.llave):
            last = enclist.pop()
            enclist.insert(0, last)
        palabra = ""
        
        if self.estado == "normal":
            for c in self.palabra:
                index_normal = self.abclist.index(c)
                word_enc = enclist[index_normal]
                palabra +=  word_enc
        else:
            for c in self.palabra:
                index_enc = enclist.index(c)
                word_norm = self.abclist[index_enc]
                palabra += word_norm
                
        with open(path_file, "a", encoding="utf-8") as file:
            if self.estado == "normal":
                file.write(f"Palabra: {self.palabra}, Llave(K): {self.llave}, Cifrado: {palabra}\n")
            else:
                file.write(f"Palabra: {self.palabra}, Llave(K): {self.llave}, Descifrado: {palabra}\n")
        return palabra
            
def leerArchivo(path_file):
    with open(path_file, "r", encoding="utf-8") as file:
        lineas = file.readlines()
    for linea in lineas:
        print(linea)

def main():
    path_file = "c:\\Users\\sidim\\Escritorio\\universidad\\Programacion Clase\\PARCIAL_1\\5AlgoritmoCifrado\\encriptados.txt"
    op = input("Quiere seguir escribiendo en el archivo?(s/n): ").lower()
    if op != "s":
        with open(path_file, "w") as file:
            pass
    while True:
        print("-" * 50)
        print("1. Cifrar - Descifrar Palabra")
        print("2. Ver Palabras Cifradas y Descifradas")
        print("3. Salir")
        opcion = int(input("Ingresa la opcion que desea: "))
        match opcion:
            case 1:
                palabra = input("Escriba la palabra que quiere Cifrar o Descifrar: ").lower()
                llave = int(input("Que llave quiere utiliza (numero): "))
                print("1. Cifrar")
                print("2. Descifrar")
                estado = int(input("La quiere Cifrar o Descifrar, escriba 1 o 2: "))
                if estado == 1:
                    nueva_palabra = CesarCifDes(palabra, llave, "normal")
                else:
                    nueva_palabra = CesarCifDes(palabra, llave, "codificado")
                
                new =nueva_palabra.cifrado(path_file)
                print(f"Palabra = {new}")
                    
            case 2:
                leerArchivo(path_file)
                
            case 3:
                print("Saliendo del programa...")
                break
            case _:
                print("Dato no valido, vuelve a intentarlo")
                

main()