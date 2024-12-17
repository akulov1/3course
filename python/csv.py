import csv
from datetime import datetime

# Путь к файлу
filename = '1 - 1.csv'
target_letter = 'И'
target_date_str = '01 Май 2017 00:00'

# Словарь для замены месяцев
months = {
    "Янв": "Jan", "Фев": "Feb", "Мар": "Mar", "Апр": "Apr", "Май": "May", "Июн": "Jun",
    "Июл": "Jul", "Авг": "Aug", "Сен": "Sep", "Окт": "Oct", "Ноя": "Nov", "Дек": "Dec"
}

# Функция замены русских месяцев
def replace_month(date_str):
    for rus, eng in months.items():
        date_str = date_str.replace(rus, eng)
    return date_str

# Преобразуем дату
target_date = datetime.strptime(replace_month(target_date_str), '%d %b %Y %H:%M')

# Результаты
passed_people = []

# Чтение CSV
with open(filename, encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row['Фамилия'].startswith(target_letter):
            try:
                completed_date = datetime.strptime(replace_month(row['Завершено']), '%d %b %Y %H:%M')
                if completed_date < target_date and float(row['Оценка/100,00']) >= 60:
                    passed_people.append({
                        'Фамилия': row['Фамилия'],
                        'Имя': row['Имя'],
                        'Завершено': row['Завершено'],
                        'Оценка': row['Оценка/100,00']
                    })
            except ValueError:
                continue

# Вывод результатов
print(f"Количество людей: {len(passed_people)}")
for person in passed_people:
    print(f"{person['Фамилия']} {person['Имя']}, Завершено: {person['Завершено']}, Оценка: {person['Оценка']}")
