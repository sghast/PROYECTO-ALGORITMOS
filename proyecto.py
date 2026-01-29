def cargarCentros():
    centros = []
    try:
        archivo = open("centros.txt", "r")
        for linea in archivo:
            centros.append(linea.strip())
        archivo.close()
    except:
        print("No se pudo abrir el archivo de centros!!!")
    return centros


def mostrarCentros(centros):
    if len(centros) == 0:
        print("No hay centros registrados!!!")
    else:
        print("\nCentros de distribución:")
        for i in range(len(centros)):
            print(f"{i+1}. {centros[i]}")


def menu():
    print("\n  --- POLIDELIVERY ---")
    print("1. Ver centros de distribución")
    print("2. Salir")
    opcion = input("Seleccione una opción: ")
    return opcion

def main():
    centros = cargar_centros()
    salir = False

    while not salir:
        opcion = menu()
        if opcion == "1":
            mostrar_centros(centros)
        elif opcion == "2":
            print("GRACIAS POR USAR EL SISTEMA\nSALIENDO...")
            salir = True
        else:
            print("Opción no válida.")


main()
