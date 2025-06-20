import random
import string

def generador_contrasena(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena =''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena