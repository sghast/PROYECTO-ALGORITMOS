from collections import deque

def cargar_centros():
    centros = []
    try:
        archivo = open("centros.txt", "r", encoding="utf-8")
        for linea in archivo:
            nombre = linea.strip()
            if nombre != "":
                centros.append(nombre)
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
    print("\n--- AGREGAR CENTRO ---")
    nuevo_centro = input("> NOMBRE: ").strip()

    if nuevo_centro == "":
        print("[ERROR] Nombre inválido!!!")
        return

    centros.append(nuevo_centro)
    print("Centro agregado con éxito!")

def guardar_centros(centros):
    try:
        archivo = open("centros.txt", "w", encoding="utf-8")
        for dato in centros:
            archivo.write(dato + "\n")
        archivo.close()
        print("Centros guardados con éxito!")
    except:
        print("[ERROR] No se pudo guardar centros en el archivo!!!")

def actualizar_centro(centros):
    if len(centros) == 0:
        print("[ERROR] No hay centros registrados")
        return

    print("\n--- ACTUALIZAR CENTRO ---")
    mostrar_centros(centros)

    try:
        pos = int(input("Ingrese el número del centro a actualizar: "))
        if pos < 1 or pos > len(centros):
            print("[ERROR] Número inválido!!!")
            return
    except:
        print("[ERROR] Entrada inválida...")
        return

    nuevo_nombre = input("Ingrese el nuevo nombre: ").strip()
    if nuevo_nombre == "":
        print("[ERROR] Nombre inválido!!!")
        return

    centros[pos - 1] = nuevo_nombre
    print("Centro actualizado con éxito!")

def eliminar_centro(centros):
    if len(centros) == 0:
        print("[ERROR] No hay centros registrados")
        return

    print("\n--- ELIMINAR CENTRO ---")
    mostrar_centros(centros)

    try:
        pos = int(input("Ingrese el número del centro a eliminar: "))
        if pos < 1 or pos > len(centros):
            print("[ERROR] Número inválido!!!")
            return
    except:
        print("[ERROR] Entrada inválida...")
        return

    eliminado = centros.pop(pos - 1)
    print(f"'{eliminado}' eliminado con éxito!")

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

    return mayusculas and minusculas and numeros

def registro_usuario():
    print("\n--- REGISTRO DE USUARIO ---")
 
    while True:

        user = input("NOMBRE Y APELLIDO: ").strip()

        if user == "":
            print("[ERROR] El nombre no puede estar vacío.")

        elif len(user.split()) < 2:
            print("[ERROR] Debe ingresar nombre y apellido.")
            
        else:
            break

    while True:

        cedula = input("CÉDULA (10 dígitos): ").strip()

        if not cedula.isdigit():
            print("[ERROR] La cédula debe contener solo números.")

        elif len(cedula) != 10:
            print("[ERROR] La cédula debe tener exactamente 10 dígitos.")
        else:
            break

    while True:

        edad = input("EDAD (16-99): ").strip()

        if not edad.isdigit():
            print("[ERROR] La edad debe ser un número.")

        else:
            edad_num = int(edad)
            if edad_num < 16:
                print("[ERROR] Debe ser mayor de 16 años para registrarse.")

            elif edad_num >= 100:
                print("[ERROR] La edad debe ser menor a 100 años.")

            else:
                break

    correo_valido = False

    while not correo_valido:

        email = input("CORREO: ").strip()
        if email == "":
            print("[ERROR] El correo no puede estar vacío.")
        elif "@" not in email:
            print("[ERROR] El correo debe contener '@'.")
        elif email.count("@") > 1:
            print("[ERROR] El correo debe contener solo un '@'.")
        elif email.startswith("@") or email.endswith("@"):
            print("[ERROR] El correo no puede comenzar ni terminar con '@'.")
        else:
            correo_valido = True
            print("Correo válido.")

    while True:

        pwd = input("CONTRASEÑA: ").strip()
        if not contraseña_segura(pwd):
            print("[ERROR] Contraseña no segura -> Debe incluir mayúsculas, minúsculas y números")

        else:
            break

    try:
        archivo = open("usuarios.txt", "a", encoding="utf-8")
        archivo.write(f"{user};{cedula};{edad};{email};{pwd}\n")
        archivo.close()
        print("Usuario registrado correctamente.")

    except:
        print("[ERROR] No se pudo guardar el usuario!!")

def login_user():
    print("\n--- LOGIN ---")
    email = input("USUARIO (correo): ").strip()
    pwd = input("CONTRASEÑA: ").strip()

    try:
        archivo = open("usuarios.txt", "r", encoding="utf-8")
    except:
        print("[ERROR] No existe el archivo de usuarios!!!")
        return None

    for linea in archivo:
        datos = linea.strip().split(";")
        if len(datos) < 5:
            continue

        correo_guardado = datos[3]
        contraseña_guardada = datos[4]

        if email == correo_guardado and pwd == contraseña_guardada:
            archivo.close()
            print("Has ingresado con éxito!")

            if email == "admin@polidelivery.com":
                return "admin", email
            else:
                return "cliente", email

    archivo.close()
    print("[ERROR] Usuario o contraseña incorrectas")
    return None

def crear_matriz_costos(centros):
    n = len(centros)
    matriz = []
    for i in range(n):
        fila = []
        for j in range(n):
            if i == j:
                fila.append(0)
            else:
                fila.append(None)
        matriz.append(fila)
    return matriz

def ingresar_costos(centros, matriz):
    if matriz is None:
        print("[ERROR] Primero cree la matriz de costos (opción 6).")
        return

    n = len(centros)
    if n < 2:
        print("[ERROR] Debe haber al menos 2 centros para ingresar costos.")
        return

    print("\n--- INGRESO DE COSTOS ---")
    for i in range(n):
        for j in range(i + 1, n):
            try:
                costo = int(input(f"Costo entre {centros[i]} y {centros[j]}: "))
                if costo < 0:
                    print("[ERROR] El costo no puede ser negativo.")
                    return
                matriz[i][j] = costo
                matriz[j][i] = costo
            except:
                print("[ERROR] Costo inválido!!!")
                return

    print("Costos ingresados con éxito!")

def mostrar_matriz(centros, matriz):
    if matriz is None:
        print("[ERROR] No existe matriz. Cree la matriz primero.")
        return

    print("\n--- MATRIZ DE COSTOS ---")
    print("     ", end="")
    for c in centros:
        print(f"{c[:3]:>5}", end="")
    print()

    for i in range(len(centros)):
        print(f"{centros[i][:3]:>5}", end="")
        for j in range(len(centros)):
            valor = matriz[i][j]
            if valor is None:
                print(f"{'-':>5}", end="")
            else:
                print(f"{valor:>5}", end="")
        print()

def dijkstra(centros, matriz, origen):
    n = len(centros)
    visitado = [False] * n
    distancia = [float("inf")] * n
    previo = [-1] * n

    distancia[origen] = 0

    for _ in range(n):
        min_dist = float("inf")
        u = -1

        for i in range(n):
            if not visitado[i] and distancia[i] < min_dist:
                min_dist = distancia[i]
                u = i

        if u == -1:
            break

        visitado[u] = True

        for v in range(n):
            if matriz[u][v] is not None and not visitado[v]:
                nueva_dist = distancia[u] + matriz[u][v]
                if nueva_dist < distancia[v]:
                    distancia[v] = nueva_dist
                    previo[v] = u

    return distancia, previo

def obtener_ruta(previo, destino):
    ruta = []
    actual = destino
    while actual != -1:
        ruta.insert(0, actual)
        actual = previo[actual]
    return ruta

def consultar_ruta(centros, matriz):
    if matriz is None:
        print("[ERROR] Aún no existe matriz de costos. Pida al ADMIN crearla e ingresar costos.")
        return

    if len(centros) < 2:
        print("[ERROR] Debe haber al menos 2 centros.")
        return

    print("\n--- CONSULTAR RUTA ÓPTIMA (DIJKSTRA) ---")
    mostrar_centros(centros)

    try:
        origen = int(input("Centro origen (#): ")) - 1
        destino = int(input("Centro destino (#): ")) - 1
        if origen < 0 or origen >= len(centros) or destino < 0 or destino >= len(centros):
            print("[ERROR] Índices fuera de rango.")
            return
    except:
        print("[ERROR] Entrada inválida!!!")
        return

    distancia, previo = dijkstra(centros, matriz, origen)

    if distancia[destino] == float("inf"):
        print("[ERROR] No hay ruta posible (faltan costos o conexión).")
        return

    ruta = obtener_ruta(previo, destino)

    print("\nRuta óptima:")
    for i in range(len(ruta)):
        if i == len(ruta) - 1:
            print(centros[ruta[i]], end="")
        else:
            print(centros[ruta[i]], end=" -> ")
    print("\nCosto total:", distancia[destino])

def crear_arbol_regiones():
    arbol = {}
    print("\n--- CREAR ÁRBOL DE REGIONES ---")
    print("(Escriba 0 para salir)")

    while True:
        region = input("\nIngrese el nombre de la región: ").strip()
        if region == "0":
            break
        if region == "":
            print("[ERROR] Región inválida.")
            continue

        if region not in arbol:
            arbol[region] = []

        while True:
            centro = input(f"Ingrese el centro para {region} (0 para terminar región): ").strip()
            if centro == "0":
                break
            if centro == "":
                print("[ERROR] Centro inválido.")
                continue
            arbol[region].append(centro)

    return arbol

def mostrar_arbol_regiones(arbol):
    if arbol is None or len(arbol) == 0:
        print("[ERROR] No hay árbol de regiones creado.")
        return

    print("\n--- ÁRBOL DE REGIONES ---")
    for region in arbol:
        print(region)
        for centro in arbol[region]:
            print("  └─", centro)

def construir_adyacencia(centros, matriz):
    adya = {}
    n = len(centros)

    for i in range(n):
        adya[i] = []
        for j in range(n):
            if matriz is not None and matriz[i][j] is not None and matriz[i][j] != 0:
                adya[i].append(j)
    return adya

def bfs_centros_cercanos(centros, matriz, origen):
    ady = construir_adyacencia(centros, matriz)
    visitado = [False] * len(centros)
    cola = deque()

    visitado[origen] = True
    cola.append(origen)

    recorrido = []

    while cola:
        actual = cola.popleft()
        recorrido.append(actual)

        for vecino in ady[actual]:
            if not visitado[vecino]:
                visitado[vecino] = True
                cola.append(vecino)

    return recorrido

def buscar_centros_cercanos(centros, matriz):
    if matriz is None:
        print("[ERROR] No existe matriz de costos.")
        return

    mostrar_centros(centros)
    try:
        origen = int(input("Centro origen (#): ")) - 1
        if origen < 0 or origen >= len(centros):
            print("[ERROR] Centro inválido.")
            return
    except:
        print("[ERROR] Entrada inválida.")
        return

    recorrido = bfs_centros_cercanos(centros, matriz, origen)

    print("\nCentros cercanos (BFS):")
    for i in recorrido:
        print("-", centros[i])

def dfs_explorar(centros, matriz, origen):
    ady = construir_adyacencia(centros, matriz)
    visitado = [False] * len(centros)
    pila = [origen]

    recorrido = []

    while pila:
        actual = pila.pop()

        if not visitado[actual]:
            visitado[actual] = True
            recorrido.append(actual)

            for vecino in ady[actual]:
                if not visitado[vecino]:
                    pila.append(vecino)

    return recorrido

def explorar_rutas_dfs(centros, matriz):
    if matriz is None:
        print("[ERROR] No existe matriz de costos.")
        return

    mostrar_centros(centros)

    try:
        origen = int(input("Centro origen (#): ")) - 1
        if origen < 0 or origen >= len(centros):
            print("[ERROR] Centro inválido.")
            return
    except:
        print("[ERROR] Entrada inválida.")
        return

    recorrido = dfs_explorar(centros, matriz, origen)

    print("\nExploración completa de rutas (DFS):")
    for i in recorrido:
        print("-", centros[i])

def guardar_ruta_cliente(nombre_archivo, centros, ruta, costo):
    try:
        archivo = open(nombre_archivo, "a", encoding="utf-8")
        archivo.write("Ruta: ")
        for i in range(len(ruta)):
            if i == len(ruta) - 1:
                archivo.write(centros[ruta[i]])
            else:
                archivo.write(centros[ruta[i]] + " -> ")
        archivo.write("\nCosto total: " + str(costo))
        archivo.write("\n-------------------------\n")
        archivo.close()
        print("Ruta guardada correctamente.")
    except:
        print("[ERROR] No se pudo guardar la ruta.")

def consultar_ruta_cliente(centros, matriz, correo_cliente):
    if matriz is None:
        print("[ERROR] No existe matriz de costos.")
        return

    mostrar_centros(centros)

    try:
        origen = int(input("Centro origen (#): ")) - 1
        destino = int(input("Centro destino (#): ")) - 1
        if origen < 0 or origen >= len(centros) or destino < 0 or destino >= len(centros):
            print("[ERROR] Índices fuera de rango.")
            return
    except:
        print("[ERROR] Entrada inválida.")
        return

    distancia, previo = dijkstra(centros, matriz, origen)

    if distancia[destino] == float("inf"):
        print("[ERROR] No hay ruta disponible.")
        return

    ruta = obtener_ruta(previo, destino)

    print("\nRuta óptima:")
    for i in range(len(ruta)):
        if i == len(ruta) - 1:
            print(centros[ruta[i]], end="")
        else:
            print(centros[ruta[i]], end=" -> ")
    print("\nCosto total:", distancia[destino])

    guardar = input("¿Desea guardar esta ruta? (s/n): ").lower()
    if guardar == "s":
        nombre_archivo = "rutas-" + correo_cliente.split("@")[0] + ".txt"
        guardar_ruta_cliente(nombre_archivo, centros, ruta, distancia[destino])

def menu_admin():
    print("\n\tMENÚ DE ADMINISTRADOR")
    print("1. Ver centros")
    print("2. Agregar centro")
    print("3. Actualizar centro")
    print("4. Eliminar centro")
    print("5. Guardar cambios")
    print("6. Crear matriz de costos")
    print("7. Ingresar costos")
    print("8. Mostrar matriz")
    print("9. Crear árbol de regiones")
    print("10. Mostrar árbol de regiones")
    print("11. SALIR")
    return input(">>> ").strip()

def menu_cliente():
    print("\n\tMENÚ DE CLIENTE")
    print("1. Ver centros")
    print("2. Consultar ruta óptima (y guardar)")
    print("3. Ver árbol de regiones")
    print("4. Buscar centros cercanos (BFS)")
    print("5. Explorar rutas (DFS)")
    print("6. SALIR")
    return input(">>> ").strip()

def menu_inicial():
    print("\n\t--- POLIDELIVERY ---")
    print("1. Ver centros de distribución")
    print("2. Registrar usuario")
    print("3. Login")
    print("4. Salir")
    return input(">>> ").strip()

def main():
    centros = cargar_centros()
    matriz = None
    arbol_regiones = {}

    salir = False
    while not salir:
        opcion = menu_inicial()

        if opcion == "1":
            mostrar_centros(centros)
        elif opcion == "2":
            registro_usuario()
        elif opcion == "3":
            rol, correo = login_user()

            if rol == "admin":
                exit_admin = False
                while not exit_admin:
                    op = menu_admin()

                    if op == "1":
                        mostrar_centros(centros)
                    elif op == "2":
                        agregar_centro(centros)
                    elif op == "3":
                        actualizar_centro(centros)
                    elif op == "4":
                        eliminar_centro(centros)
                    elif op == "5":
                        guardar_centros(centros)
                    elif op == "6":
                        matriz = crear_matriz_costos(centros)
                        print("Matriz creada con éxito!")
                    elif op == "7":
                        ingresar_costos(centros, matriz)
                    elif op == "8":
                        mostrar_matriz(centros, matriz)
                    elif op == "9":
                        arbol_regiones = crear_arbol_regiones()
                        print("Árbol de regiones creado con éxito!")
                    elif op == "10":
                        mostrar_arbol_regiones(arbol_regiones)
                    elif op == "11":
                        exit_admin = True
                    else:
                        print("[ERROR] Opción inválida")

            elif rol == "cliente":
                exit_cliente = False
                while not exit_cliente:
                    op = menu_cliente()

                    if op == "1":
                        mostrar_centros(centros)
                    elif op == "2":
                        consultar_ruta_cliente(centros, matriz, correo)
                    elif op == "3":
                        mostrar_arbol_regiones(arbol_regiones)
                    elif op == "4":
                        buscar_centros_cercanos(centros, matriz)
                    elif op == "5":
                        explorar_rutas_dfs(centros, matriz)
                    elif op == "6":
                        exit_cliente = True
                    else:
                        print("[ERROR] Opción inválida")

        elif opcion == "4":
            print("GRACIAS POR USAR EL SISTEMA\nSALIENDO...")
            salir = True

        else:
            print("[ERROR] Opción no válida!!!")


main()