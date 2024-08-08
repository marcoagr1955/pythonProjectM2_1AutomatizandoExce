# Programa 9: Este programa identifica la calificación más alta y más baja de cada materia
# utilizando los campos "Mat_CalculoIntegral", "Mat_ProgramacionOOP", "Mat_EstructuraDatos" y "Mat_Fisica".

import pandas as pd

# Cargar los datos del archivo Excel
file_path = 'calificaciones_alumnos_actualizado.xlsx'
df = pd.read_excel(file_path)

# Identificar la calificación más alta y más baja de cada materia
max_calificaciones = df[['Mat_CalculoIntegral', 'Mat_ProgramacionOOP', 'Mat_EstructuraDatos', 'Mat_Fisica']].max()
min_calificaciones = df[['Mat_CalculoIntegral', 'Mat_ProgramacionOOP', 'Mat_EstructuraDatos', 'Mat_Fisica']].min()

# Verificar la calificación más alta y más baja de cada materia
print(f'Calificaciones más altas:\n{max_calificaciones}')
print(f'Calificaciones más bajas:\n{min_calificaciones}')

# Guardar las calificaciones más altas y más bajas en un
