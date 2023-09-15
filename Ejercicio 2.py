import numpy as np


estudiantes = np.array([
    (1, "Estudiante1", 1985, 4.5, "X", False),# array para los estudiantes agregables
    (2, "Estudiante2", 1992, 3.2, "Y", True),
    (3, "Estudiante3", 1989, 4.8, "X", True),
    (4, "Estudiante4", 1987, 3.7, "X", False),



], dtype=[('codigo', int), ('nombre', 'U20'), ('anio_ingreso', int), ('promedio_acumulado', float), ('carrera', 'U10'), ('condicional', bool)])

# Estudiantes de la carrera X con promedio acumulado >= 4
carrera_a_buscar = input("Ingrese el código de la carrera a listar: ")
promedio_minimo = 4.0

filtro_carrera_promedio = (estudiantes['carrera'] == carrera_a_buscar) & (estudiantes['promedio_acumulado'] >= promedio_minimo)
estudiantes_carrera_x = estudiantes[filtro_carrera_promedio]

print(f"\nEstudiantes de la carrera {carrera_a_buscar} con promedio acumulado >= {promedio_minimo}:")
for estudiante in estudiantes_carrera_x:
    print(f"Código: {estudiante['codigo']}, Nombre: {estudiante['nombre']}")

print(f"Total de estudiantes en esta categoría: {len(estudiantes_carrera_x)}")

# Estudiantes que ingresaron antes de 1990 y están condicionales
anio_limite = 1990

filtro_ingreso_condicional = (estudiantes['anio_ingreso'] < anio_limite) & (estudiantes['condicional'] == True)
estudiantes_condicionales_anterior_1990 = estudiantes[filtro_ingreso_condicional]

print("\nEstudiantes que ingresaron antes de 1990 y están condicionales:")
for estudiante in estudiantes_condicionales_anterior_1990:
    print(f"Código: {estudiante['codigo']}, Nombre: {estudiante['nombre']}")
