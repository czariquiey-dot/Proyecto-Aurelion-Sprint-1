# Menú nivel kinder

print("Bienvenido al menú kinder!")
print("Elige una opción:")
print("1.Problema por investigar en Aurelion")
print("2. Dataset")
print("3. Pseudocodigo y Diagrama de flujo")
print("4. Sugerencias y mejoras aplicadas con Copilot")
print("0. Salir")

while True:
    opcion = input("Escribe el número de tu opción: ")
    if opcion == "0":
        print("¡Adiós! Que tengas un día bonito.")
        break
    elif opcion == "1":
        print("Investigar como varia el consumo dependiendo del medio de pago y el lugar de residencia")
    elif opcion == "2":
        print("DOCUMENTACION.md:")
        with open("DOCUMENTACION.md", "r") as archivo:
            contenido = archivo.read()
            print(contenido)
        print(".")
    elif opcion == "3":
        print("Pseudocódigo y Diagrama de flujo se encuentran en los archivos correspondientes del proyecto.")
        with open("menu_kinder_pseudocodigo.md", "r") as archivo:
            contenido = archivo.read()
            print(contenido)
        with open("menu_kinder_diagrama.md", "r") as archivo:
            contenido = archivo.read()
            print(contenido)
    elif opcion == "4":
        print("Sugerencias y mejoras aplicadas con Copilot:" \
        "n- Mejora en la estructura del código para mayor claridad." \
        "n- Inclusión de mensajes más amigables para el usuario." \
        "n- Optimización del flujo de control para manejar entradas inválidas.")
    else:
        print("Opción no válida. Intenta otra vez.")
1