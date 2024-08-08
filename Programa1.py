# Programa 1: Este programa calcula el promedio de calificaciones de cada alumno
# utilizando los campos "Mat_CalculoIntegral", "Mat_ProgramacionOOP", "Mat_EstructuraDatos" y "Mat_Fisica".

import pandas as pd

# Cargar los datos del archivo Excel
file_path = 'calificaciones_alumnos_actualizado.xlsx'
df = pd.read_excel(file_path)

# Calcular el promedio de calificaciones de cada alumno
df['Promedio'] = df[['Mat_CalculoIntegral', 'Mat_ProgramacionOOP', 'Mat_EstructuraDatos', 'Mat_Fisica']].mean(axis=1)

# Verificar la estructura del DataFrame después de agregar la nueva columna
print(df.head())

# Guardar el DataFrame actualizado en un nuevo archivo Excel
df.to_excel('calificaciones_promedio.xlsx', index=False)
