# --- 8. Lanzar errores con 'raise' ---

def registrar_usuario(nombre, edad):
    # VALIDACION DE LOGICA DE NEGOCIO
    if edad < 0:
        # 'raise' nos permite DETENER el programa y lanzar un error manualmente.
        # Usamos ValueError porque el valor es inaceptable.
        raise ValueError("La edad no puede ser negativa.")
    
    if len(nombre) < 2:
        raise ValueError("El nombre es demasiado corto.")
        
    print(f"Usuario {nombre} registrado con exito.")

# --- Prueba ---
try:
    registrar_usuario("A", 20) # Esto detonara el 'raise'
except ValueError as e:
    # Aqui atrapamos nuestro propio error lanzado manualmente
    print(f"Error de registro: {e}")