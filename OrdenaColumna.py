# Este programa carga un archivo Excel con calificaciones de alumnos, agrega una columna llamada 'Mat_Fisica'
# con valores aleatorios entre 0 y 100 con un decimal, ordena la tabla por el campo 'Nombre',
# y guarda el archivo actualizado.

import pandas as pd
import numpy as np

# Cargar los datos del archivo Excel
file_path = 'calificaciones_alumnos.xlsx'
df = pd.read_excel(file_path)

# Verificar la estructura del DataFrame
print(df.head())

# Generar valores aleatorios entre 0 y 100 con un decimal para la nueva columna 'Mat_Fisica'
df['Mat_Fisica'] = np.round(np.random.uniform(0, 100, len(df)), 1)

# Verificar la estructura del DataFrame después de agregar la nueva columna
print(df.head())

# Ordenar la tabla por el campo 'Nombre'
df = df.sort_values(by='Nombre')

# Verificar la estructura del DataFrame después de ordenar
print(df.head())

# Guardar el DataFrame actualizado en un nuevo archivo Excel
df.to_excel('calificaciones_alumnos_actualizado.xlsx', index=False)

# Verificar que el archivo se haya guardado correctamente
print("Archivo actualizado guardado como 'calificaciones_alumnos_actualizado.xlsx'")
