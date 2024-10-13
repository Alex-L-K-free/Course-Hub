# 1. Необходимо вывести на экран числа от 5 до 1
# ДЗ. Вывести на экран произведение чисел от -10 до 7
counter = 5
while counter >= 1:
    print(counter)
    counter -= 1
from_5_to_1 = range(5, 0, -1)
print(list(from_5_to_1))

# 2. Программа находит сумму чисел от N до M, включая N и M, где N и M вводятся через input()
# number1 = int(input("Введите первое число: "))
# number2 = int(input("Введите второе число: "))
# sum_number = 0
# if number1 <= number2:
#     while number1 <= number2:
#         print(number1)
#         sum_number += number1
#         number1 += 1
# else:
#     while number2 <= number1:
#         print(number2)
#         sum_number += number2
#         number2 += 1
# print('Сумма', sum_number)

# 3. Найти сумму нечётных чисел от N до M, включая N и M, где N и M вводятся через input()
# ДЗ. Найти сумму чётных чисел от N до M, включая N и M, где N и M вводятся через input(). Учесть условие когда первое число больше второго
# number1 = int(input("Введите первое число: "))
# number2 = int(input("Введите второе число: "))
# sum_number = 0
# while number1 <= number2:
#     if (number1 % 2) == 0:
#         print(number1)
#         sum_number += number1
#     number1 += 1
# print('Сумма', sum_number)

# 4. Найти количество нечётных чисел в списке
# ДЗ. Найти количество кратных 10 (10, 20, 30 ...) чисел в списке
numbers = range(1, 10)
# counter = 0
# for number in numbers:
#     if (number % 2) == 1:
#         counter += 1
# print("количество нечетных =", counter)

# 5. Вывести первые 12 степеней числа 2
# Вывести первые 7 степеней числа 3
# for ctepen in range(1, 13):
#     print(f"2 в степени {ctepen} = {pow(2, ctepen)}")
