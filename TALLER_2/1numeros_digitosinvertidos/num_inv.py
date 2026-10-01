import os
"""
1. Números y dígitos invertidos
- Crear una clase `Numero` donde pueda tener un entero de tres cifras.
- Implemente un método que devuelva la suma de sus dígitos.
- Implemente otro método que escriba en `numeros.txt` el número original y su versión
invertida.
- Leer el archivo e imprimir los resultados.
"""
class Numero:
    
    def __init__(self,num):
        self.num = num

    def suma_digitos(self):
        total = 0
        for dig in str(self.num):
            total += int(dig)
        return total
    
    def guardar_original_invertido(self):
        path_file = os.path.join(os.path.dirname(__file__), "numeros.txt")
        new_num = str(self.num)
        
        with open(path_file, "w") as file:
            file.write(f"{new_num}\n")
            for dig in reversed(new_num):
                file.write(dig)
                
        with open(path_file, "r") as file:
            text= file.read()
            print(text)
        

    
def main():
    while True:
        try:
            num = int(input("Ingrese un entero de tres cifras: "))
            if num >99 and num<1000:
                break
            else:
                print("Este numero no esta en el rango")
        except ValueError:
            print("Tipo de dato erroneo")
            
    numero1 = Numero(num)
    print(f"La suma de sus digitos es: {numero1.suma_digitos()}")
    
    numero1.guardar_original_invertido()

if __name__ == "__main__":
    main()