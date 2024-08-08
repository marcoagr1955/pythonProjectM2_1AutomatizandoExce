# Programa 12: Este programa calcula el porcentaje de aprobados y reprobados por materia
# utilizando los campos "Mat_CalculoIntegral", "Mat_ProgramacionOOP", "Mat_EstructuraDatos" y "Mat_Fisica".

import pandas as pd

# Cargar los datos del archivo Excel
file_path = 'calificaciones_alumnos_actualizado.xlsx'
df = pd.read_excel(file_path)

# Calcular el porcentaje de aprobados y reprobados por materia
porcentaje_aprobados = (df[['Mat_CalculoIntegral', 'Mat_ProgramacionOOP', 'Mat_EstructuraDatos', 'Mat_Fisica']] >= 70).mean() * 100
porcentaje_reprobados = (df[['Mat_CalculoIntegral', 'Mat_ProgramacionOOP', 'Mat_EstructuraDatos', 'Mat_Fisica']] < 70).mean() * 100

# Verificar el porcentaje de aprobados y reprobados por materia
print(f'Porcentaje de Aprobados:\n{porcentaje_aprobados}')
print(f'Porcentaje de Reprobados:\n{porcentaje_reprobados}')

# Guardar el porcentaje de aprobados y reprobados en un archivo Excel
pd.DataFrame({'Aprobados': porcentaje_aprobados, 'Reprobados': porcentaje_reprobados}).to_excel('porcentaje_aprobados_reprobados.xlsx')
