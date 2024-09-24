def sort_by_vowel_consonant_diff(strings):
    def vowel_consonant_diff(s):
        vowels = set("aeiouAEIOU")
        consonants = set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")
        vowel_count = sum(1 for char in s if char in vowels)
        consonant_count = sum(1 for char in s if char in consonants)
        if vowel_count + consonant_count == 0:
            return 0
        return consonant_count - vowel_count

    return sorted(strings, key=vowel_consonant_diff)


def sort_by_ascii(strings):
    first_string = strings[0] if strings else ""

    def ascii_deviation(s):
        ascii_mean = sum(ord(char) for char in s) / len(s)
        first_ascii_mean = sum(ord(char) for char in first_string) / len(first_string)
        return (ascii_mean - first_ascii_mean) ** 2

    return sorted(strings, key=ascii_deviation)



def sort3(strings):
    def f(s):
        vowels = set("aeiouAEIOU")
        consonants = set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")

        transitions_vc = sum(1 for i in range(len(s) - 1) if s[i] in vowels and s[i + 1] in consonants)
        transitions_cv = sum(1 for i in range(len(s) - 1) if s[i] in consonants and s[i + 1] in vowels)

        # print(s,transitions_vc, transitions_cv)
        return transitions_vc - transitions_cv

    return sorted(strings, key=f)


#среднее количество зеркальных троек символов
def sort_by_palindrom(strings):
    def palindrom(s):
        count = 0
        for i in range(len(s) - 2):
            if s[i] == s[i + 2]:
                count += 1
        return count

    return sorted(strings, key=palindrom)


# Пример строк
strings = [
    "hlhl world",
    "abaracadabr",
    "proozru",
]

# Сортировка строк по каждому условию
sorted1 = sort_by_vowel_consonant_diff(strings)
sorted2 = sort_by_ascii(strings)
sorted3 = sort3(strings)
sorted4 = sort_by_palindrom(strings)

# Вывод результата
print("Отсортированные строки в порядке увеличения разницы между кол-вом согласных и гласных в строке")
print(sorted1)

print("\nВ порядке увеличения квадратичного отклонения среднего веса ascii кода символа строки от среднего веса ascii кода символа первой строки:")
print(sorted2)

print("\nВ порядке увеличения разницы между количеством гласная-согласная и согласная-гласная в строке:")
print(sorted3)

print("\nВ порядке увеличения среднего количества зеркальных троек (например, 'ada') символов в строке:")
print(sorted4)
