# Programa 2: Este programa cuenta el número de materias aprobadas por cada alumno
# utilizando los campos "Mat_CalculoIntegral", "Mat_ProgramacionOOP", "Mat_EstructuraDatos" y "Mat_Fisica".

import pandas as pd

# Cargar los datos del archivo Excel
file_path = 'calificaciones_alumnos_actualizado.xlsx'
df = pd.read_excel(file_path)

# Contar el número de materias aprobadas por cada alumno
df['Materias_Aprobadas'] = (df[['Mat_CalculoIntegral', 'Mat_ProgramacionOOP', 'Mat_EstructuraDatos', 'Mat_Fisica']] >= 70).sum(axis=1)

# Verificar la estructura del DataFrame después de agregar la nueva columna
print(df.head())

# Guardar el DataFrame actualizado en un nuevo archivo Excel
df.to_excel('calificaciones_materias_aprobadas.xlsx', index=False)
