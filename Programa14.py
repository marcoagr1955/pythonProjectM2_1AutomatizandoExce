# Programa 14: Este programa crea una tabla que muestra los alumnos con calificaciones sobresalientes (mayores a 90) en cualquier materia
# utilizando los campos "Mat_CalculoIntegral", "Mat_ProgramacionOOP", "Mat_EstructuraDatos" y "Mat_Fisica".

import pandas as pd

# Cargar los datos del archivo Excel
file_path = 'calificaciones_alumnos_actualizado.xlsx'
df = pd.read_excel(file_path)

# Crear una tabla que muestra los alumnos con calificaciones sobresalientes en cualquier materia
alumnos_sobresalientes = df[(df['Mat_CalculoIntegral'] > 90) | (df['Mat_ProgramacionOOP'] > 90) | (df['Mat_EstructuraDatos'] > 90) | (df['Mat_Fisica'] > 90)]

# Verificar la tabla de alumnos sobresalientes
print(alumnos_sobresalientes)

# Guardar la tabla de alumnos sobresalientes en un archivo Excel
alumnos_sobresalientes.to_excel('alumnos_sobresalientes.xlsx', index=False)
