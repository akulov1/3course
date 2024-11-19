#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cgi
import sqlite3
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print("Content-Type: text/html; charset=UTF-8")
print()

html_template = """
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>База данных: Космос</title>
</head>
<body>
    <h1>Добавление новой планеты</h1>
    <form method="post" action="/cgi-bin/cgi_server.py">
        <label for="name">Название планеты:</label>
        <input type="text" id="name" name="name" required><br><br>

        <label for="type">Тип планеты:</label>
        <input type="text" id="type" name="type" required><br><br>

        <label for="distance">Расстояние от Солнца (в млн км):</label>
        <input type="number" id="distance" name="distance" step="0.1" required><br><br>

        <input type="submit" value="Добавить">
    </form>
    <h2>Список всех планет</h2>
    <table border="1">
        <tr>
            <th>ID</th>
            <th>Название</th>
            <th>Тип</th>
            <th>Расстояние от Солнца (млн км)</th>
        </tr>
        {planets_rows}
    </table>

    <h2>Добавить спутник</h2>
    <form method="post" action="/cgi-bin/cgi_server.py">
        <label for="satellite_name">Название спутника:</label>
        <input type="text" id="satellite_name" name="satellite_name" required><br><br>

        <label for="planet_id">ID планеты:</label>
        <input type="number" id="planet_id" name="planet_id" required><br><br>

        <input type="submit" value="Добавить спутник">
    </form>
    <h2>Список спутников</h2>
    <table border="1">
        <tr>
            <th>ID</th>
            <th>Название спутника</th>
            <th>Планета</th>
        </tr>
        {satellites_rows}
    </table>

    <h2>Добавить миссию</h2>
    <form method="post" action="/cgi-bin/cgi_server.py">
        <label for="mission_name">Название миссии:</label>
        <input type="text" id="mission_name" name="mission_name" required><br><br>

        <label for="mission_planet_id">ID планеты:</label>
        <input type="number" id="mission_planet_id" name="mission_planet_id" required><br><br>

        <label for="year">Год миссии:</label>
        <input type="number" id="year" name="year" required><br><br>

        <input type="submit" value="Добавить миссию">
    </form>
    <h2>Список миссий</h2>
    <table border="1">
        <tr>
            <th>ID</th>
            <th>Название миссии</th>
            <th>Год</th>
            <th>Планета</th>
        </tr>
        {missions_rows}
    </table>
</body>
</html>
"""

# Подключение к базе данных
db_path = 'cosmos.db'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Получение данных из формы
form = cgi.FieldStorage()

# Добавление новой планеты
name = form.getvalue("name")
type_ = form.getvalue("type")
distance = form.getvalue("distance")

if name and type_ and distance:
    cursor.execute("INSERT INTO Planets (name, type, distance_from_sun) VALUES (?, ?, ?)",
                   (name, type_, float(distance)))
    conn.commit()

# Добавление спутника
satellite_name = form.getvalue("satellite_name")
planet_id = form.getvalue("planet_id")

if satellite_name and planet_id:
    cursor.execute("INSERT INTO Satellites (name, planet_id) VALUES (?, ?)",
                   (satellite_name, int(planet_id)))
    conn.commit()

# Добавление миссии
mission_name = form.getvalue("mission_name")
mission_planet_id = form.getvalue("mission_planet_id")
year = form.getvalue("year")

if mission_name and mission_planet_id and year:
    cursor.execute("INSERT INTO Missions (name, planet_id, year) VALUES (?, ?, ?)",
                   (mission_name, int(mission_planet_id), int(year)))
    conn.commit()

# Получение всех данных из таблицы Planets
cursor.execute("SELECT * FROM Planets")
planets_rows = cursor.fetchall()

# Получение всех данных из таблицы Satellites
cursor.execute("SELECT Satellites.id, Satellites.name, Planets.name FROM Satellites INNER JOIN Planets ON Satellites.planet_id = Planets.id")
satellites_rows = cursor.fetchall()

# Получение всех данных из таблицы Missions
cursor.execute("SELECT Missions.id, Missions.name, Missions.year, Planets.name FROM Missions INNER JOIN Planets ON Missions.planet_id = Planets.id")
missions_rows = cursor.fetchall()

planets_html = ""
for row in planets_rows:
    planets_html += f"""
    <tr>
        <td>{row[0]}</td>
        <td>{row[1]}</td>
        <td>{row[2]}</td>
        <td>{row[3]}</td>
    </tr>
    """

satellites_html = ""
for row in satellites_rows:
    satellites_html += f"""
    <tr>
        <td>{row[0]}</td>
        <td>{row[1]}</td>
        <td>{row[2]}</td>
    </tr>
    """

missions_html = ""
for row in missions_rows:
    missions_html += f"""
    <tr>
        <td>{row[0]}</td>
        <td>{row[1]}</td>
        <td>{row[2]}</td>
        <td>{row[3]}</td>
    </tr>
    """

# Закрытие соединения с базой данных
conn.close()

# Вывод HTML-страницы
print(html_template.format(planets_rows=planets_html, satellites_rows=satellites_html, missions_rows=missions_html))
#python -m http.server --cgi 8000
