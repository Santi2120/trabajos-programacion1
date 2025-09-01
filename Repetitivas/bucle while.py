    #bucle while
    
import random

puntaje_jugador = 0
puntaje_computadora = 0

while True:
    print("\n--- JUEGO: PIEDRA, PAPEL O TIJERA ---")
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")
    print("4. Salir")

    eleccion = input("Elige una opción (1-4): ")

    if eleccion == "4":
        print("\nJuego terminado.")
        print("Marcador final -> Jugador:", puntaje_jugador, "| Computadora:", puntaje_computadora)
        if puntaje_jugador > puntaje_computadora:
            print(" ¡Ganaste el juego!")
        elif puntaje_jugador < puntaje_computadora:
            print(" La computadora ganó el juego.")
        else:
            print(" El juego terminó en empate.")
        break

    if eleccion == "1":
        jugador = "piedra"
    elif eleccion == "2":
        jugador = "papel"
    elif eleccion == "3":
        jugador = "tijera"
    else:
        print(" Opción inválida. Intenta de nuevo.")
        continue

    
    num = random.randint(1, 3)
    if num == 1:
        computadora = "piedra"
    elif num == 2:
        computadora = "papel"
    else:
        computadora = "tijera"

    print("\n Tú elegiste:", jugador)
    print(" La computadora eligió:", computadora)

    
    if jugador == computadora:
        print(" ¡Empate!")
    elif jugador == "piedra" and computadora == "tijera":
        print(" ¡Ganaste esta ronda!")
        puntaje_jugador = puntaje_jugador + 1
    elif jugador == "tijera" and computadora == "papel":
        print(" ¡Ganaste esta ronda!")
        puntaje_jugador = puntaje_jugador + 1
    elif jugador == "papel" and computadora == "piedra":
        print(" ¡Ganaste esta ronda!")
        puntaje_jugador = puntaje_jugador + 1
    else:
        print(" La computadora gana esta ronda.")
        puntaje_computadora = puntaje_computadora + 1

    print("Marcador -> Jugador:", puntaje_jugador, "| Computadora:", puntaje_computadora)
