import sqlite3
import json

def export_to_json():
    db_path = 'cosmos.db'
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Planets")
    planets_rows = cursor.fetchall()

    planets_data = []
    for row in planets_rows:
        planet = {
            "ID": row[0],
            "Name": row[1],
            "Type": row[2],
            "Distance": row[3]
        }
        planets_data.append(planet)

    with open('planets.json', 'w', encoding='utf-8') as file:
        json.dump(planets_data, file, ensure_ascii=False, indent=4)

    conn.close()
    print("Экспорт завершен! Данные сохранены в planets.json.")


export_to_json()
