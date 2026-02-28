# --- REPASO 1: Fundamentos y Conversión de Tipos ---

# 1. INPUT SIEMPRE devuelve texto (str).
#    Pedimos el precio de un producto.
precio_texto = input("Ingresa el precio del producto: ")

# 2. CONVERSION (Casting).
#    Para hacer matematicas, convertimos el texto a decimal (float).
precio = float(precio_texto)

# 3. OPERACIONES ARITMETICAS.
#    Calculamos el IVA (16%).
iva = precio * 0.16
precio_final = precio + iva

# 4. SALIDA CON FORMATO (f-strings).
#    Usamos la 'f' antes de las comillas para insertar variables con {}.
#    :.2f significa "mostrar con 2 decimales".
print(f"--- Ticket de Compra ---")
print(f"Precio Base: ${precio:.2f}")
print(f"IVA (16%):   ${iva:.2f}")
print(f"TOTAL:       ${precio_final:.2f}")