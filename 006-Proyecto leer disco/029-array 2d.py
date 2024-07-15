import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
import math

conn = sqlite3.connect('discos.db')
cursor = conn.cursor()

query = '''
SELECT
    disco,
    SUM(CASE
        WHEN LOWER(archivo) LIKE '%.jpg' OR LOWER(archivo) LIKE '%.png' THEN 1
        ELSE 0
    END) AS imagenes,
    SUM(CASE
        WHEN LOWER(archivo) LIKE '%.mp4' OR LOWER(archivo) LIKE '%.avi' THEN 1
        ELSE 0
    END) AS videos,
    SUM(CASE
        WHEN LOWER(archivo) LIKE '%.pdf' OR LOWER(archivo) LIKE '%.doc' OR LOWER(archivo) LIKE '%.docx'  OR LOWER(archivo) LIKE '%.odt' THEN 1
        ELSE 0
    END) AS documentos,
    SUM(CASE
        WHEN  LOWER(archivo) LIKE '%.blend' THEN 1
        ELSE 0
    END) AS blender,
    SUM(CASE
        WHEN LOWER(archivo) LIKE '%.max'  THEN 1
        ELSE 0
    END) AS max,
    SUM(CASE
        WHEN LOWER(archivo) LIKE '%.3dm'  THEN 1
        ELSE 0
    END) AS Rhino,
    SUM(CASE
        WHEN LOWER(archivo) LIKE '%.jpg' OR LOWER(archivo) LIKE '%.png'
          OR LOWER(archivo) LIKE '%.mp4' OR LOWER(archivo) LIKE '%.avi'
          OR LOWER(archivo) LIKE '%.pdf' OR LOWER(archivo) LIKE '%.doc'
          OR LOWER(archivo) LIKE '%.docx'
            OR LOWER(archivo) LIKE '%.odt'
            OR LOWER(archivo) LIKE '%.blend'
            OR LOWER(archivo) LIKE '%.max'
            OR LOWER(archivo) LIKE '%.3dm'
          THEN 0
        ELSE 1
    END) AS otros
FROM archivos
GROUP BY disco;
'''

df = pd.read_sql_query(query, conn)

def create_pie_chart(ax, data, title):
    labels = ['Imagenes', 'Videos', 'Documentos', 'Otros','Max','Blender','Rhino']
    sizes = data
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    ax.set_title(title)

# Calculate the number of rows and columns needed for a 16:9 ratio
total_charts = len(df)
aspect_ratio = 16 / 9
cols = math.ceil(math.sqrt(total_charts * aspect_ratio))
rows = math.ceil(total_charts / cols)

fig, axs = plt.subplots(rows, cols, figsize=(16, 9))

# Flatten axs array if it is 2D
if rows > 1 and cols > 1:
    axs = axs.flatten()

for i, row in df.iterrows():
    create_pie_chart(axs[i], [row['imagenes'], row['videos'], row['documentos'], row['otros'], row['max'], row['blender'], row['Rhino']], f"Disco {row['disco']}")

# Hide any unused subplots
for j in range(i + 1, len(axs)):
    fig.delaxes(axs[j])

plt.tight_layout()
plt.show()
