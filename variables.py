import os

# Constante: Nombre del archivo y el símbolo de completado
ARCHIVO_TAREAS = "tareas.txt"
SIMBOLO_COMPLETADO = "✅ "


def cargar_tareas():
    """Lee las tareas desde el archivo de texto."""
    if not os.path.exists(ARCHIVO_TAREAS):
        return []

    with open(ARCHIVO_TAREAS, "r", encoding="utf-8") as archivo:
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

    while True:
        mostrar_tareas(tareas)
        # Actualizamos el menú con la nueva opción
        print("Opciones: [1] Agregar  [2] Eliminar  [3] Completar  [4] Salir")
        opcion = input("Elige una opción (1/2/3/4): ").strip()

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

        # --- 🌟 NUEVA OPCIÓN: COMPLETAR TAREA 🌟 ---
        elif opcion == "3":
            if tareas:
                try:
                    indice = int(input("Número de la tarea a completar: ")) - 1
                    tarea = tareas[indice]

                    # Verificamos si ya tiene el símbolo de completado
                    if not tarea.startswith(SIMBOLO_COMPLETADO):
                        # Le agregamos el símbolo al inicio
                        tareas[indice] = SIMBOLO_COMPLETADO + tarea
                        guardar_tareas(tareas)
                        print(
                            f"🎉 ¡Felicidades! Tarea '{tarea}' marcada como completada."
                        )
                    else:
                        print("⚠️ Esta tarea ya estaba completada. ¡Buen trabajo!")

                except (ValueError, IndexError):
                    print("❌ Número de tarea inválido. Intenta de nuevo.")
            else:
                print("No hay tareas para completar.")
        # ------------------------------------------------

        elif opcion == "4":  # Cambiado de 3 a 4
            print("¡Hasta luego, Willy! Que tengas un gran día. 👋")
            break

        else:
            print("⚠️ Opción no válida, por favor elige 1, 2, 3 o 4.")


if __name__ == "__main__":
    main()
