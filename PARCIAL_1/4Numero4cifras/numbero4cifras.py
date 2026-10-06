"""
Diseñe un programa que reciba un numero entero de 4 cifras, diga si el
primer número es múltiplo del cuarto número y debe mostrar la suma del
segundo número y el tercero (no requiere implementar el paradigma
orientado a objetos), este punto se debe hacer usando operaciones
aritméticas para descomponer el numero de 4 cifras.

"""


def main():
    while True:
        num = int(input("Ingrese un numero de 4 cifras: "))
        if 10000 > num >= 1000:
            break
        else:
            print("Numero erroneo")
            continue
    d1 = num // 1000
    d2 = (num // 100) % 10
    d3 = (num // 10) % 10
    d4 = num % 10
    if d4 == 0:
        print("El cuarto numero es 0 por ende no se puede calcular si es multiplo o no")
    elif d1 % d4 == 0:
        print("El primer número es múltiplo del cuarto número")
    else:
        print("El primer número NO es múltiplo del cuarto número")
        
    print(f"La suma del digito 2 y 3 es: {d2 +d3}")
    
main()