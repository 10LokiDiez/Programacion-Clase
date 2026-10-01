"""
3. Escribir un programa que almacene las asignaturas de un
curso en una lista, pida al usuario las 4 notas de cada
materia y en pantalla mostrar el promedio que ha sacado 
en cada materia y si alguna materia queda por debajo de 
la nota 3 debe salir en pantalla “asignatura perdida”, 
luego se deben calcular el promedio general de todas las 
materias si el promedio está por debajo de 3 debe imprimir
“semestre perdido”, si esta entre 3 y 4 debe imprimir “buen 
trabajo”, si el promedio esta entre 4 y 5 debe imprimir 
“felicidades serás becado”.

Salida de datos:

Matemáticas - nota1: 2, nota2: 2, nota3: 2, nota 4: 2
Promedio de matemáticas: 2 - asignatura perdida

Inglés - nota1: 3, nota2: 3, nota3: 3, nota 4: 3
Promedio de matemáticas: 3 - asignatura ganada

Promedio general: 2.5 - “Semestre perdido
”"""

# Permite al usuario agregar materias hasta que ingrese 0
def asignacion_materias(materias):

    while True:

        materia = input("Ingrese la materia que quiere agregar (0 para salir): ")

        if materia == "0":

            # Muestra la cantidad de materias ingresadas
            print(f"Ingresaste {len(materias)} materias")
            print("Vamos con las notas...")

            break
        else:
            materias.append(materia)


# Pide las 4 notas de cada materia
def asignacion_notas(materias, todas_notas):
    notas = []

    for materia in materias:

        print(f"INGRESE LAS NOTAS DE {materia}")

        # Limpia las notas anteriores para ingresar las de la nueva materia
        notas.clear()

        for i in range(1,5):

            while True:

                nota = float(input(f"Cual es la nota {i} de (0 a 5): "))

                # Verifica que la nota esté entre 0 y 5
                if nota >= 0 and nota <= 5:
                    notas.append(nota)
                    break
                else:
                    print("Vuelva a ingresar la nota")

        print()

        # Guarda una copia de las notas de la materia
        todas_notas.append(notas.copy())


# Calcula los promedios y muestra los resultados
def resultados(materias, todas_notas):

    print("ESTOS SON TUS RESULTADOS")
    sum_prom_fin = 0

    for materia in materias:

        suma = 0

        print(f"Materia {materia}:")

        # Muestra y suma las 4 notas
        for i in range(0,4):

            print(todas_notas[materias.index(materia)][i])

            suma += todas_notas[materias.index(materia)][i]

        # Calcula el promedio de la materia
        prom = suma/4

        imprimir_prom_materias(materia, prom)

        # Acumula los promedios para calcular el general
        sum_prom_fin += prom

    # Calcula el promedio general
    promedio_gen = sum_prom_fin/len(materias)

    print(f"Promedio general: {promedio_gen}")

    # Determina si se ganó o perdió el semestre
    if promedio_gen < 3:
        print("Semestre perdido")
    else:
        print("Semestre ganado")


# Muestra el promedio y el resultado de cada materia
def imprimir_prom_materias(materia, prom):

    print(f"El promedio de {materia} es: {prom},", end=" ")

    if prom < 3:
        print("Asignatura perdida", end="\n\n")

    elif prom >= 3 and prom <4:
        print("Buen trabajo", end="\n\n")

    else:
        print("Felicidades seras becado", end="\n\n")


# Función principal del programa
def main():

    materias =[]

    # Solicita las materias
    asignacion_materias(materias)

    todas_notas=[]

    # Solicita las notas
    asignacion_notas(materias, todas_notas)

    # Muestra los resultados finales
    resultados(materias, todas_notas)


# Inicia el programa
if __name__ == '__main__':
    main()