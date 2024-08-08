# Este programa carga un archivo Excel con calificaciones de alumnos y grafica dichas calificaciones.
# Se asegura de que las etiquetas de los alumnos en el eje X no se encimen utilizando rotación de etiquetas.

import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos del archivo Excel
file_path = 'calificaciones_alumnos.xlsx'
df = pd.read_excel(file_path)

# Verificar la estructura del DataFrame
print(df.head())

# Crear una figura y ejes para el gráfico
fig, ax = plt.subplots()

# Graficar las calificaciones
for column in df.columns[1:]:  # Saltar la primera columna que es 'Nombre'
    ax.plot(df['Nombre'], df[column], marker='o', label=column)

# Configurar etiquetas y título del gráfico
ax.set_xlabel('Nombre del Alumno')
ax.set_ylabel('Calificación')
ax.set_title('Calificaciones de los Alumnos')
ax.legend()

# Rotar las etiquetas del eje X para evitar que se encimen
plt.xticks(rotation=45, ha='right')

# Ajustar el diseño para evitar recortes
plt.tight_layout()

# Mostrar el gráfico
plt.show()
