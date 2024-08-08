# Programa 4: Este programa identifica los alumnos con un promedio mayor a 85
# utilizando los campos "Mat_CalculoIntegral", "Mat_ProgramacionOOP", "Mat_EstructuraDatos" y "Mat_Fisica".

import pandas as pd

# Cargar los datos del archivo Excel
file_path = 'calificaciones_alumnos_actualizado.xlsx'
df = pd.read_excel(file_path)

# Calcular el promedio de calificaciones de cada alumno
df['Promedio'] = df[['Mat_CalculoIntegral', 'Mat_ProgramacionOOP', 'Mat_EstructuraDatos', 'Mat_Fisica']].mean(axis=1)

# Identificar los alumnos con un promedio mayor a 85
df_alumnos_destacados = df[df['Promedio'] > 85]

# Verificar la estructura del DataFrame de alumnos destacados
print(df_alumnos_destacados)

# Guardar el DataFrame de alumnos destacados en un nuevo archivo Excel
df_alumnos_destacados.to_excel('alumnos_destacados.xlsx', index=False)
