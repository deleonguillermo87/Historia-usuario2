# Programa de inventario simple
# Este programa solicita el nombre de un producto, su precio y la cantidad disponible.

from mod_agregar import agregar_producto
from mod_mostrar import mostrar_inventario
from mod_estadistica import mostrar_estadisticas

print("=== SISTEMA DE INVENTARIO ===")

inventario = []

while True:
    # ciclo principal del programa para mostrar el menu constantemente

    print("\nopciones disponible")
    print("1. desea agregrar un producto")
    print("2. desea ver el inventario")
    print("3. desea calcular estadisticas ")
    print("4. salir...")

    opcion = input("elegir la opcion : ")

    if opcion == "1":
        # opcion para registrar un nuevo producto en el inventario
        agregar_producto(inventario)

    elif opcion == "2":
        mostrar_inventario(inventario)

    elif opcion == "3":
        mostrar_estadisticas(inventario)

    elif opcion == "4":
        print("Saliendo del sistema...")
        break

    else:
        print("Opcion no valida, intenta de nuevo")
