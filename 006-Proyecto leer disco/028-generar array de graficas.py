import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

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
        WHEN LOWER(archivo) LIKE '%.pdf' OR LOWER(archivo) LIKE '%.doc' OR LOWER(archivo) LIKE '%.docx' THEN 1
        ELSE 0
    END) AS documentos,
    SUM(CASE
        WHEN LOWER(archivo) LIKE '%.jpg' OR LOWER(archivo) LIKE '%.png'
          OR LOWER(archivo) LIKE '%.mp4' OR LOWER(archivo) LIKE '%.avi'
          OR LOWER(archivo) LIKE '%.pdf' OR LOWER(archivo) LIKE '%.doc'
          OR LOWER(archivo) LIKE '%.docx' THEN 0
        ELSE 1
    END) AS otros
FROM archivos
GROUP BY disco;
'''

df = pd.read_sql_query(query, conn)

def create_pie_chart(ax, data, title):
    labels = ['Imagenes', 'Videos', 'Documentos', 'Otros']
    sizes = data
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    ax.set_title(title)

fig, axs = plt.subplots(1, len(df), figsize=(15, 5))

for i, row in df.iterrows():
    create_pie_chart(axs[i], [row['imagenes'], row['videos'], row['documentos'], row['otros']], f"Disco {row['disco']}")

plt.tight_layout()
plt.show()
