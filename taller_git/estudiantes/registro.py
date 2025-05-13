import csv

def cargar_estudiantes(ruta_csv):
    estudiantes = []
    with open(ruta_csv, newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            try:
                nota = float(fila["nota"])
                if 0.0 <= nota <= 5.0:
                    estudiantes.append({"nombre": fila["nombre"], "nota": nota})
            except ValueError:
                continue
    return estudiantes

def mostrar_tabla(estudiantes):
    estudiantes_ordenados = sorted(estudiantes, key=lambda e: e["nombre"])
    print(f"{'Nombre':<10} | {'Nota':<5}")
    print("-" * 18)
    for e in estudiantes_ordenados:
        print(f"{e['nombre']:<10} | {e['nota']:<5.1f}")

def calcular_promedio(estudiantes):
    if not estudiantes:
        return 0.0
    total = sum(e["nota"] for e in estudiantes)
    promedio = total / len(estudiantes)
    return round(promedio, 2)
