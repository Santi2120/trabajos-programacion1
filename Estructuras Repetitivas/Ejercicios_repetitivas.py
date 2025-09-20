#ejercicio 1
for i in range(101):
    print(i)

#ejercicio 2
numero = int(input("Ingrese un número entero: "))
cantidad_digitos = len(str(numero))
print(f"El número ingresado tiene {cantidad_digitos} dígitos.")

#ejercicio 3
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
suma = 0

if num1 > num2:
    num1, num2 = num2, num1

for i in range(num1 + 1, num2):
    suma += i

print(f"La suma de los números entre {num1} y {num2} es: {suma}")

#ejercicio 4
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
suma = 0

if num1 > num2:
    num1, num2 = num2, num1

for i in range(num1 + 1, num2):
    suma += i

print(f"La suma de los números entre {num1} y {num2} es: {suma}")

#ejercicio 5
import random

numero_secreto = random.randint(0, 9)
intentos = 0

while True:
    try:
        suposicion = int(input("Adivina el número entre 0 y 9: "))
        intentos += 1
        if suposicion == numero_secreto:
            print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
            break
        elif suposicion < numero_secreto:
            print("El número es mayor.")
        else:
            print("El número es menor.")
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número entero.")

#ejercicio 6
for i in range(100, -1, -2):
    print(i)

#ejercicio 7
numero_final = int(input("Ingrese un número entero positivo: "))
suma = 0

for i in range(numero_final + 1):
    suma += i

print(f"La suma de los números desde 0 hasta {numero_final} es: {suma}")

#ejercicio 8
cantidad_numeros = 100
pares = 0
impares = 0
positivos = 0
negativos = 0

for _ in range(cantidad_numeros):
    numero = int(input("Ingrese un número entero: "))
    
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

print(f"Números procesados: {cantidad_numeros}")
print(f"Cantidad de pares: {pares}")
print(f"Cantidad de impares: {impares}")
print(f"Cantidad de positivos: {positivos}")
print(f"Cantidad de negativos: {negativos}")


#ejercicio 9
cantidad_numeros = 100
suma = 0

for _ in range(cantidad_numeros):
    numero = int(input("Ingrese un número entero: "))
    suma += numero

media = suma / cantidad_numeros
print(f"La media de los {cantidad_numeros} números es: {media}")

#ejercicio 10
numero = input("Ingrese un número para invertir: ")
numero_invertido = numero[::-1]
print(f"El número invertido es: {numero_invertido}")

