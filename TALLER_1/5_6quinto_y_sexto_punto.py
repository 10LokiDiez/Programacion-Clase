"""
5. Realice un programa que almacene una cantidad de cadenas
dictaminadas por el usuario, en pantalla se debe mostrar la
cadena que más caracteres contenga y la cadena que menos
caracteres contenga.
Ejemplo:
Lista= [“oso”, “casa”, “murciélago”, “ventana”, “programación”]
Cadena mayor = programación.
Cadena menor = oso
"""

num_cadenas = int(input("Ingrese cuanta cantadad de cadenas quiere en la lista: "))
lista= [input(f"Ingrese la cadena {i+1}: ") for i in range(num_cadenas)]
print(lista)
min_cadena=lista[0]
max_cadena=""
for cadena in lista:
    if len(cadena) > len(max_cadena):
        max_cadena = cadena
    if len(cadena) < len(min_cadena):
            min_cadena = cadena
            
print(f"Cadena mayor = {max_cadena}")
print(f"Cadena menor = {min_cadena}")

"""
6. Realice un programa en el que el usuario ingrese un valor
entero, luego debe mostrar en pantalla las cadenas cuya longitud
sea igual al número ingresado, puede usar la lista del ejercicio 5
o 7.
"""
lennum = int(input("Ingrese la longitud de las cadenas que quiera usar: "))
for cadena in lista:
    if len(cadena) == lennum:
        print(cadena)
    