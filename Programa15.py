# Programa 15: Este programa crea un gráfico de barras apiladas mostrando la distribución de aprobados y reprobados por materia
# utilizando los campos "Mat_CalculoIntegral", "Mat_ProgramacionOOP", "Mat_EstructuraDatos" y "Mat_Fisica".

import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos del archivo Excel
file_path = 'calificaciones_alumnos_actualizado.xlsx'
df = pd.read_excel(file_path)

# Contar el número de aprobados y reprobados por materia
aprobados = (df[['Mat_CalculoIntegral', 'Mat_ProgramacionOOP', 'Mat_EstructuraDatos', 'Mat_Fisica']] >= 70).sum()
reprobados = (df[['Mat_CalculoIntegral', 'Mat_ProgramacionOOP', 'Mat_EstructuraDatos', 'Mat_Fisica']] < 70).sum()

# Crear un gráfico de barras apiladas
fig, ax = plt.subplots()
bar_width = 0.5
index = range(len(aprobados))

bar1 = ax.bar(index, aprobados, bar_width, label='Aprobados')
bar2 = ax.bar(index, reprobados, bar_width, bottom=aprobados, label='Reprobados')

ax.set_xlabel('Materia')
ax.set_ylabel('Número de Alumnos')
ax.set_title('Distribución de Aprobados y Reprobados por Materia')
ax.set_xticks(index)
ax.set_xticklabels(['Calculo Integral', 'Programación OOP', 'Estructura de Datos', 'Física'])
ax.legend()

# Mostrar el gráfico
plt.show()
