# Pido la fecha
fecha = input("Ingrese la fecha actual en formato dia, DD/MM: ")

# Separo el día de la fecha
partes = fecha.split(",")
if len(partes) != 2:
    print("Error en el formato")
else:
    dia_semana = partes[0].strip().lower()
    fecha_numeros = partes[1].strip().split("/")

    if len(fecha_numeros) != 2:
        print("Error en el formato")
    else:
        dia = int(fecha_numeros[0])
        mes = int(fecha_numeros[1])

        if dia < 1 or dia > 31 or mes < 1 or mes > 12:
            print("Error en el dia o mes")
        else:
            if dia_semana == "lunes":
                print("Hoy toca nivel inicial")
                examenes = input("¿Hubo examenes? si/no: ")
                if examenes == "si":
                    aprobados = int(input("Cuantos aprobaron: "))
                    desaprobados = int(input("Cuantos no aprobaron: "))
                    total = aprobados + desaprobados
                    if total > 0:
                        porcentaje = (aprobados * 100) / total
                        print("El porcentaje de aprobados es:", porcentaje, "%")
                    else:
                        print("No hubo alumnos")

            elif dia_semana == "martes":
                print("Hoy toca nivel intermedio")
                examenes = input("¿Hubo examenes? si/no: ")
                if examenes == "si":
                    aprobados = int(input("Cuantos aprobaron: "))
                    desaprobados = int(input("Cuantos no aprobaron: "))
                    total = aprobados + desaprobados
                    if total > 0:
                        porcentaje = (aprobados * 100) / total
                        print("El porcentaje de aprobados es:", porcentaje, "%")
                    else:
                        print("No hubo alumnos")

            elif dia_semana == "miercoles" or dia_semana == "miércoles":
                print("Hoy toca nivel avanzado")
                examenes = input("¿Hubo examenes? si/no: ")
                if examenes == "si":
                    aprobados = int(input("Cuantos aprobaron: "))
                    desaprobados = int(input("Cuantos no aprobaron: "))
                    total = aprobados + desaprobados
                    if total > 0:
                        porcentaje = (aprobados * 100) / total
                        print("El porcentaje de aprobados es:", porcentaje, "%")
                    else:
                        print("No hubo alumnos")

            elif dia_semana == "jueves":
                print("Hoy toca practica hablada")
                asistencia = int(input("Ingrese porcentaje de asistencia: "))
                if asistencia > 50:
                    print("Asistio la mayoria")
                else:
                    print("No asistio la mayoria")

            elif dia_semana == "viernes":
                print("Hoy toca ingles para viajeros")
                if dia == 1 and (mes == 1 or mes == 7):
                    print("Comienzo de nuevo ciclo")
                    alumnos = int(input("Cuantos alumnos hay: "))
                    arancel = float(input("Cuanto paga cada uno: "))
                    ingreso = alumnos * arancel
                    print("El ingreso total es:", ingreso)

            else:
                print("Error en el dia de la semana")
