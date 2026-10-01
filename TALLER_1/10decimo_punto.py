"""
10. Elabore un programa para ingresar la siguiente lista.
Lista= [“casa”, “programación”, “utp”, “universidad”, “utp, “casa”,
“casa”,” thj”, “vbh”, “456”, “987”]
a. Borre los elementos repetidos que tengamos en la lista
b. Borre las cadenas que NO contengan vocales.
c. Ordene la lista en orden alfabético respecto al primer
elemento de la cadena.
"""
def imprimirlista(lista):
    for pal in lista:
        print(f"{pal} ", end="")
    print("\n\n")
        
Lista = ["casa", "programación", "utp", "universidad", "utp", "casa",
         "casa", "thj", "vbh", "456", "987"]
print("LISTA INICIAL")
imprimirlista(Lista)

Lista = list(set(Lista))

print("LISTA SIN REPETIDOS")
imprimirlista(Lista)
Listacop = []
for let in Lista:
    tiene_vocal = False
    
    for car in let:
        if car in "aeiouáéíóú":
            tiene_vocal = True
            
    if tiene_vocal:
        Listacop.append(let)
        
Lista = Listacop

print("LISTA SIN CADENAS SIN VOCALES")
imprimirlista(Lista)

Lista.sort()
print("LISTA EN ORDEN")
imprimirlista(Lista)