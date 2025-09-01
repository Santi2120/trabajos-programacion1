
alfabeto = "abcdefghijklmnñopqrstuvwxyz"


corrimiento = int(input("Ingrese el corrimiento: "))


for i in range(1, 6):  # el jefe manda 5 mensajes
    mensaje = input(f"Ingrese el mensaje {i}: ")
    encriptado = ""

   
    for caracter in mensaje.lower():  
        if caracter in alfabeto:  
            
            indice = alfabeto.index(caracter)
          
            nuevo_indice = (indice + corrimiento) % 27
           
            encriptado += alfabeto[nuevo_indice]
        else:
          
            encriptado += caracter

    print(f"Mensaje {i} encriptado: {encriptado}")