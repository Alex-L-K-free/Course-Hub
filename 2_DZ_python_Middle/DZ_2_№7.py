# задачи решены верно, в первой функции, также можно использовать оператор return

print("*" * 150)
print("Задание 1. Написать функцию которая принимает 2 параметра: число часов и число минут и выводит число секунд на экран")
def get_seconds (hours, minutes):
    seconds = hours * 3600 + minutes * 60
    print(f"Число секунд из {hours} часа(ов) и {minutes} минут(ы) равно", seconds)
    return seconds

hours = int(input("Введите число часов (от 1 до 24): "))
minutes = int(input("Введите число минут (от 1 до 60): "))

get_seconds(hours, minutes)
print("*" * 150)
###################################################################################################################
print("Задание 2. Написать функцию которая принимает 2 параметра и возвращает список чисел от первого до второго")
def get_range(from_number, to_number):
    numbers = []
    if to_number >= from_number:
        for number in range(from_number, to_number + 1):
            numbers.append(number)
    else:
        print("Второе число меньше первого. СТОП")
    print(f"Список чисел от {from_number} до {to_number}: ", numbers)
    return numbers

from_number = int(input("Введите первое число: "))
to_number = int(input("Введите второе число: "))

get_range(from_number, to_number)
print("*" * 150)
#############################################################################################################################################
print("Задание 3. Написать функцию которая принимает список чисел и возвращает наибольшее из чисел, встроенные функции использовать нельзя")
import random
numbers = []
def get_max(numbers):
    max_number = -9999999999999999999
    counter = 0
    while counter < 10:
        numbers.append(random.randint(1,100))
        counter += 1
    for number in numbers:
        if number > max_number:
            max_number = number
    print(f"Наибольшее число из списка чисел {numbers} равно ", max_number)
    return max_number

get_max(numbers)
########################################################################################################################