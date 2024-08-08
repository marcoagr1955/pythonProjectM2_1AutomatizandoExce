# Programa 7: Este programa calcula la mediana de las calificaciones de cada materia
# utilizando los campos "Mat_CalculoIntegral", "Mat_ProgramacionOOP", "Mat_EstructuraDatos" y "Mat_Fisica".

import pandas as pd

# Cargar los datos del archivo Excel
file_path = 'calificaciones_alumnos_actualizado.xlsx'
df = pd.read_excel(file_path)

# Calcular la mediana de las calificaciones de cada materia
mediana_calificaciones = df[['Mat_CalculoIntegral', 'Mat_ProgramacionOOP', 'Mat_EstructuraDatos', 'Mat_Fisica']].median()

# Verificar la mediana de las calificaciones
print(mediana_calificaciones)

# Guardar la mediana de las calificaciones en un archivo Excel
mediana_calificaciones.to_excel('mediana_calificaciones.xlsx')
