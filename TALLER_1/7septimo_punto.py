"""
7. Realizar un programa que pida al usuario un carácter, luego se
debe mostrar las cadenas que contengan dicho carácter y debe
mostrar si dichas cadenas son pares o impares.
Lista= [“oso”, “casa”, “murciélago”, “ventana”, “programación”,” objetos”, “listas”, “métodos”, “utp”]
"""
lista = ["oso", "casa", "murciélago", "ventana", "programación", "objetos", "listas", "métodos", "utp"]
let = input("Ingrese un caracter, el cual quiera buscar: ")

for cadena in lista:
    if cadena.count(let) > 0:
        print(f"{cadena} ", end="")
        if len(cadena) % 2 ==0:
            print("y es par")
        else:
            print("y es impar")