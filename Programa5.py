# Programa 5: Este programa identifica los alumnos que reprobaron todas las materias
# utilizando los campos "Mat_CalculoIntegral", "Mat_ProgramacionOOP", "Mat_EstructuraDatos" y "Mat_Fisica".

import pandas as pd

# Cargar los datos del archivo Excel
file_path = 'calificaciones_alumnos_actualizado.xlsx'
df = pd.read_excel(file_path)

# Identificar los alumnos que reprobaron todas las materias
df_alumnos_reprobados = df[(df['Mat_CalculoIntegral'] < 70) & (df['Mat_ProgramacionOOP'] < 70) & (df['Mat_EstructuraDatos'] < 70) & (df['Mat_Fisica'] < 70)]

# Verificar la estructura del DataFrame de alumnos reprobados
print(df_alumnos_reprobados)

# Guardar el DataFrame de alumnos reprobados en un nuevo archivo Excel
df_alumnos_reprobados.to_excel('alumnos_reprobados.xlsx', index=False)
