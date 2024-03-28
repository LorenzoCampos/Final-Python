import os

def menu():
    os.system("cls")
    print("1- Carga de clases y cantidad máxima de horas sin mantenimiento.")
    print("2- Carga de aviones y su clase.")
    print("3- Horas de vuelo.")
    print("4- Aviones que necesitan mantenimiento.")
    print("5- Salir.")

def validar_nro(n, d, h):
    try:
        n = int(n)
        if  h >= n >= d:
            return False
        else:
            return True
    except:
            return True

def carga_clases():  # Carga de clases y cantidad max de horas sin mantenimiento.
    id_clase = input("Ingrese el ID de la clase <0 a 4>: ")
    while validar_nro(id_clase, 0, 3):
        id_clase = input("Incorrecto - Ingrese el ID de la clase <0 a 3>: ")
    os.system("cls")
    print("ID: " + id_clase)
    horas_max = input("Ingrese la cantidad de horas máximas sin mantenimiento: ")
    while validar_nro(horas_max, 1, float('inf')):
        horas_max = input("Incorrecto - Ingrese la cantidad de horas máximas sin mantenimiento: ")

    horas_clases[int(id_clase)] = int(horas_max)
    input()
    menu()

def carga_avion():
    nro_avion = input("Ingrese el número de avión <1 al 7>: ")
    while validar_nro(nro_avion, 1, 7):
        nro_avion = input("Incorrecto - Ingrese un número de avión valido <1 al 7>: ")
    nro_avion = int(nro_avion)

    nro_clase = input("Ingrese el número de clase <0 al 3>: ")
    while validar_nro(nro_clase, 0, 3):
        nro_clase = input("Incorrecto - Ingrese un número de clase válido <0 al 3>: ")

    clases_aviones[int(nro_avion) - 1] = int(nro_clase)
    input()
    menu()

def carga_horas():
    nro_avion = input("Ingresa el número de avión <1 al 7>: ")
    while validar_nro(nro_avion, 0, 7):
        nro_avion = input("Incorrecto - Ingrese un número de avión valido <1 al 7>: ")
    nro_avion = int(nro_avion)
    while nro_avion != 0:
        horas_vuelo = input("Ingresé la cantidad de horas del vuelo <1 al 10>: ")
        while validar_nro(horas_vuelo, 1, 10):
            horas_vuelo = input("Incorrecto - Ingresé un numero valido <1 al 10>: ")
        horas_vuelo = int(horas_vuelo)
        horas_avion [nro_avion - 1] += horas_vuelo
        nro_avion = input("Ingresa el número de avión <1 al 7>: ")
        while validar_nro(nro_avion, 0, 7):
            nro_avion = input("Incorrecto - Ingrese un número de avión valido <1 al 7>: ")
        nro_avion = int(nro_avion)
    input()
    menu()

def mostrar():
    print(f"{'Nro. Avión': <15} {'Clase': <11} {'Horas max. para mantenimiento': <35} {'Horas funcionando': <23} {'Exceso relativo'}")
    #crear lista de tuplas
    aviones_info = [(i + 1, clases_aviones[i], horas_clases[clases_aviones[i]], horas_avion[i], (horas_clases[clases_aviones[i]] - horas_avion[i]) / horas_clases[clases_aviones[i]]) for i in range(7)]
    #ordenar por exceso relativo
    aviones_ordenados = sorted(aviones_info, key=lambda x: x[4], reverse=True)
    
    for i, (nro_avion, avion_clase, horas_max, horas, exceso_rel) in enumerate(aviones_ordenados, start=1):
        if horas != 0 :
            print(f"{nro_avion: <16}{avion_clase: <12}{horas_max: <36}{horas: <24}{exceso_rel}")
    input()

clases_aviones = [0]*7
horas_clases = [0]*4
horas_avion = [0]*7
opc=0

while opc!=5:
    menu()
    opc = input("Ingrese una opcion <1 a 5>: ")
    while validar_nro(opc, 1, 5):
        opc = input("Incorrecto-Ingrese una opcion <1 a 5>: ")
    opc = int(opc)
    match opc:
        case 1:
            os.system("cls")
            print("-------- DEFINIR CLASES --------\n")
            carga_clases()
        case 2:
            os.system("cls") 
            print("-------- ASIGNAR CLASES --------\n")
            carga_avion()
        case 3:
            os.system("cls")
            print("-------- CARGA DE HORAS ---------\n")
            carga_horas()
        case 4:
            os.system("cls")
            print("-------- LISTA DE MANTENIMIENTO --------\n")
            mostrar()
        case 5:
            print("\n\nFin del Programa\n")