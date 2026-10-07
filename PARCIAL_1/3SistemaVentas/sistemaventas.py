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

