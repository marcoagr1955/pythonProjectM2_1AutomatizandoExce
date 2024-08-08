# Programa 13: Este programa crea una tabla pivot que muestra el promedio de calificaciones por alumno y materia
# utilizando los campos "Mat_CalculoIntegral", "Mat_ProgramacionOOP", "Mat_EstructuraDatos" y "Mat_Fisica".

import pandas as pd

# Cargar los datos del archivo Excel
file_path = 'calificaciones_alumnos_actualizado.xlsx'
df = pd.read_excel(file_path)

# Crear una tabla pivot para promedio de calificaciones por alumno y materia
pivot_table = pd.pivot_table(df, values=['Mat_CalculoIntegral', 'Mat_ProgramacionOOP', 'Mat_EstructuraDatos', 'Mat_Fisica'], index='Nombre', aggfunc='mean')

# Verificar la tabla pivot
print(pivot_table)

# Guardar la tabla pivot en un archivo Excel
pivot_table.to_excel('tabla_pivot_promedio_calificaciones.xlsx')
