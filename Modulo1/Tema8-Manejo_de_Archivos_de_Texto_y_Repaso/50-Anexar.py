# --- CODIGO 3: Agregar informacion (Modo 'a') ---

print("Agregando una nueva entrada al diario...")

# 1. Abrimos en modo 'a' (Append).
#    El 'cursor' de escritura se coloca automaticamente al final del archivo.
with open("Ensayo_Escuela_Botes.txt", "a", encoding="utf-8") as archivo:
    
    # 2. Escribimos una linea nueva.
    #    Es buena practica empezar con '\n' para asegurarnos de que
    #    no quede pegado a la ultima linea anterior.
    archivo.write("\n\n Puedo Hacerlo!")
    archivo.write("\n Porque hace tanto calor aqui")
    archivo.write("\n ah mi mano, mi mano se esta acalambrando...")

print("Informacion agregada.")