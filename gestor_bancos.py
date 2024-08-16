import clase # __init__.py (archivo vacio en directorio del cual queremos traer un modulo)

banco = clase.Banco("Info")
opcion = 1
contrasenia = "1234"
guirnarlda = "*" * 30

while opcion != 0:
    print(guirnarlda)
    print("Seleccione una opcion:\n1. Crear cuenta\n2. Modificar cuenta")
    print("3. Eliminar cuenta\n4. Ver cuentas\n0. Salir")
    print(guirnarlda)
    opcion = int(input())
    print(guirnarlda)

    if opcion == 1: #crear cuenta
        #Crear validaciones necesarias para crear cuentas (No tener nombres repetidos)
        pass
    elif opcion == 2: #operaciones con cuentas
        #Ver de desarrollar un submenu para distintas opciones de modificacion de cuenta
        pass
    elif opcion == 3: #eliminar cuenta
        #Validar y confirmar elminacion antes de borrar
        pass
    elif opcion == 4: #ver cuentas
        #Ver cuentas
        pass
    elif opcion == 0:
        break
    