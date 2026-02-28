# --- REPASO 2: Condicionales (Lógica Booleana) ---

# Solicitamos la edad (convertimos a entero de una vez)
edad = int(input("¿Cuántos años tienes? "))

# Evaluamos las condiciones en orden descendente o especifico.
if edad >= 18:
    # Se ejecuta si la condicion es VERDADERA (True)
    print("Eres mayor de edad. Puedes votar y conducir.")
    
    # Podemos anidar un if dentro de otro
    if edad >= 65:
        print("¡Y también tienes descuentos de jubilado!")

elif edad >= 13:
    # Se ejecuta solo si el primer 'if' fue FALSO
    print("Eres un adolescente.")

else:
    # Se ejecuta si NINGUNA de las anteriores fue verdadera
    print("Eres un niño.")