# Programa 6: Este programa calcula la media de las calificaciones de cada materia
# utilizando los campos "Mat_CalculoIntegral", "Mat_ProgramacionOOP", "Mat_EstructuraDatos" y "Mat_Fisica".

import pandas as pd

# Cargar los datos del archivo Excel
file_path = 'calificaciones_alumnos_actualizado.xlsx'
df = pd.read_excel(file_path)

# Calcular la media de las calificaciones de cada materia
media_calificaciones = df[['Mat_CalculoIntegral', 'Mat_ProgramacionOOP', 'Mat_EstructuraDatos', 'Mat_Fisica']].mean()

# Verificar la media de las calificaciones
print(media_calificaciones)

# Guardar la media de las calificaciones en un archivo Excel
media_calificaciones.to_excel('media_calificaciones.xlsx')
