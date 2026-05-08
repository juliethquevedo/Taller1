usuario_correcto="admin"
contrasena_correcta="1234"
usuario=input("ingrese el usuario:")
contrasena=input("ingrese la contraseña:")
if usuario == usuario_correcto and contrasena== contrasena_correcta:
    print("Acceso permitido")
else:
    print("Usuario o contraseña incorrectos")
