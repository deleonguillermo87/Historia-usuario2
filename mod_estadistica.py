def mostrar_estadisticas(inventario):
    if len(inventario) == 0:
        print("\nNo hay productos para calcular estadisticas.")
        return

    total = len(inventario)
    suma_cantidad = 0
    valor_total = 0

    for p in inventario:
        suma_cantidad = suma_cantidad + p["cantidad"]
        valor_total = valor_total + (p["precio"] * p["cantidad"])

    print("\n=== ESTADISTICAS ===")
    print("Total de productos diferentes:", total)
    print("Total de unidades en stock:", suma_cantidad)
    print("Valor total del inventario:", valor_total)
