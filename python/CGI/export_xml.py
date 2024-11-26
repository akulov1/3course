import sqlite3
from xml.dom.minidom import Document


def export_to_xml():
    db_path = 'cosmos.db'
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Planets")
    planets_rows = cursor.fetchall()

    doc = Document()

    root = doc.createElement('Planets')
    doc.appendChild(root)

    for row in planets_rows:
        planet = doc.createElement('Planet')
        root.appendChild(planet)

        id_element = doc.createElement('ID')
        id_element.appendChild(doc.createTextNode(str(row[0])))
        planet.appendChild(id_element)

        name_element = doc.createElement('Name')
        name_element.appendChild(doc.createTextNode(row[1]))
        planet.appendChild(name_element)

        type_element = doc.createElement('Type')
        type_element.appendChild(doc.createTextNode(row[2]))
        planet.appendChild(type_element)

        distance_element = doc.createElement('Distance')
        distance_element.appendChild(doc.createTextNode(str(row[3])))
        planet.appendChild(distance_element)

    with open('planets.xml', 'w', encoding='utf-8') as file:
        file.write(doc.toprettyxml(indent="  "))

    conn.close()
    print("Экспорт завершен! Данные сохранены в planets.xml.")


export_to_xml()
