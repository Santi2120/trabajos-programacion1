# EJERCICIO 1
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300
print(precios_frutas)
print("-" * 50)

# EJERCICIO 2
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800
print(precios_frutas)
print("-" * 50)

# EJERCICIO 3
lista_frutas = list(precios_frutas.keys())
print(lista_frutas)
print("-" * 50)

# EJERCICIO 4
contactos = {}
for i in range(5):
    nombre = input(f"Ingrese el nombre del contacto {i+1}: ")
    numero = input("Ingrese el número telefónico: ")
    contactos[nombre] = numero
nombre_buscar = input("Ingrese el nombre del contacto a buscar: ")
if nombre_buscar in contactos:
    print(f"El número de {nombre_buscar} es {contactos[nombre_buscar]}")
else:
    print("El contacto no existe.")
print("-" * 50)

# EJERCICIO 5
frase = input("Ingrese una frase: ").lower()
palabras = frase.split()
palabras_unicas = set(palabras)
frecuencia = {}
for palabra in palabras:
    frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
print(palabras_unicas)
print(frecuencia)
print("-" * 50)

# EJERCICIO 6
alumnos = {}
for i in range(3):
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
    notas = []
    for j in range(3):
        nota = float(input(f"Ingrese la nota {j+1} de {nombre}: "))
        notas.append(nota)
    alumnos[nombre] = tuple(notas)
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}")
print("-" * 50)

# EJERCICIO 7
parcial1 = {"Ana", "Luis", "María", "Pedro"}
parcial2 = {"María", "Pedro", "Lucía", "Jorge"}
ambos = parcial1 & parcial2
solo_uno = parcial1 ^ parcial2
al_menos_uno = parcial1 | parcial2
print(ambos)
print(solo_uno)
print(al_menos_uno)
print("-" * 50)

# EJERCICIO 8
productos = {"Arroz": 10, "Fideos": 20, "Aceite": 5}
producto = input("Ingrese el nombre del producto: ")
if producto in productos:
    print(productos[producto])
    agregar = int(input("¿Cuántas unidades desea agregar?: "))
    productos[producto] += agregar
else:
    nuevo_stock = int(input("Producto no encontrado. Ingrese el stock inicial: "))
    productos[producto] = nuevo_stock
print(productos)
print("-" * 50)

# EJERCICIO 9
agenda = {
    ("Lunes", "10:00"): "Reunión de trabajo",
    ("Martes", "15:00"): "Clase de programación",
    ("Viernes", "19:00"): "Cena con amigos"
}
dia = input("Ingrese el día: ").capitalize()
hora = input("Ingrese la hora (HH:MM): ")
if (dia, hora) in agenda:
    print(agenda[(dia, hora)])
else:
    print("No hay actividades.")
print("-" * 50)

# EJERCICIO 10
paises_capitales = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Uruguay": "Montevideo",
    "Brasil": "Brasilia"
}
capitales_paises = {capital: pais for pais, capital in paises_capitales.items()}
print(capitales_paises)
print("-" * 50)
