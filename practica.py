import os

# Constante: Nombre del archivo donde guardaremos los datos
ARCHIVO_TAREAS = "tareas.txt"


def cargar_tareas():
    """Lee las tareas desde el archivo de texto."""
    if not os.path.exists(ARCHIVO_TAREAS):
        return []  # Si no existe el archivo, devuelve una lista vacía

    with open(ARCHIVO_TAREAS, "r", encoding="utf-8") as archivo:
        # Lee cada línea y le quita los espacios o saltos de línea al final
        return [linea.strip() for linea in archivo.readlines()]


def guardar_tareas(tareas):
    """Sobrescribe el archivo con la lista actualizada de tareas."""
    with open(ARCHIVO_TAREAS, "w", encoding="utf-8") as archivo:
        for tarea in tareas:
            archivo.write(f"{tarea}\n")


def mostrar_tareas(tareas):
    """Imprime las tareas en la consola de forma ordenada."""
    print("\n--- 📋 Mis Tareas ---")
    if not tareas:
        print("¡No tienes tareas pendientes! Aprovecha para descansar. 🎉")
    else:
        for i, tarea in enumerate(tareas, 1):
            print(f"{i}. {tarea}")
    print("---------------------\n")


def main():
    """Función principal que controla el flujo del programa."""
    tareas = cargar_tareas()

    while True:  # Bucle infinito que se rompe solo al elegir "Salir"
        mostrar_tareas(tareas)
        print("Opciones: [1] Agregar  [2] Eliminar  [3] Salir")
        opcion = input("Elige una opción (1/2/3): ").strip()

        if opcion == "1":
            nueva_tarea = input("Escribe la nueva tarea: ").strip()
            if nueva_tarea:
                tareas.append(nueva_tarea)
                guardar_tareas(tareas)
                print("✅ Tarea agregada correctamente.")
            else:
                print("⚠️ No puedes agregar una tarea vacía.")

        elif opcion == "2":
            if tareas:
                try:
                    indice = int(input("Número de la tarea a eliminar: ")) - 1
                    tarea_eliminada = tareas.pop(indice)
                    guardar_tareas(tareas)
                    print(f"🗑️ Tarea '{tarea_eliminada}' eliminada.")
                except (ValueError, IndexError):
                    print("❌ Número de tarea inválido. Intenta de nuevo.")
            else:
                print("No hay tareas para eliminar.")

        elif opcion == "3":
            print("¡Hasta luego, Willy! Que tengas un gran día. 👋")
            break  # Rompe el bucle y termina el programa

        else:
            print("⚠️ Opción no válida, por favor elige 1, 2 o 3.")


# Esta línea asegura que el código solo se ejecute si corremos este archivo directamente
if __name__ == "__main__":
    main()
