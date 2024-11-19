import sqlite3

conn = sqlite3.connect('cosmos.db')
cursor = conn.cursor()

# Заполняем таблицу "Планеты"
cursor.executemany('''
INSERT INTO Planets (name, type, distance_from_sun) VALUES (?, ?, ?)
''', [
    ('Земля', 'Террестриальная', 149.6),
    ('Марс', 'Террестриальная', 227.9),
    ('Юпитер', 'Газовый гигант', 778.5)
])

# Заполняем таблицу "Спутники"
cursor.executemany('''
INSERT INTO Satellites (name, planet_id) VALUES (?, ?)
''', [
    ('Луна', 1),
    ('Фобос', 2),
    ('Ганимед', 3)
])

# Заполняем таблицу "Исследовательские миссии"
cursor.executemany('''
INSERT INTO Missions (name, planet_id, year) VALUES (?, ?, ?)
''', [
    ('Apollo 11', 2, '1969'),
    ('Viking 1', 4, '1975'),
    ('Galileo', 1, '1989')
])

conn.commit()
conn.close()
