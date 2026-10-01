"""
4. Escriba un programa que pida al usuario la cantidad que desea
de la lista, luego el usuario debe ingresar valores numéricos
enteros hasta llenar la lista, luego de ingresarlos se debe
imprimir en pantalla cada número ingresado por el usuario y al
lado debe aparecer ese mismo número al cuadrado y al lado ese
mismo número al cubo, ejemplo:
L = [2,3]
Salida:
2 - 4 - 8
3 - 9 - 27
"""
cantidad_de_numeros = int(input("Ingrese cuantos numeros desea en la lista: "))
lista= [int(input(f"Ingrese en numero {i+1}: ")) for i in range(cantidad_de_numeros)]

for num in lista:
    print (f"{num} - {num**2} - {num**3}")