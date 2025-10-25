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
    