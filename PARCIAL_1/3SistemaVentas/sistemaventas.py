"""
3. Sistema de Ventas de Productos con Inventario
Crea un sistema de ventas que gestione productos y clientes. El sistema
debe llevar control de los productos en inventario y de las ventas
realizadas, Para ello, crea las siguientes clases:
Nota importante: para este ejercicio debe implementar archivos XML, la
documentación quedará adjunta en la actividad de “parcial I”.
"""
"""
Clase Producto:
• Atributos:
o Nombre (cadena de texto)
o ID (entero)
o Precio (flotante)
o Cantidad en inventario (entero)
• Métodos:
o Constructor para inicializar todos los atributos.
o disminuir_inventario(cantidad: int): Disminuye la cantidad del inventario al realizar una venta.
o aumentar_inventario(cantidad: int): Aumenta la cantidad del inventario al reponer stock.
o mostrar_informacion(): Muestra la información del producto en formato legible.
"""
import xml.etree.ElementTree as ET
class Producto:
    def __init__(self, id, nombre, precio, cantidadinv):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.cantidadinv = cantidadinv
        
    def disminuir_inventario(self, cantidad):
        self.cantidadinv -= cantidad
        
    def aumentar_inventario(self, cantidad):
        self.cantidadinv += cantidad
        
    def mostrar_informacion(self):
        print(f"ID del Producto: {self.id}, Nombre: {self.nombre}, Precio: {self.precio:.2f}, Cantidad: {self.cantidadinv}")
        
        
"""
Clase Cliente:
• Atributos:
o Nombre (cadena de texto)
o ID (entero)
o Saldo (flotante)

• Métodos:
o Constructor para inicializar los atributos.
o realizar_compra(producto: Producto, cantidad: int): Reduce el
saldo del cliente y reduce la cantidad en inventario del producto,
siempre que el saldo y el stock lo permitan.
o mostrar_informacion(): Muestra la información del cliente en
formato legible.
"""
class Cliente:
    def __init__(self, id, nombre, saldo):
        self.id = id
        self.nombre = nombre
        self.saldo = saldo
        
    def realizar_compra(self, producto, cantidad):
        if producto.cantidadinv < cantidad:
            print("No hay suficiente Stock de este producto...")
        elif self.saldo < (producto.precio * cantidad):
            print(f"{self.nombre} no tiene saldo suficiente para esta compra")
        else:
            producto.disminuir_inventario(cantidad)
            self.saldo -= (producto.precio * cantidad)
            print("Se ha realizado la compra con exito")
            
    
    def mostrar_informacion(self):
        print(f"ID del Cliente: {self.id}, Nombre: {self.nombre}, Saldo: {self.saldo:.2f}")
        
"""
Clase Tienda:
• Atributos:
o Una lista de productos disponibles.
o Una lista de clientes registrados.
• Métodos:
o agregar_producto(producto: Producto): Agrega un nuevo producto
a la lista de productos.
o agregar_cliente(cliente: Cliente): Agrega un cliente a la lista de
clientes.
o realizar_venta(id_cliente: int, id_producto: int, cantidad: int):
Realiza una venta de un producto a un cliente si se cumplen las
condiciones de stock y saldo.
o mostrar_productos(): Muestra todos los productos disponibles.
o mostrar_clientes(): Muestra todos los clientes registrados.
o guardar_datos(archivo: str): Guarda los productos y clientes en un
archivo.
o cargar_datos(archivo: str): Carga los productos y clientes desde
un archivo.
"""
class Tienda:
    def __init__(self):
        self.listapro = []
        self.listacli = []
        
    def agregar_producto(self, producto):
        self.listapro.append(producto)
        
    def agregar_cliente(self, cliente):
        self.listacli.append(cliente)
        
    def realiza_venta(self, idcliente, idproducto, cantidad):
        clientef = None
        productof = None
        for cliente in self.listacli:
            if cliente.id == idcliente:
                clientef = cliente
                break
            
        if clientef == None:                
            print("No se encontro el Cliente")
            return
        
        for producto in self.listapro:
            if producto.id == idproducto:
                productof = producto
                break
            
        if productof == None:                
            print("No se encontro el Producto")
            return
            
        clientef.realizar_compra(productof,cantidad)              
    
    def mostrar_productos(self):
        for producto in self.listapro:
            if producto.cantidadinv != 0:
                producto.mostrar_informacion()
                
    def mostrar_clientes(self):
        for cliente in self.listacli:
            cliente.mostrar_informacion()            

    def guardar_datos(self, path):
        root = ET.Element("Tienda")
        
        #(self, id, nombre, saldo)
        for cli in self.listacli:
            cliente = ET.SubElement(root, "Cliente")
            cliente.set("id",str(cli.id))
            nombre = ET.SubElement(cliente, "Nombre")
            nombre.text = cli.nombre
            saldo = ET.SubElement(cliente, "Saldo")
            saldo.text = str(cli.saldo)
        
        #(self, id, nombre, precio, cantidadinv)
        for pro in self.listapro:
            producto = ET.SubElement(root, "Producto")
            producto.set("id",str(pro.id))
            nombre = ET.SubElement(producto, "Nombre")
            nombre.text = pro.nombre
            precio = ET.SubElement(producto, "Precio")
            precio.text = str(pro.precio)
            cantidad = ET.SubElement(producto, "Cantidad")
            cantidad.text = str(pro.cantidadinv)
            
        tree = ET.ElementTree(root)
        tree.write(path,encoding="utf-8",xml_declaration=True)
        print("Archivo creado con exito")
        
    def cargar_datos(self, path):
        tree = ET.parse(path)
        
        root = tree.getroot()
        
        for cliente in root.findall('Cliente'):
            id_cli = cliente.get('id')
            nombre = cliente.find('Nombre')
            saldo = cliente.find('Saldo')
            self.agregar_cliente(Cliente(int(id_cli), nombre.text, float(saldo.text)))
            
        for producto in root.findall('Producto'):
            id_pro = producto.get('id')
            nombre = producto.find('Nombre')
            precio = producto.find('Precio')
            cantidad = producto.find('Cantidad')
            self.agregar_producto(Producto(int(id_pro), nombre.text, float(precio.text), int(cantidad.text)))
            
            
            
def menu(path_file):
    print("----- BIENVENIDO AL SISTEMA DE VENTAS -----")
    tienda = Tienda()
    ca = input("Le recomendamos antes de empezar cargar el inventario creado en el archivo (s/n): ").lower()    
    if ca == "s":
        tienda.cargar_datos(path_file)
    while True:
        print("-" * 50)
        print("1. Agregar Producto")
        print("2. Agregar Cliente")
        print("3. Realizar Venta")
        print("4. Ver Clientes y Productos")
        print("5. Salir del Programa")
        opcion = int(input("Ingresa la opcion que desea: "))
        
        if  1 <= opcion <= 5:
            print("Dato Valido")
        else:
            print("Dato Erroneo")
            continue
        match opcion:
            case 1:
                print("------ AGREGAR PRODUCTO ------")
                found = 0
                id_prod = int(input("ID del producto: "))
                for producto in tienda.listapro:
                    if producto.id == id_prod:
                        producto_encontrado = producto
                        found = 1
                        break
                if found == 0:
                    nombre = input("Nombre del producto: ")
                    precio = float(input("Precio: "))
                    cant = int(input("Cantidad en inventario: "))
                    nuevo_producto = Producto(id_prod, nombre, precio, cant)
                    tienda.agregar_producto(nuevo_producto)
                    print("Producto agregado con exito.")
                else:
                    print(f"El producto {producto_encontrado.nombre} ya existe en el sistema.")
                    cant_extra = int(input("Ingrese la cantidad a agregar al stock: "))
                    producto_encontrado.aumentar_inventario(cant_extra)
                    print("Stock actualizado con exito.")
                tienda.guardar_datos(path_file)
                    
            case 2:
                print("------ AGREGAR CLIENTE ------")
                found = 0
                id_cli = int(input("ID del cliente: "))
                for cliente in tienda.listacli:
                    if cliente.id == id_cli:
                        found = 1
                        break
                
                if found == 0:
                    nombre = input("Nombre del cliente: ")
                    saldo = float(input("Saldo inicial: "))
                    
                    nuevo_cliente = Cliente(id_cli, nombre, saldo)
                    tienda.agregar_cliente(nuevo_cliente)
                    print("Cliente agregado con exito.")
                    tienda.guardar_datos(path_file)
                else:
                    print("El ID YA EXISTE")
                
            case 3:
                print("------ REALIZAR VENTA ------")
                id_cli = int(input("ID del Cliente que compra: "))
                id_prod = int(input("ID del Producto a comprar: "))
                cant = int(input("Cantidad a comprar: "))
                tienda.realiza_venta(id_cli, id_prod, cant)
                tienda.guardar_datos(path_file)
                
            case 4:
                print("------ VER CLIENTES Y PRODUCTOS ------")
                print("\n--- PRODUCTOS ---")
                tienda.mostrar_productos()
                print("\n--- CLIENTES ---")
                tienda.mostrar_clientes()
                
            case 5:
                print("Guardando datos y saliendo del programa...")
                tienda.guardar_datos(path_file)
                break            
            
def main():
    path= "c:\\Users\\sidim\\Escritorio\\universidad\\Programacion Clase\\PARCIAL_1\\3SistemaVentas\\inventario.xml"
    menu(path)


main()
