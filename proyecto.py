from collections import deque
from datetime import datetime


# ──────── ORDENAMIENTO ────────
def ordenar_burbuja_nombres(lista):
    n = len(lista)
    for i in range(n):
        for j in range(n - i - 1):
            if lista[j].lower() > lista[j + 1].lower():
                lista[j], lista[j + 1] = lista[j + 1], lista[j]


def ordenar_insercion_nombres(lista):
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        while j >= 0 and lista[j].lower() > clave.lower():
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave


def ordenar_seleccion_nombres(lista):
    n = len(lista)
    for i in range(n):
        minimo = i
        for j in range(i + 1, n):
            if lista[j].lower() < lista[minimo].lower():
                minimo = j
        lista[i], lista[minimo] = lista[minimo], lista[i]


# ──────── BÚSQUEDA ────────
def buscar_lineal(lista, valor):
    valor = valor.lower()
    for i, elem in enumerate(lista):
        if elem.lower() == valor:
            return i
    return -1


# ──────── GESTIÓN DE CENTROS ────────
def cargar_centros():
    centros = []
    try:
        with open("centros.txt", "r", encoding="utf-8") as f:
            for linea in f:
                nombre = linea.strip()
                if nombre:
                    centros.append(nombre)
    except FileNotFoundError:
        print("[ERROR] No se encontró centros.txt")
    except Exception:
        print("[ERROR] Problema al leer centros.txt")
    return centros


def mostrar_centros(centros):
    if not centros:
        print("[ERROR] No hay centros registrados")
        return
    print("\nCentros de distribución:")
    for i, c in enumerate(centros, 1):
        print(f"{i}. {c}")


def agregar_centro(centros):
    nombre = input("\n> Nombre del nuevo centro: ").strip()
    if not nombre:
        print("[ERROR] Nombre no puede estar vacío")
        return
    centros.append(nombre)
    print("Centro agregado correctamente")


def guardar_centros(centros):
    try:
        with open("centros.txt", "w", encoding="utf-8") as f:
            for c in centros:
                f.write(c + "\n")
        print("Centros guardados correctamente")
    except Exception:
        print("[ERROR] No se pudo guardar el archivo centros.txt")


def actualizar_centro(centros):
    if not centros:
        print("[ERROR] No hay centros registrados")
        return
    mostrar_centros(centros)
    try:
        num = int(input("Número del centro a actualizar: "))
        if num < 1 or num > len(centros):
            print("[ERROR] Número fuera de rango")
            return
    except ValueError:
        print("[ERROR] Debe ingresar un número válido")
        return

    nuevo = input("Nuevo nombre: ").strip()
    if not nuevo:
        print("[ERROR] Nombre no puede estar vacío")
        return
    centros[num - 1] = nuevo
    print("Centro actualizado")


def eliminar_centro(centros):
    if not centros:
        print("[ERROR] No hay centros registrados")
        return
    mostrar_centros(centros)
    try:
        num = int(input("Número del centro a eliminar: "))
        if num < 1 or num > len(centros):
            print("[ERROR] Número fuera de rango")
            return
    except ValueError:
        print("[ERROR] Debe ingresar un número válido")
        return
    eliminado = centros.pop(num - 1)
    print(f"Centro eliminado: {eliminado}")


# ──────── USUARIOS ────────
def contraseña_segura(texto):
    tiene_mayus = any(c.isupper() for c in texto)
    tiene_minus = any(c.islower() for c in texto)
    tiene_numero = any(c.isdigit() for c in texto)
    return tiene_mayus and tiene_minus and tiene_numero


def registrar_usuario():
    print("\n--- Registro de usuario ---")

    while True:
        nombre = input("Nombre y apellido: ").strip()
        if len(nombre.split()) >= 2:
            break
        print("[ERROR] Debe ingresar nombre y apellido")

    while True:
        cedula = input("Cédula (10 dígitos): ").strip()
        if cedula.isdigit() and len(cedula) == 10:
            break
        print("[ERROR] Cédula debe tener exactamente 10 dígitos numéricos")

    while True:
        edad_str = input("Edad (16-99): ").strip()
        if edad_str.isdigit():
            edad = int(edad_str)
            if 16 <= edad < 100:
                break
        print("[ERROR] Edad debe estar entre 16 y 99")

    while True:
        email = input("Correo electrónico: ").strip()
        if "@" in email and "." in email and email.count("@") == 1 and not (email.startswith("@") or email.endswith("@") or email.startswith(".") or email.endswith(".")):
            break
        print("[ERROR] Correo inválido")

    while True:
        clave = input("Contraseña: ").strip()
        if contraseña_segura(clave):
            break
        print("[ERROR] La contraseña debe contener mayúsculas, minúsculas y números")

    try:
        with open("usuarios.txt", "a", encoding="utf-8") as f:
            f.write(f"{nombre};{cedula};{edad};{email};{clave}\n")
        print("Usuario registrado exitosamente")
    except Exception:
        print("[ERROR] No se pudo guardar el usuario")


def iniciar_sesion():
    print("\n--- Iniciar sesión ---")
    email = input("Correo: ").strip()
    clave = input("Contraseña: ").strip()

    try:
        with open("usuarios.txt", "r", encoding="utf-8") as f:
            for linea in f:
                datos = linea.strip().split(";")
                if len(datos) >= 5 and datos[3] == email and datos[4] == clave:
                    print("Sesión iniciada correctamente")
                    if email == "admin@polidelivery.com":
                        return "admin", email
                    return "cliente", email
    except FileNotFoundError:
        print("[ERROR] No existe el archivo de usuarios")
        return None
    except Exception:
        print("[ERROR] Problema al leer usuarios.txt")
        return None

    print("[ERROR] Credenciales incorrectas")
    return None


# ──────── MATRIZ Y COSTOS ────────

def crear_matriz_costos(centros):
    n = len(centros)
    return [[0 if i == j else None for j in range(n)] for i in range(n)]


def ingresar_costos(centros, matriz):
    if matriz is None:
        print("[ERROR] Primero debe crear la matriz de costos")
        return
    n = len(centros)
    if n < 2:
        print("[ERROR] Se necesitan al menos 2 centros")
        return

    for i in range(n):
        for j in range(i + 1, n):
            try:
                costo = int(input(f"Costo de {centros[i]} → {centros[j]}: "))
                if costo < 0:
                    print("[ERROR] El costo no puede ser negativo")
                    return
                matriz[i][j] = matriz[j][i] = costo
            except ValueError:
                print("[ERROR] Ingrese un número entero válido")
                return
    print("Costos ingresados correctamente")


def mostrar_matriz(centros, matriz):
    if matriz is None:
        print("[ERROR] No existe matriz de costos")
        return
    n = len(centros)
    print("\nMatriz de costos:")
    print("      " + " ".join(f"{c[:3]:>5}" for c in centros))
    for i in range(n):
        print(f"{centros[i][:3]:>5}", end=" ")
        for j in range(n):
            v = matriz[i][j]
            print(f"{v if v is not None else '-':>5}", end=" ")
        print()


# ──────── DIJKSTRA ────────

def dijkstra(centros, matriz, inicio):
    n = len(centros)
    dist = [float('inf')] * n
    prev = [-1] * n
    visitado = [False] * n
    dist[inicio] = 0

    for _ in range(n):
        u = -1
        min_d = float('inf')
        for i in range(n):
            if not visitado[i] and dist[i] < min_d:
                min_d = dist[i]
                u = i
        if u == -1:
            break
        visitado[u] = True
        for v in range(n):
            if matriz[u][v] is not None and matriz[u][v] > 0 and not visitado[v]:
                alt = dist[u] + matriz[u][v]
                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u
    return dist, prev


def obtener_ruta(prev, destino):
    ruta = []
    actual = destino
    while actual != -1:
        ruta.insert(0, actual)
        actual = prev[actual]
    return ruta


def consultar_ruta_cliente(centros, matriz, email):
    if matriz is None:
        print("[ERROR] No existe matriz de costos")
        return

    mostrar_centros(centros)
    try:
        o = int(input("Centro origen (número): ")) - 1
        d = int(input("Centro destino (número): ")) - 1
        if not (0 <= o < len(centros) and 0 <= d < len(centros)):
            print("[ERROR] Centro fuera de rango")
            return
    except ValueError:
        print("[ERROR] Ingrese números válidos")
        return

    dist, prev = dijkstra(centros, matriz, o)

    if dist[d] == float('inf'):
        print("[ERROR] No existe ruta entre estos centros")
        return

    ruta_idx = obtener_ruta(prev, d)
    print("\nRuta óptima encontrada:")
    print(" → ".join(centros[i] for i in ruta_idx))
    print(f"Costo total: ${dist[d]}")

    if input("\n¿Guardar esta ruta? (s/n): ").lower().startswith('s'):
        nombre_arch = f"rutas-{email.split('@')[0]}.txt"
        try:
            with open(nombre_arch, "a", encoding="utf-8") as f:
                f.write(f"{datetime.now():%Y-%m-%d %H:%M} | Ruta: {' → '.join(centros[i] for i in ruta_idx)} | Costo: ${dist[d]}\n")
            print(f"Ruta guardada en {nombre_arch}")
        except:
            print("[ERROR] No se pudo guardar la ruta")


# ──────── ÁRBOL DE REGIONES ────────

def crear_arbol_regiones():
    regiones = {}
    print("\n--- Crear árbol de regiones ---")
    print("  (escriba '0' para terminar)")

    while True:
        region = input("\nNombre de la región: ").strip()
        if region == "0":
            break
        if not region:
            print("[ERROR] Nombre de región inválido")
            continue

        regiones.setdefault(region, [])

        while True:
            centro = input(f"  Centro en {region} (0 para terminar región): ").strip()
            if centro == "0":
                break
            if not centro:
                print("  [ERROR] Nombre de centro inválido")
                continue
            regiones[region].append(centro)

    return regiones


def mostrar_arbol_regiones(regiones):
    if not regiones:
        print("[ERROR] No hay regiones creadas")
        return

    print("\n--- Árbol de regiones ---")
    for region, centros in regiones.items():
        print(f"{region}")
        for c in centros:
            print(f"  └─ {c}")


# ──────── BFS y DFS ────────

def construir_adyacencia(centros, matriz):
    ady = {i: [] for i in range(len(centros))}
    n = len(centros)
    for i in range(n):
        for j in range(n):
            if i != j and matriz[i][j] is not None and matriz[i][j] > 0:
                ady[i].append(j)
    return ady


def bfs_centros_cercanos(centros, matriz, origen):
    if matriz is None:
        print("[ERROR] No hay matriz de costos")
        return []

    ady = construir_adyacencia(centros, matriz)
    visitado = [False] * len(centros)
    cola = deque([origen])
    visitado[origen] = True
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
    if not centros:
        print("[ERROR] No hay centros")
        return

    mostrar_centros(centros)
    try:
        origen = int(input("Número del centro origen: ")) - 1
        if origen < 0 or origen >= len(centros):
            print("[ERROR] Centro inválido")
            return
    except ValueError:
        print("[ERROR] Ingrese un número válido")
        return

    recorrido = bfs_centros_cercanos(centros, matriz, origen)
    print("\nCentros alcanzables (BFS):")
    for idx in recorrido:
        print(f"- {centros[idx]}")


def dfs_explorar(centros, matriz, origen):
    if matriz is None:
        print("[ERROR] No hay matriz de costos")
        return []

    ady = construir_adyacencia(centros, matriz)
    visitado = [False] * len(centros)
    pila = [origen]
    recorrido = []

    while pila:
        actual = pila.pop()
        if not visitado[actual]:
            visitado[actual] = True
            recorrido.append(actual)
            for vecino in reversed(ady[actual]):
                if not visitado[vecino]:
                    pila.append(vecino)
    return recorrido


def explorar_rutas_dfs(centros, matriz):
    if not centros:
        print("[ERROR] No hay centros")
        return

    mostrar_centros(centros)
    try:
        origen = int(input("Número del centro origen: ")) - 1
        if origen < 0 or origen >= len(centros):
            print("[ERROR] Centro inválido")
            return
    except ValueError:
        print("[ERROR] Ingrese un número válido")
        return

    recorrido = dfs_explorar(centros, matriz, origen)
    print("\nExploración DFS (orden de visita):")
    for idx in recorrido:
        print(f"- {centros[idx]}")


# ──────── CARRITO ────────
def mostrar_seleccion_carrito(seleccion, centros, matriz):
    if not seleccion:
        print("  Carrito vacío")
        return 0
    total = 0
    print("\nContenido del carrito:")
    for i, idx in enumerate(seleccion, 1):
        print(f"  {i}. {centros[idx]}")
        if i > 1:
            ant = seleccion[i-2]
            costo = matriz[ant][idx] if matriz and matriz[ant][idx] is not None else None
            if costo is not None:
                print(f"     └─ tramo ${costo}")
                total += costo
            else:
                print("     └─ costo no disponible")
    print(f"\nTotal estimado de tramos: ${total}")
    return total


def agregar_al_carrito(seleccion, centros):
    mostrar_centros(centros)
    try:
        num = int(input("Número del centro a agregar: ")) - 1
        if 0 <= num < len(centros):
            if num not in seleccion:
                seleccion.append(num)
                print(f"Agregado: {centros[num]}")
            else:
                print("Este centro ya está en el carrito")
        else:
            print("Número fuera de rango")
    except ValueError:
        print("[ERROR] Ingrese un número válido")


def quitar_del_carrito(seleccion, centros):
    if not seleccion:
        print("Carrito vacío")
        return
    for i, idx in enumerate(seleccion, 1):
        print(f"{i}. {centros[idx]}")
    try:
        pos = int(input("Posición a quitar: ")) - 1
        if 0 <= pos < len(seleccion):
            eliminado = seleccion.pop(pos)
            print(f"Quitado: {centros[eliminado]}")
        else:
            print("Posición inválida")
    except ValueError:
        print("[ERROR] Ingrese un número válido")


def guardar_carrito(seleccion, centros, email):
    if not seleccion:
        print("No hay nada que guardar")
        return
    arch = f"carrito-{email.split('@')[0]}.txt"
    try:
        with open(arch, "a", encoding="utf-8") as f:
            f.write(f"\n{datetime.now():%Y-%m-%d %H:%M}\n")
            for idx in seleccion:
                f.write(f"• {centros[idx]}\n")
            f.write("-" * 40 + "\n")
        print(f"Carrito guardado en {arch}")
    except Exception:
        print("[ERROR] No se pudo guardar el carrito")


# ──────── MENÚS ────────

def menu_admin():
    print("\n  MENÚ ADMINISTRADOR")
    print(" 1. Ver centros          7. Ingresar costos")
    print(" 2. Agregar centro       8. Mostrar matriz")
    print(" 3. Actualizar centro    9. Crear árbol regiones")
    print(" 4. Eliminar centro     10. Ver árbol regiones")
    print(" 5. Guardar cambios     11. Salir")
    print(" 6. Crear matriz")
    return input("→ ").strip()


def menu_cliente():
    print("\n  MENÚ CLIENTE")
    print(" 1. Ver centros")
    print(" 2. Ruta óptima (Dijkstra)")
    print(" 3. Ver regiones")
    print(" 4. Centros cercanos (BFS)")
    print(" 5. Explorar rutas (DFS)")
    print(" 6. Mi carrito")
    print(" 7. Salir")
    return input("→ ").strip()


def menu_principal():
    print("\n  === POLIDELIVERY ===")
    print(" 1. Ver centros")
    print(" 2. Registrarse")
    print(" 3. Iniciar sesión")
    print(" 4. Salir")
    return input("→ ").strip()


# ──────── PROGRAMA PRINCIPAL ────────

def main():
    centros = cargar_centros()
    matriz_costos = None
    regiones = {}

    while True:
        opcion = menu_principal()

        if opcion == "1":
            mostrar_centros(centros)

        elif opcion == "2":
            registrar_usuario()

        elif opcion == "3":
            sesion = iniciar_sesion()
            if sesion is None:
                continue
            rol, email = sesion

            if rol == "admin":
                while True:
                    op = menu_admin()
                    if op == "1": mostrar_centros(centros)
                    elif op == "2": agregar_centro(centros)
                    elif op == "3": actualizar_centro(centros)
                    elif op == "4": eliminar_centro(centros)
                    elif op == "5": guardar_centros(centros)
                    elif op == "6":
                        matriz_costos = crear_matriz_costos(centros)
                        print("Matriz de costos creada")
                    elif op == "7": ingresar_costos(centros, matriz_costos)
                    elif op == "8": mostrar_matriz(centros, matriz_costos)
                    elif op == "9":
                        regiones = crear_arbol_regiones()
                        print("Árbol de regiones creado")
                    elif op == "10": mostrar_arbol_regiones(regiones)
                    elif op == "11": break
                    else: print("[Opción no válida]")
            else:
                carrito = []
                while True:
                    op = menu_cliente()
                    if op == "1":
                        mostrar_centros(centros)
                    elif op == "2":
                        consultar_ruta_cliente(centros, matriz_costos, email)
                    elif op == "3":
                        mostrar_arbol_regiones(regiones)
                    elif op == "4":
                        buscar_centros_cercanos(centros, matriz_costos)
                    elif op == "5":
                        explorar_rutas_dfs(centros, matriz_costos)
                    elif op == "6":
                        while True:
                            print(f"\n  MI CARRITO ({len(carrito)} items)")
                            print(" 1. Ver carrito")
                            print(" 2. Agregar centro")
                            print(" 3. Quitar centro")
                            print(" 4. Ordenar alfabéticamente")
                            print(" 5. Buscar en carrito")
                            print(" 6. Guardar carrito")
                            print(" 7. Volver")
                            sub = input("→ ").strip()

                            if sub == "1":
                                mostrar_seleccion_carrito(carrito, centros, matriz_costos)
                            elif sub == "2":
                                agregar_al_carrito(carrito, centros)
                            elif sub == "3":
                                quitar_del_carrito(carrito, centros)
                            elif sub == "4":
                                metodo = input("Método (a=burbuja, b=inserción, c=selección): ").lower()
                                if metodo not in ('a','b','c'):
                                    print("Opción inválida")
                                    continue
                                nombres = [centros[i] for i in carrito]
                                if metodo == 'a': ordenar_burbuja_nombres(nombres)
                                elif metodo == 'b': ordenar_insercion_nombres(nombres)
                                else: ordenar_seleccion_nombres(nombres)
                                print("\nOrdenado:")
                                for n in nombres:
                                    print(f"• {n}")
                            elif sub == "5":
                                busqueda = input("Nombre del centro: ").strip()
                                pos = buscar_lineal([centros[i] for i in carrito], busqueda)
                                print(f"Encontrado en posición {pos+1}" if pos >= 0 else "No encontrado")
                            elif sub == "6":
                                guardar_carrito(carrito, centros, email)
                            elif sub == "7":
                                break
                            else:
                                print("[Opción no válida]")
                    elif op == "7":
                        break
                    else:
                        print("[Opción no válida]")

        elif opcion == "4":
            print("Gracias por usar Polidelivery")
            break

        else:
            print("[Opción no válida]")


if __name__ == "__main__":
    main()