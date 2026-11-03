import tkinter as tk

def saludar():
    # Saco el texto de la cajita con .get() y lo meto en la etiqueta
    etiqueta.config(text=f"Bienvenido, {entrada.get()}!")
    

ventana = tk.Tk() # Aquí creo la ventana base
ventana.geometry("300x150") 
ventana.title("Interfaz Tkinter") # El título de arriba

# Creo un texto fijo y .pack() lo acomoda ahí mismo
tk.Label(ventana, text="Ingresa tu nombre:").pack(pady=5)

entrada = tk.Entry(ventana) # Esta es la cajita donde uno escribe
entrada.pack(pady=5) # Le doy un margen de 5px

# El command sirve para enlazar el clic a mi función de arriba
tk.Button(ventana, text="Ejecutar", command=saludar).pack(pady=5)

etiqueta = tk.Label(ventana, text="") # Etiqueta vacía para llenarla después
etiqueta.pack(pady=5)

ventana.mainloop() # Este es el bucle infinito para que la ventana no se desaparezca al instante