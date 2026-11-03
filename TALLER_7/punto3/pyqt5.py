import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class VentanaPrincipal(QWidget): # Aquí toca meter todo en una clase
    def __init__(self):
        super().__init__() # Inicializo la ventana padre
        self.setWindowTitle("Interfaz PyQt5")
        self.resize(300, 150) # Igual que geometry, pero con dos números
        
        layout = QVBoxLayout() # Esto organiza los elementos de arriba hacia abajo automáticamente
        
        self.label = QLabel("Ingresa tu nombre:") # Texto fijo
        layout.addWidget(self.label) # Lo meto al organizador
        
        self.entrada = QLineEdit() # La cajita de texto 
        layout.addWidget(self.entrada)
        
        self.boton = QPushButton("Ejecutar")
        self.boton.clicked.connect(self.saludar) # Así se conecta el clic a la función (sin parentesis al final)
        layout.addWidget(self.boton)
        
        self.resultado = QLabel("")
        layout.addWidget(self.resultado)
        
        self.setLayout(layout) # Finalmente le aplico el organizador a la ventana

    def saludar(self):
        # En vez de .get() y .config(), aquí uso .text() y .setText()
        self.resultado.setText(f"Bienvenido, {self.entrada.text()}!")

app = QApplication(sys.argv) # Obligatorio para inicializar los procesos de PyQt
ventana = VentanaPrincipal()
ventana.show() 
sys.exit(app.exec_()) 