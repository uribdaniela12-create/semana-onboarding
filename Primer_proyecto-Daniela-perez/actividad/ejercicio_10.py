usuario_resgistrado = "salome7"
contraseña_registrada= "Salome4218*"
usuario = input("ponga su usurio: ")
contraseña= input("digite su contraseña: ")

if usuario and contraseña == (usuario_resgistrado and contraseña_registrada):
    print("el usuario y contraseña son correctas")
else:
    print("el usuario o contraseña son incorrectas")

