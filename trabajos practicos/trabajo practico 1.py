
#ejercicio 1
print("Hola Mundo!")

#ejercicio 2
nombre = input("Ingresa tu nombre: ")
print(f"Hola {nombre}!")

#ejercicio 3
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = input("Ingresa tu edad: ")
residencia = input("Ingresa tu lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

#ejercicio 4
import math
radio = float(input("Ingresa el radio del círculo: "))
area = math.pi * radio**2
perimetro = 2 * math.pi * radio
print(f"Área: {area:.2f}, Perímetro: {perimetro:.2f}")

#ejercicio 5
segundos = int(input("Ingresa una cantidad de segundos: "))
horas = segundos / 3600
print(f"{segundos} segundos equivalen a {horas:.2f} horas.")

#ejercicio 6
numero = int(input("Ingresa un número: "))
print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

#ejercicio 7
a = int(input("Ingresa el primer número entero (≠ 0): "))
b = int(input("Ingresa el segundo número entero (≠ 0): "))
print(f"Suma: {a + b}")
print(f"Resta: {a - b}")
print(f"Multiplicación: {a * b}")
print(f"División: {a / b}")

#ejercicio 8
peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en metros: "))
imc = peso / (altura ** 2)
print(f"Tu IMC es: {imc:.2f}")

#ejercicio 9
celsius = float(input("Ingresa la temperatura en grados Celsius: "))
fahrenheit = (9/5) * celsius + 32
print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F")

#ejercicio 10
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
num3 = float(input("Ingresa el tercer número: "))
promedio = (num1 + num2 + num3) / 3
print(f"El promedio es: {promedio:.2f}")
