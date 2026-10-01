"""
2. Dada la siguiente lista: 
palabras = ["Hola", "mundo", "esto", "es","Python"]
Una todas las palabras de la lista en una sola cadena
separadaspor espacio o algún carácter especial.
"""

palabras = ["Hola", "mundo", "esto", "es","Python"]
new_word = ""
for palabra in palabras:
    new_word += palabra + " "
    
print(new_word)