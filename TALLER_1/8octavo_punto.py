"""
8. Realizar un programa que haga conteo de todos los caracteres
que no sean vocales en una lista de 10 cadenas.
"""

lista = ["oso", "casa", "murciélago", "ventana", "programación", "objetos", "listas", "métodos", "utp", "computador"]
cout = 0
for let in lista:
    for car in let:
        if car not in "aeiouáéíóú":
            cout += 1
        
print(f"Hay {cout} que no son vocales")