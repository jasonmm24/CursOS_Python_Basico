print("\n--- 4. Alcance de Variables (Scope) ---")

# 1. VARIABLE GLOBAL:
# Esta variable esta definida 'fuera' de cualquier funcion.
# Es accesible desde cualquier parte del codigo (globalmente).
variable_global = "Soy GLOBAL"

def funcion_de_prueba():
    # 2. VARIABLE LOCAL:
    # Esta variable esta definida 'dentro' de la funcion.
    # Solo existe y es accesible DENTRO de esta funcion.
    variable_local = "Soy LOCAL"
    
    #global variable_global
    #variable_global = "He sido modificada"
    
    print(f"Dentro de la funcion, puedo ver la variable {variable_local}")
    print(f"Dentro de la funcion, tambien puedo leer la variable {variable_global}")
    
    # 3. Modificar una variable global (requiere la palabra 'global')
    

# 4. Llamamos a la funcion
print("Llamando a la funcion:")
funcion_de_prueba()

# 5. Verificamos el alcance fuera de la funcion
print("\nFuera de la funcion:")
print(f"Puedo ver la variable {variable_global}")

# 6. ¡Esto dara un error!
# La 'variable_local' no existe aqui fuera. Su "scope" termino
# cuando la funcion finalizo.
# Si descomentas la linea de abajo, el programa fallara.

#print(variable_local)
# Genera: NameError: name 'variable_local' is not defined