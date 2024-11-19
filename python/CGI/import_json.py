import sqlite3
import json


def import_from_json():
    db_path = 'cosmos.db'
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    with open('planets.json', 'r', encoding='utf-8') as file:
        planets_data = json.load(file)

    # Вставляем только новые данные (проверка на существующий id)
    for planet in planets_data:
        cursor.execute("SELECT COUNT(*) FROM Planets WHERE id = ?", (planet["ID"],))
        count = cursor.fetchone()[0]

        if count == 0:  # Только если такого ID нет
            cursor.execute("INSERT INTO Planets (id, name, type, distance_from_sun) VALUES (?, ?, ?, ?)",
                           (planet["ID"], planet["Name"], planet["Type"], planet["Distance"]))

    conn.commit()

    conn.close()
    print("Импорт завершен! Данные импортированы из planets.json в базу данных.")


import_from_json()
