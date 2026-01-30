def cargar_centros():
    centros = []
    try:
        archivo = open("centros.txt", "r")
        for linea in archivo:
            centros.append(linea.strip())
        archivo.close()
    except:
        print("[ERROR] No se pudo abrir el archivo de centros!!!")
    return centros

def mostrar_centros(centros):
    if len(centros) == 0:
        print("[ERROR] No hay centros registrados!!!")
    else:
        print("\nCentros de distribución:")
        for i in range(len(centros)):
            print(f"{i+1}. {centros[i]}")

def agregar_centro(centros):
    nuevo_centro = input("> NOMBRE: ")

    if nuevo_centro == "":
        print("[ERROR] Nombre inávlido!!!")
        return
    
    centros.append(nuevo_centro)
    print("Centro agregado con éxito!")

def guardar_centros(centros):
    archivo = open("centros.txt", "w")

    for dato in centros:
        archivo.write(dato + "\n")
        
    archivo.close()
    print("Centros guardados con éxito!")

def actualizar_centro(centros):
    if len(centros) == 0:
        print("No hay centros registrados")
        return
    
    mostrar_centros(centros)
    try:
        posicion_actualizar = int(input("Ingresa el número del centro a actualizar: "))
        if posicion_actualizar < 1 or posicion_actualizar > len(centros):
            print("[ERROR] Número inválido!!!")
            return
    except:
        print("Entrada inávlida...")
        return
    
    nuevo_nombre = input("Ingrese el nuevo nombre: ")
    if nuevo_nombre == "":
        print("[ERROR] Nombre inválido!!!")
        return
    
    centros[posicion_actualizar - 1] = nuevo_nombre
    print("Centro actualizado con éxito!")

def eliminar_centro(centros):
    if len(centros) == 0:
        print("No hay centros registrados")
        return
    
    mostrar_centros(centros)
    try:
        posicion_eliminar = int(input("Ingresa el número del centro a actualizar: "))
        if posicion_eliminar < 1 or posicion_eliminar > len(centros):
            print("[ERROR] Número inválido!!!")
            return
    except:
        print("Entrada inávlida...")
        return
    
    eliminado = centros.pop(posicion_eliminar - 1)
    print(f"{eliminado} eliminado con éxito!")

#forzar al usuario a ingresar una contraseña segura: eSf0T
def contraseña_segura(contraseña):
    mayusculas = False
    minusculas = False
    numeros = False

    for caracter in contraseña:
        if caracter.isupper():
            mayusculas = True
        elif caracter.islower():
            minusculas = True
        elif caracter.isdigit():
            numeros = True
    
    if mayusculas and minusculas and numeros:
        return True
    else:
        return False

#ingreso de un nuevo usuario
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

#login de un usuario ya existente
def login_user():
    email = input("USUARIO (correo): ")
    pwd = input("CONTRASEÑA: ")

    try:
        archivo = open("usuarios.txt", "r")
    except:
        print("[ERROR] No existe el archivo de usuarios!!!")
        return None
    
    for linea in archivo:
        datos = linea.strip().split(";")
        #estructura de usuarios.txt:
        #nombre;cedula;edad;email;contraseña
        #  0      1     2    3        4
        #entonces debemos fijarnos en la posición 3 y 4
        correo_guardado = datos[3]
        contraseña_guardada = datos[4]

        if email == correo_guardado and pwd == contraseña_guardada:
            print("Has ingresado con éxito!")
            archivo.close()

            if email == "admin@polidelivery.com":
                return "admin"
            else:
                return "cliente"
    
    archivo.close()
    print("[ERROR] Usuario o contraseña incorrectas")
    return None

def menu_admin():
    print("MENÚ DE ADMINISTRADOR")
    print("1. Ver centros")
    print("2. Agregar centro")
    print("3. Actualizar centro")
    print("4. Eliminar centro")
    print("5. Guardar cambios")
    print("6. SALIR")

    return input(">>> ")

def menu_cliente():
    print("MENú DE USUARIO")
    print("1. Ver centros")
    print("2. Consultar rutas")
    print("3. SALIR")

    return input(">>> ")

#se aumenta la opción: registrar usuario
def menu():
    print("\n\t--- POLIDELIVERY ---")
    print("1. Ver centros de distribución")
    print("2. Registrar usuario")
    print("3. Login")
    print("4. Salir")
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
            en_sesion = login_user()
            if en_sesion == "admin":

                exit_admin = False

                while not exit_admin:
                    opcion = menu_admin()
                    if opcion == "1":
                        mostrar_centros(centros)
                    elif opcion == "2":
                        agregar_centro(centros)
                    elif opcion == "3":
                        actualizar_centro(centros)
                    elif opcion == "4":
                        eliminar_centro(centros)
                    elif opcion == "5":
                        guardar_centros(centros)
                    elif opcion == "6":
                        exit_admin = True
                    else:
                        print("[ERROR] Opción inválida")
            elif en_sesion == "cliente":
                menu_cliente()
        elif opcion == "4":
            print("GRACIAS POR USAR EL SISTEMA\nSALIENDO...")
            salir = True
        else:
            print("Opción no válida!!!")

main()
