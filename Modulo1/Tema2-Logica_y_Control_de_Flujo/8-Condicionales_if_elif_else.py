# --- Condicionales if, elif, else ---

edad = int(input("Introduce tu edad: "))

# El programa evalúa la condición. Si es True, ejecuta el código indentado.
if edad >= 18:
    print("Eres mayor de edad.")

# 'elif' (else if) nos permite evaluar una segunda condición si la primera fue falsa.
elif edad > 12:
    print("Eres un adolescente.")

# 'else' se ejecuta si NINGUNA de las condiciones anteriores fue verdadera.
else:
    print("Eres un niño.")

print("Fin del programa.") # Esta línea se ejecuta siempre, al no estar indentada.