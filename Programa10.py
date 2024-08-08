# Programa 10: Este programa crea un histograma de las calificaciones de "Mat_Fisica"
# utilizando los campos "Mat_CalculoIntegral", "Mat_ProgramacionOOP", "Mat_EstructuraDatos" y "Mat_Fisica".

import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos del archivo Excel
file_path = 'calificaciones_alumnos_actualizado.xlsx'
df = pd.read_excel(file_path)

# Crear un histograma de las calificaciones de "Mat_Fisica"
plt.hist(df['Mat_Fisica'], bins=10, edgecolor='black')
plt.title('Histograma de Calificaciones de Mat_Fisica')
plt.xlabel('Calificación')
plt.ylabel('Frecuencia')
plt.grid(True)

# Mostrar el histograma
plt.show()
