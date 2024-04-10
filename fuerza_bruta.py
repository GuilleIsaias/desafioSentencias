import string

contrasena = input('Ingrese una contraseña: ')
letras = string.ascii_lowercase
compara = 0


for letra in contrasena: 
    for letter in letras:
        compara += 1
        if letra == letter:
            counttotal = compara
            print(f'La contraseña fue forzada en {counttotal} intentos.')
            break
