import csv
import os
import psycopg2


conn = psycopg2.connect(
    host=os.getenv('POSTGRES_HOST'),
    port=os.getenv('POSTGRES_PORT'),
    db_name_pstgres=os.getenv('POSTGRES_DB'),
    user=os.getenv('POSTGRES_USER'),
    password=os.getenv('POSTGRES_PASSWORD'),
)

cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    title TEXT,
    publisher TEXT
    )
""")

with open('books.csv', newline='', encoding='utf8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        cursor.execute("""
        INSERT INTO books (title, publisher) VALUES (%s, %s) 
        (row['title'], row['publisher']))
        """)

conn.commit()
cursor.close()
conn.close()
