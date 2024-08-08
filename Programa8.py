# Programa 8: Este programa calcula la desviación estándar de las calificaciones de cada materia
# utilizando los campos "Mat_CalculoIntegral", "Mat_ProgramacionOOP", "Mat_EstructuraDatos" y "Mat_Fisica".

import pandas as pd

# Cargar los datos del archivo Excel
file_path = 'calificaciones_alumnos_actualizado.xlsx'
df = pd.read_excel(file_path)

# Calcular la desviación estándar de las calificaciones de cada materia
desviacion_estandar_calificaciones = df[['Mat_CalculoIntegral', 'Mat_ProgramacionOOP', 'Mat_EstructuraDatos', 'Mat_Fisica']].std()

# Verificar la desviación estándar de las calificaciones
print(desviacion_estandar_calificaciones)

# Guardar la desviación estándar de las calificaciones en un archivo Excel
desviacion_estandar_calificaciones.to_excel('desviacion_estandar_calificaciones.xlsx')
