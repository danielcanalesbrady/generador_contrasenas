from generador import generar_contrasena

def iniciar():
    try:
        longitud = int(input("¿Cuántos caracteres quieres en tu contraseña?: "))
        if longitud < 4:
            print("La contraseña debe tener al menos 4 caracteres.")
            return
        contrasena = generar_contrasena(longitud)
        print("Tu contraseña segura es:", contrasena)
    except ValueError:
        print("Por favor ingresa un número válido.")

iniciar()
