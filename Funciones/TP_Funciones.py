
# -------------------------------
# Ejercicio 1
# -------------------------------
def imprimir_hola_mundo():
    print("Hola Mundo!")

# Llamada a la función
imprimir_hola_mundo()


# -------------------------------
# Ejercicio 2
# -------------------------------
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

nombre_usuario = input("\nEjercicio 2 - Ingrese su nombre: ")
print(saludar_usuario(nombre_usuario))


# -------------------------------
# Ejercicio 3
# -------------------------------
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

nombre = input("\nEjercicio 3 - Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")

informacion_personal(nombre, apellido, edad, residencia)


# -------------------------------
# Ejercicio 4
# -------------------------------
import math

def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

radio = float(input("\nEjercicio 4 - Ingrese el radio del círculo: "))
print(f"Área: {calcular_area_circulo(radio):.2f}")
print(f"Perímetro: {calcular_perimetro_circulo(radio):.2f}")


# -------------------------------
# Ejercicio 5
# -------------------------------
def segundos_a_horas(segundos):
    return segundos / 3600

segundos = int(input("\nEjercicio 5 - Ingrese la cantidad de segundos: "))
print(f"Equivale a {segundos_a_horas(segundos):.2f} horas.")


# -------------------------------
# Ejercicio 6
# -------------------------------
def tabla_multiplicar(numero):
    print(f"\nTabla del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

numero = int(input("\nEjercicio 6 - Ingrese un número para ver su tabla: "))
tabla_multiplicar(numero)


# -------------------------------
# Ejercicio 7
# -------------------------------
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "No se puede dividir por cero"
    return suma, resta, multiplicacion, division

a = float(input("\nEjercicio 7 - Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))

resultados = operaciones_basicas(a, b)
print(f"Suma: {resultados[0]}, Resta: {resultados[1]}, Multiplicación: {resultados[2]}, División: {resultados[3]}")


# -------------------------------
# Ejercicio 8
# -------------------------------
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

peso = float(input("\nEjercicio 8 - Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
print(f"Su IMC es: {calcular_imc(peso, altura):.2f}")


# -------------------------------
# Ejercicio 9
# -------------------------------
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

temp_celsius = float(input("\nEjercicio 9 - Ingrese la temperatura en °C: "))
print(f"Equivale a {celsius_a_fahrenheit(temp_celsius):.2f} °F.")


# -------------------------------
# Ejercicio 10
# -------------------------------
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

a = float(input("\nEjercicio 10 - Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
c = float(input("Ingrese el tercer número: "))

print(f"El promedio es: {calcular_promedio(a, b, c):.2f}")

# ======================================================
# Fin del TP
# ======================================================
