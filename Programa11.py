# Programa 11: Este programa crea un boxplot de las calificaciones de todas las materias
# utilizando los campos "Mat_CalculoIntegral", "Mat_ProgramacionOOP", "Mat_EstructuraDatos" y "Mat_Fisica".

import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos del archivo Excel
file_path = 'calificaciones_alumnos_actualizado.xlsx'
df = pd.read_excel(file_path)

# Crear un boxplot de las calificaciones de todas las materias
df[['Mat_CalculoIntegral', 'Mat_ProgramacionOOP', 'Mat_EstructuraDatos', 'Mat_Fisica']].boxplot()
plt.title('Boxplot de Calificaciones de Todas las Materias')
plt.xlabel('Materia')
plt.ylabel('Calificación')
plt.grid(True)

# Mostrar el boxplot
plt.show()
