from generador import generar_contrasena

def guardar_en_archivo(contrasena):
    with open("contrasenas_generadas.txt", "a") as archivo:
        archivo.write(contrasena + "\n")

def iniciar():
    try:
        longitud = int(input("¿Cuántos caracteres quieres en tu contraseña?: "))
        if longitud < 4:
            print("La contraseña debe tener al menos 4 caracteres.")
            return
        contrasena = generar_contrasena(longitud)
        print("Tu contraseña segura es:", contrasena)

        guardar_en_archivo(contrasena)
        print("Contraseña guardada en 'contrasenas_generadas.txt'.")

    except ValueError:
        print("Por favor ingresa un número válido.")

iniciar()
