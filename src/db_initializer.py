import pandas as pd
import sqlite3

df = pd.read.csv('data/crime_data.csv')
conn = sqlite3.connect('data/crime.db')
cursor = conn.cursor()

create_table_sql = """
CREATE TABLE IF NOT EXISTS crime_stats (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    major_category TEXT NOT NULL,
    minor_category TEXT NOT NULL,
    location TEXT NOT NULL,
    case_count INTEGER NOT NULL
    );
"""

cursor.execute(create_table_sql)

for _, row in df.iterrows():
    major = row['범죄대분류']
    minor = row['범죄중분류']

    for location in df.columns[2:]:
        count = int(row[location])
        cursor.execute(
            "INSERT INTO crime_stats (major_category, minor_category, location, case_count) VALUES (?, ?, ?, ?)",
            (major, minor, location, count)
        )

conn.commit()
conn.close()