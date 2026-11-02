from crearobjetos import crear_objetos

def catalogar(lista, ruedas=None):
    if ruedas == None:
        for obj in lista:
            print(obj)
    else:
        count = 0
        for obj in lista:
            if obj.get_numllantas() == ruedas:
                print(obj)
                count += 1
        print(f"Se han encontrado {count} vehículos con {ruedas} ruedas:")

def main():
    vehiculos = crear_objetos()
    
    print("\nCATALOGO NORMAL")
    catalogar(vehiculos)
    
    print("\nCATALOGO CON RUEDAS")
    catalogar(vehiculos, 4)

    print("\nMODIFICANDO ATRIBUTOS VÍA MÉTODOS SET:")
    vehiculos[0].set_color("Verde")
    print(f"Nuevo color del coche: {vehiculos[0].get_color()}")

if __name__ == "__main__":
    main()