CONFIG_TIENDA = ("TechStore", 0.16)  # Nombre de la tienda y tasa de IVA (16%)

#Diccionario de productos (`inventario`):

inventario = {
    "P01": {
        "nombre": "Teclado Mecánico",
        "precio": 45.0,
        "stock": 10,
        "categoria": "Periféricos",
    },
    "P02": {
        "nombre": "Mouse Gamer",
        "precio": 25.0,
        "stock": 15,
        "categoria": "Periféricos",
    },
    "P03": {
        "nombre": "Monitor 24''",
        "precio": 130.0,
        "stock": 5,
        "categoria": "Pantallas",
    },
    "P04": {
        "nombre": "Cable HDMI",
        "precio": 8.0,
        "stock": 20,
        "categoria": "Accesorios",
    },
}      


def mostrar_inventario(inventario):
    print(f"\n--- INVENTARIO {CONFIG_TIENDA[0]} ---")

    # 1. Recorremos cada producto
    for codigo, datos in inventario.items():
        print(
            f"[{codigo}] {datos['nombre']} | Precio: ${datos['precio']} | Stock:"
            f" {datos['stock']} | Cat: {datos['categoria']}"
        )

    # 2. Extraemos las categorías sin duplicados usando un set
    # ¿Te acuerdas de la comprensión de listas? ¡Esto es una comprensión de set!
    categorias = {datos["categoria"] for datos in inventario.values()}
    print("-" * 40)
    print(f"Categorías disponibles: {categorias}")

def realizar_venta(inventario):
    carrito = []

    #Bucle de compra interactiva
    while True:
        codigo = input("\nIngrese el código del producto ('FIN' para terminar): ").upper()
        
        # Si escribe FIN, salimos del bucle
        if codigo == "FIN":
            break

        #Validación 1 ¿El código existe en la tienda?
        if codigo in inventario:
            producto = inventario[codigo]
            print(
                f"✅ Seleccionaste: {producto['nombre']} (Stock disponible:"
                f" {producto['stock']})"
                )
            # 1. Preguntamos la cantidad 
            cantidad = int(input(f"¿Cuántas unidades deseas llevar?: "))

            # 2. ¿Pide más de lo que tenemos? # Validación de stock con if/elseP02

            if cantidad > producto["stock"]:
                print(f"⚠️ No hay suficiente stock. Solo quedan {producto['stock']} unidades.")

            # 3. Si hay suficiente: restamos del stock disponible
            else:
                producto["stock"] -= cantidad
                subtotal = cantidad * producto["precio"] # 4. Lo metemos a la lista del carrito con un diccionario
                carrito.append({
                            "nombre": producto["nombre"],
                            "cantidad": cantidad,
                            "subtotal": subtotal,
                            })
                print(f"🛒 ¡Agregado al carrito! Subtotal: ${subtotal}")
        else:
        # Si el código no estaba en el inventario:
            print("❌ Ese código no existe. Intenta de nuevo.")

    # Este print va AQUÍ, cuando el usuario escribe FIN y termina el while
    print("\n👋 Saliste de la compra.")

    # --- SECCIÓN DEL TICKET (4 espacios por estar dentro de la función) ---
    if not carrito:
        print("🛒 El carrito está vacío. No se realizó ninguna compra.")
    else:
        print("\n========================================")
        print(f"     TICKET DE COMPRA - {CONFIG_TIENDA[0]}")
        print("========================================")

        total_neto = 0.0
        for item in carrito:
            print(f"• {item['nombre']} x{item['cantidad']} -> ${item['subtotal']}")
            total_neto += item["subtotal"]  # 8 espacios (DENTRO del for)

        iva = total_neto * CONFIG_TIENDA[1]
        total_final = total_neto + iva


        print("-" * 40)
        print(f"Subtotal Neto: ${total_neto:.2f}")
        print(f"IVA ({int(CONFIG_TIENDA[1]*100)}%):    ${iva:.2f}")
        print(f"TOTAL A PAGAR:  ${total_final:.2f}")
        print("========================================")

    return carrito


# Pruebas:
mostrar_inventario(inventario)
mi_carrito = realizar_venta(inventario)

