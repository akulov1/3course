import math

import numpy

print('Variant 1:\n')


def first_task(
        string):  # в порядке увеличения разницы количества согласных и гласных (сначала гласные, потом согласные?) (согласные-гласные)
    s = ['a', 'e', 'y', 'u', 'o', 'i']
    res = ''
    for word in string.split():
        gl = ''
        sogl = ''
        for letter in word:
            if letter in s:
                sogl += letter
            else:
                gl += letter
        word = gl + sogl
        res += word
        res += ' '

    return res


print('first task: \n' + first_task('world strong yolo') + '\n')


def mse(string):
    suml = 0
    for letter in string:
        suml += ord(letter)
    mean = suml / len(string)
    sum_avg = 0
    for letter in string:
        sum_avg += (ord(letter) - mean) ** 2

    mse = math.sqrt(sum_avg / (len(string) - 1))

    return mse


def second_task(string1, string2):
    suml = 0
    for letter in string1:
        suml += ord(letter)
    avg_weight = suml / len(string1)

    print(avg_weight)


second_task('asd', 'omn')
