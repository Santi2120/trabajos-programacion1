from funciones_paises import (
    cargar_datos,
    buscar_pais,
    filtrar_por_continente,
    filtrar_por_rango,
    ordenar_paises,
    estadisticas,
    mostrar_paises,
)


def menu():
    paises = cargar_datos("paises.csv")
    if not paises:
       return
    
while True:
    print("\n ==== MENU DE GESTION DE PAISES ====")
    print("1. Buscar pais por nombre")
    print("2. Filtrar paises por continente")
    print("3. Filtrar paises por rango de poblacion")
    print("4. Filtrar paises por rango de superficie")
    print("5. Ordenar paises")
    print("6. Mostrar estadisticas")
    print("7. Salir")

    opcion = input("Seleccione una opcion: ")

    match opcion:
        case "1":
            nombre = input("Ingrese el nombre del pais a buscar: ")
            mostrar_paises(buscar_pais(paises, nombre))


        case "2":
            continente = input("Ingrese el continente: ")
            mostrar_paises(filtrar_por_continente(paises, continente))

        case "3":
            try: 
                main_p = int(input("Poblacion minima: "))
                max_p = int(input("Poblacion maxima: "))
                mostrar_paises(filtrar_por_rango(paises, "superficie", min_s, max_s))
            except ValueError:
                print(" Ingrese valores numericos validos.")                
        case "4":
                try:
                    min_s = int(input("Superficie mínima: "))
                    max_s = int(input("Superficie máxima: "))
                    mostrar_paises(filtrar_por_rango(paises, "superficie", min_s, max_s))
                except ValueError:
                    print("⚠️ Ingrese valores numéricos válidos.")

        case "5":
                campo = input("Campo para ordenar (nombre/poblacion/superficie): ").lower()
                descendente = input("¿Orden descendente? (s/n): ").lower() == "s"
                if campo in ["nombre", "poblacion", "superficie"]:
                    mostrar_paises(ordenar_paises(paises, campo, descendente))
                else:
                    print("Campo no válido.")

        case "6":
                e = estadisticas(paises)
                if e:
                    print(f"\nPaís con mayor población: {e['mayor_poblacion']['nombre']}")
                    print(f"País con menor población: {e['menor_poblacion']['nombre']}")
                    print(f"Promedio de población: {e['promedio_poblacion']:.2f}")
                    print(f"Promedio de superficie: {e['promedio_superficie']:.2f}")
                    print("Cantidad de países por continente:")
                    for cont, cant in e["cantidad_por_continente"].items():
                        print(f"  {cont}: {cant}")

        case "7":
                print(" Saliendo del programa... ¡Hasta luego!")
                break

        case _:
                print(" Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    menu()