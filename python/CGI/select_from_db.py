import sqlite3

conn = sqlite3.connect('cosmos.db')
cursor = conn.cursor()

# 1. Количество спутников у каждой планеты
cursor.execute('''
SELECT Planets.name, COUNT(Satellites.id) AS satellite_count
FROM Planets
LEFT JOIN Satellites ON Planets.id = Satellites.planet_id
GROUP BY Planets.name
''')
print(cursor.fetchall())

# 2. Среднее расстояние планет от Солнца
cursor.execute('''
SELECT AVG(distance_from_sun) AS avg_distance
FROM Planets
''')
print(cursor.fetchall())

# 3. Количество миссий
cursor.execute('''
SELECT COUNT(*)
FROM Missions
''')
print(cursor.fetchall())

conn.close()
