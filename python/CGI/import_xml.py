import sqlite3
from xml.dom.minidom import parse

def import_from_xml():
    db_path = 'cosmos.db'
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    doc = parse('planets.xml')

    planets = doc.getElementsByTagName('Planet')

    for planet in planets:
        name_element = planet.getElementsByTagName('Name')[0].firstChild.nodeValue
        type_element = planet.getElementsByTagName('Type')[0].firstChild.nodeValue
        distance_element = planet.getElementsByTagName('Distance')[0].firstChild.nodeValue

        cursor.execute("INSERT INTO Planets (name, type, distance_from_sun) VALUES (?, ?, ?)",
                       (name_element, type_element, distance_element))

    conn.commit()

    conn.close()
    print("Импорт завершен! Данные импортированы из planets.xml в базу данных.")


import_from_xml()