import sqlite3
from xml.dom import minidom

def import_from_xml():
    db_path = 'cosmos.db'
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    doc = minidom.parse('planets.xml')
    planets = doc.getElementsByTagName('Planet')

    for planet in planets:
        planet_id = int(planet.getElementsByTagName('ID')[0].childNodes[0].data)
        name = planet.getElementsByTagName('Name')[0].childNodes[0].data
        planet_type = planet.getElementsByTagName('Type')[0].childNodes[0].data
        distance = float(planet.getElementsByTagName('Distance')[0].childNodes[0].data)

        # Проверка на существование записи
        cursor.execute("SELECT COUNT(*) FROM Planets WHERE id = ?", (planet_id,))
        count = cursor.fetchone()[0]

        if count == 0:  # Если записи нет, вставляем новую
            cursor.execute("INSERT INTO Planets (id, name, type, distance_from_sun) VALUES (?, ?, ?, ?)",
                           (planet_id, name, planet_type, distance))
        else:
            print(f"Пропущена запись с ID {planet_id}, так как она уже существует.")

    conn.commit()
    conn.close()
    print("Импорт из XML завершён!")


import_from_xml()
