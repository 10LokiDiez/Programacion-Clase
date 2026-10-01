
"""
1. Realice un algoritmo para sumar los valores numéricos de la
siguiente lista sin ordenarla:Lista= [2, 8,” hola”, 
“programación”, 10, “utp”, 85, 82, 100,”
mundo”]
"""
Lista= [2, 8, "hola", "programación", 10, "utp", 85, 82, 100,"mundo"]
sum = 0
for dig in Lista:
    if isinstance(dig, int):
        sum += dig
        
print(sum)
