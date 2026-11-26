def saludar(nombre_completo):
    if not nombre_completo or not nombre_completo.strip():
        raise ValueError("El nombre no puede estar vacío")
    return f"Hola {nombre_completo.strip()}"


print(saludar("GitHub"))