from estudiantes.registro import cargar_estudiantes, mostrar_tabla, calcular_promedio

def main():
    estudiantes = cargar_estudiantes("estudiantes.csv")
    mostrar_tabla(estudiantes)
    promedio = calcular_promedio(estudiantes)
    print(f"\nPromedio general: {promedio:.2f}")

if __name__ == "__main__":
    main()
