usuario_correcto = "Julieth"
contraseña_correcta = "1234"
rol_correcto = "admin"
usuario=input("usuario:")
contraseña=input("contraseña:")
rol=input("rol:")
if usuario == usuario_correcto and contraseña == contraseña_correcta and rol == rol_correcto:
    print("Acceso permitido")
else:
    print("Acceso denegado")
