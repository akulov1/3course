import osmium
import re

class BankHandler(osmium.SimpleHandler):
    def __init__(self):
        super().__init__()
        self.banks = []  # Список для хранения информации о банках

    def node(self, n):
        # Проверяем, если у объекта есть тег amenity=bank
        if 'amenity' in n.tags and n.tags['amenity'] == 'bank':
            bank_name = n.tags.get('name', 'Не указано')  # Получаем имя банка
            opening_hours = n.tags.get('opening_hours', '')  # Часы работы
            self.banks.append((bank_name, opening_hours))

# Указываем путь к вашему файлу .osm
osm_file = '1 - 2.osm'

# Создаем экземпляр обработчика и применяем его к файлу
handler = BankHandler()
handler.apply_file(osm_file)

# Шаг 1: Общее количество банков
total_banks = len(handler.banks)

# Шаг 2: Сортировка банков по алфавиту
sorted_banks = sorted(set(bank[0] for bank in handler.banks))  # Сортируем имена банков

# Шаг 3: Подсчет банков, работающих с 9:00
banks_opening_9am = [bank for bank in handler.banks if re.search(r'09:00', bank[1])]
num_banks_opening_9am = len(banks_opening_9am)

# Вывод результатов
print(f"Количество банков: {total_banks}\n")

print("Банки в алфавитном порядке:")
for name in sorted_banks:
    print(name)

print(f"\nКоличество банков, работающих с 9:00: {num_banks_opening_9am}")
