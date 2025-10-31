import csv   #Librería para leer archivos CSV

# -------------------------------------------------------
# 📌 1. FUNCIÓN PARA LEER EL ARCHIVO CSV
# -------------------------------------------------------
def cargar_paises(nombre_archivo):
    paises = []  # Lista donde se guardarán todos los países
    try:
        with open(nombre_archivo, encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)  # Cada fila será un diccionario
            for fila in lector:
                # Convertimos los números a enteros (int)
                pais = {
                    'nombre': fila['nombre'],
                    'poblacion': int(fila['poblacion']),
                    'superficie': int(fila['superficie']),
                    'continente': fila['continente']
                }
                paises.append(pais)  # Agregamos el país a la lista
    except FileNotFoundError:
        print("No se encontró el archivo CSV.")
    return paises

# -------------------------------------------------------
# 📌 2. FUNCIÓN PARA BUSCAR UN PAÍS POR NOMBRE
# -------------------------------------------------------
def buscar_pais(paises, nombre):
    resultados = []
    for pais in paises:
        # Si el texto buscado está dentro del nombre (ignora mayúsculas)
        if nombre.lower() in pais['nombre'].lower():
            resultados.append(pais)
    return resultados


# -------------------------------------------------------
# 📌 3. FUNCIÓN PARA MOSTRAR ESTADÍSTICAS BÁSICAS
# -------------------------------------------------------
def mostrar_estadisticas(paises):
    if not paises:
        print("No hay datos cargados.")
        return

    # Calculamos población y superficie promedio
    total_poblacion = sum(p['poblacion'] for p in paises)
    total_superficie = sum(p['superficie'] for p in paises)
    promedio_poblacion = total_poblacion / len(paises)
    promedio_superficie = total_superficie / len(paises)

    # Buscamos país con mayor y menor población
    mayor = max(paises, key=lambda p: p['poblacion'])
    menor = min(paises, key=lambda p: p['poblacion'])

    print("\n📊 ESTADÍSTICAS:")
    print(f"• País con mayor población: {mayor['nombre']} ({mayor['poblacion']})")
    print(f"• País con menor población: {menor['nombre']} ({menor['poblacion']})")
    print(f"• Promedio de población: {promedio_poblacion:,.0f}")
    print(f"• Promedio de superficie: {promedio_superficie:,.0f}")


# -------------------------------------------------------
# 📌 4. MENÚ PRINCIPAL
# -------------------------------------------------------
def menu():
    paises = cargar_paises('paises.csv')  # Cargamos los datos del CSV

    if not paises:
        return  # Si no hay datos, salimos del programa

    while True:
        print("\n🌎 MENÚ PRINCIPAL")
        print("1) Buscar país por nombre")
        print("2) Mostrar estadísticas")
        print("3) Salir")
        opcion = input("Elija una opción: ")

        if opcion == "1":
            texto = input("Ingrese el nombre o parte del nombre del país: ")
            resultados = buscar_pais(paises, texto)
            if resultados:
                print("\n🔎 Resultados encontrados:")
                for p in resultados:
                    print(f"{p['nombre']} - {p['continente']} - Población: {p['poblacion']}")
            else:
                print("❌ No se encontró ningún país con ese nombre.")
        elif opcion == "2":
            mostrar_estadisticas(paises)
        elif opcion == "3":
            print("👋 ¡Hasta luego!")
            break
        else:
            print("⚠️ Opción no válida. Intente otra vez.")


# -------------------------------------------------------
# 📌 5. PUNTO DE ENTRADA DEL PROGRAMA
# -------------------------------------------------------
if __name__ == "__main__":
    menu()  # Inicia el programa
