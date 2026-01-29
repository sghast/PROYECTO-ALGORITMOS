def cargar_centros():
    centros = []
    try:
        archivo = open("centros.txt", "r")
        for linea in archivo:
            centros.append(linea.strip())
        archivo.close()
    except:
        print("No se pudo abrir el archivo de centros!!!")
    return centros

def mostrar_centros(centros):
    if len(centros) == 0:
        print("No hay centros registrados!!!")
    else:
        print("\nCentros de distribución:")
        for i in range(len(centros)):
            print(f"{i+1}. {centros[i]}")

#forzar al usuario a ingresar una contraseña segura: eSf0T
def contraseña_segura (contraseña):
    mayusculas = False
    minusculas = False
    numeros = False

    for c in contraseña:
        if c.isupper():
            mayusculas = True
        elif c.islower():
            minusculas = True
        elif c.isdigit():
            numeros = True
    
    if mayusculas and minusculas and numeros:
        return True
    else:
        return False
        
def registro_usuario():
    user = input("USER: ")
    cedula = input("CEDULA: ")
    edad = input("EDAD: ")
    email = input("CORREO: ")

    pwd = input("CONTRASEÑA: ")
    if not contraseña_segura(pwd):
        print("La contraseña no es segura -> Debe incluir mayúsculas, minúsculas y números")
        return
    
    archivo = open("usuarios.txt", "a")
    archivo.write(f"{user};{cedula};{edad};{email};{pwd}\n")
    archivo.close()

    print("Usuario registrado correctamente.")

#se aumenta la opción: registrar usuario
def menu():
    print("\n  --- POLIDELIVERY ---")
    print("1. Ver centros de distribución")
    print("2. Registrar usuario")
    print("3. Salir")
    opcion = input(">>> ")
    return opcion

def main():
    centros = cargar_centros()
    salir = False

    while not salir:
        opcion = menu()
        if opcion == "1":
            mostrar_centros(centros)
        elif opcion == "2":
            registro_usuario()
        elif opcion == "3":
            print("GRACIAS POR USAR EL SISTEMA\nSALIENDO...")
            salir = True
        else:
            print("Opción no válida!!!")

main()
