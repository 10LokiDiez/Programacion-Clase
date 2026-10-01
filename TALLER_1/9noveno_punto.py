"""
9. Realizar un programa que inicialice una lista con 15 valores
aleatorios y posteriormente muestre en pantalla cada elemento
de la lista junto con su cuadrado y su cubo.
"""

import random

lista =[random.randint(1,100) for _ in range(0,15)]

print (f"La lista de numeros es: \n{lista}")
print("\nRESULTADOS:")
for num in lista:
    print(f"{num} - {num**2} - {num**3}")