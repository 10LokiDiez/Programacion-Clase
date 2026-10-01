"""
7. Diseñe una clase `AgendaContactos` con atributos como nombre, teléfono, correo y
dirección. Agregue métodos para buscar contactos, eliminar contactos y actualizar
información desde y hacia un archivo.

"""
import os

class AgendaContactos:
    def __init__(self, nombre, telefono, correo, direccion):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion
    
    def agregarCont(self, file_path):
        with open(file_path, "a", encoding="utf-8") as file:
            file.write(f"{self.nombre},{self.telefono},{self.correo},{self.direccion}\n")
          
    @staticmethod  
    def buscarCont(file_path,nom):
        if not os.path.exists(file_path):
            print("El archivo aún no existe.")
            return
        
        with open(file_path, "r", encoding="utf-8") as file:
            lineas = file.readlines()
            for contacto in lineas:
                if contacto.strip():
                    nombre,telefono,correo,direccion = contacto.strip().split(',')
                    if nombre.lower() == nom.lower():
                        print(f"Dato encontrado: {nombre}, {telefono}, {correo}, {direccion}")
                        return
    
    @staticmethod  
    def elimCont(file_path,file_path_copy,nom):
        if not os.path.exists(file_path):
            return
        copiar(file_path, file_path_copy)
        os.remove(file_path)
        eliminado = False
        with open(file_path_copy, "r", encoding="utf-8") as file:
            lineas = file.readlines()
            for contacto in lineas:
                if contacto.strip():
                    nombre,telefono,correo,direccion = contacto.strip().split(',')
                    if nombre.lower() != nom.lower():
                        with open(file_path, "a", encoding="utf-8") as file2:
                            file2.write(f"{nombre},{telefono},{correo},{direccion}\n")
                    else:
                        eliminado = True
                        print(f"Has eliminado a {nombre} Exitosamente")
                    
        if not eliminado:
            print(f"No se encontro el contacto '{nom}' para eliminar.")
        os.remove(file_path_copy)

    @staticmethod
    def actualizarCont(file_path, file_path_copy, nom, nuevo_tel, nuevo_correo, nueva_dir):
        if not os.path.exists(file_path):
            return
        
        copiar(file_path, file_path_copy)
        os.remove(file_path)
        editado = False
        with open(file_path_copy, "r", encoding="utf-8") as file:
            lineas = file.readlines()
            for contacto in lineas:
                if contacto.strip():
                    nombre,telefono,correo,direccion = contacto.strip().split(',')
                    with open(file_path, "a", encoding="utf-8") as file2:
                        if nombre.lower() != nom.lower():
                                file2.write(f"{nombre},{telefono},{correo},{direccion}\n")
                        else:
                            editado = True
                            file2.write(f"{nombre},{nuevo_tel},{nuevo_correo},{nueva_dir}\n")
                            print(f"Has editado a {nombre} Exitosamente")
                            
        if not editado:
            print(f"No se encontro el contacto '{nom}' para editar.")
        os.remove(file_path_copy)
        
                  
def copiar(origen, destino):
    with open(origen, 'r', encoding='utf-8') as f_origen:
        contenido = f_origen.read()

    with open(destino, 'w', encoding='utf-8') as f_destino:
        f_destino.write(contenido)


def main():
    file_path = os.path.join(os.path.dirname(__file__), "contactos.txt")
    file_path_copy = os.path.join(os.path.dirname(__file__), "contactos_copy.txt")
    open(file_path, "w", encoding="utf-8").close()
    contacto1 = AgendaContactos("Laura Gomez", "3001234567", "laura@gmail.com", "Calle 10 #4-20")
    contacto2 = AgendaContactos("Carlos Ruiz", "3159876543", "carlos@hotmail.com", "Cra 15 #8-45")
    contacto3 = AgendaContactos("Ana Martinez", "3204567890", "ana@gmail.com", "Av Central #10-02")
    contactos = [contacto1,contacto2,contacto3]
    for contacto in contactos:
        contacto.agregarCont(file_path)
    AgendaContactos.buscarCont(file_path, "Carlos Ruiz")
    AgendaContactos.elimCont(file_path,file_path_copy,"Laura Gomez")
    AgendaContactos.actualizarCont(file_path,file_path_copy,"Ana Martinez","3005688499", "anita@gmail.com", "Av Central #93-02")

if __name__ == "__main__":
    main()