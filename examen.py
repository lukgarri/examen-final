import random
import csv
import statistics

trabajadores = ["Juan Perez", "Maria Garcia", "Carlos Lopez", "Ana Martinez", "Pedro Rodriguez", "Laura Hernandez", "Miguel Sanchez","Isabel Gomez","Francisco Diaz","Elena Fernández"]

# Funcion para generar sueldos aleatorios
def generar_sueldos_aleatorios():
    sueldos = {}
    for trabajador in trabajadores:
        sueldos[trabajador] = random.randint(300000, 2500000)
    return sueldos

# Funcion para clasificar sueldos
def clasificar_sueldos(sueldos):
    print("\n-- CLASIFICACION DE SUELDOS -- \n")
    for trabajador, sueldo in sueldos.items():
        if sueldo < 800000:
            print("\nSueldos menores a $800.000\n")
            print(f"Nombre empleado\tSueldo")
            print(f"{trabajador}\t{sueldo}") 
        elif 800000 < sueldo < 2000000:
            print("\nSueldos entre $800.000 y $2.000.000\n")
            print("Nombre empleado\tSueldo")
            print(f"{trabajador}\t{sueldo}")
        else:
            print("\nSueldos superiores a $2.000.000\n")
            print("Nombre empleado\tSueldo")
            print(f"{trabajador}\t{sueldo}")

# Funcion para visualizar estadisticas
def visualizar_estadisticas(sueldos):
    montos = list(sueldos.values())
    print("\n-- ESTADISTICA DE SUELDOS: -- \n")
    print(f"Sueldo mas alto -> {max(montos)}")
    print(f"Sueldo mas bajo -> {min(montos)}")
    print(f"Promedio del sueldo: {statistics.mean(montos)}")
    print(f"Desviacion estándar de sueldos: {statistics.stdev(montos)}")

# Funcion para generar repote de sueldos en un archivo .csv
def reporte_sueldos(sueldos):
    descuento_salud = 0.07 * 10000
    descuento_afp = 0.12 * 10000
    with open('reporte.csv', 'w', newline='') as csvfile:
        fieldnames = ['Nombre empleado', 'Sueldo base', 'Descuento salud', 'Descuento AFP', 'Sueldo liquido']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for empleado, sueldo in sueldos.items():    
            writer.writerow({'Nombre empleado': empleado, 'Sueldo base': int(sueldo), 'Descuento salud': int(descuento_salud), 'Descuento AFP': int(descuento_afp), 'Sueldo liquido': int(sueldo - descuento_salud - descuento_afp)})

    print("\nReporte de donaciones generado correctamente\n")

# Funcion main, flujo principal del programa
def main():
    while True:
        print("\nMenu")
        print("1 - Asignar sueldos aleatorios")
        print("2 - Clasificar sueldos")
        print("3 - Ver estadisticas")
        print("4 - Reporte de sueldos")
        print("5 - Salir del programa")
        opcion = input("\nSelecciona una opcion: ")

        if opcion == '1':
            sueldos = generar_sueldos_aleatorios()
            print("\nSueldos generados aleatoriamente.\n")
        elif opcion == '2':
            clasificar_sueldos(sueldos)
        elif opcion == '3':
            visualizar_estadisticas(sueldos)
        elif opcion == '4':
            reporte_sueldos(sueldos)
        elif opcion == '5':
            print("\nFinalizando programa...\n Desarrollado por Lukas Gaete\n RUT 22.056.738-9")
            break
        else:
            print("Opcion no valida. Porfavor selecciona una opcion valida")
            break


# Flujo principal del programa
if __name__ == '__main__':
    main()