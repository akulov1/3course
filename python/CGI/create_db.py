import sqlite3

conn = sqlite3.connect('cosmos.db')
cursor = conn.cursor()

# Таблица "Планеты"
cursor.execute('''
CREATE TABLE IF NOT EXISTS Planets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    type TEXT NOT NULL,
    distance_from_sun REAL NOT NULL
)
''')

# Создание таблицы для спутников
cursor.execute("""
CREATE TABLE IF NOT EXISTS Satellites (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    planet_id INTEGER,
    FOREIGN KEY (planet_id) REFERENCES Planets(id)
)
""")

# Создание таблицы для миссий
cursor.execute("""
CREATE TABLE IF NOT EXISTS Missions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    planet_id INTEGER,
    year INTEGER,
    FOREIGN KEY (planet_id) REFERENCES Planets(id)
)
""")

conn.commit()
conn.close()
