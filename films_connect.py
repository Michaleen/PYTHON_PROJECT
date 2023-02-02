import sqlite3 as sql
conn = sql.connect("films_project.db")
cursor = conn.cursor()