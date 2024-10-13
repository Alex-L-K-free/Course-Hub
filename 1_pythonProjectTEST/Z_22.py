# 1. Найти сумму цифр числа
# number = -2345
# sum_res = 0
# number = abs(number)
# while number != 0:
#     division_res = number % 10
#     print('Остаток: ', division_res)
#     sum_res += division_res
#     number = int(number / 10)
#     print('Число', number)
# print('Суммы цифр числа = ', sum_res)

# 2. Найти максимальное чётное чило из случайного набора чисел(Сгенерировать случайный набор чисел)
# import random
# numbers = []
# counter = 0
# while counter < 100:
#     numbers.append(random.randint(1, 10))
#     counter += 1
# print(numbers)
# max_number = -9999999999999
# for number in numbers:
#     if number > max_number:
#         max_number = number
#
# print(max_number)
# print(sorted(numbers)[-1])

#print(random.randint(1, 100))

# 3. Отсортировать список от меньшего к большему не используя функцию sort()
# ДЗ. Отсортировать список от большему к меньшему не используя функцию sort()
# import random
# numbers = []
# numbers_sorted = []
# counter = 0
# while counter < 10:
#     numbers.append(random.randint(1, 1000))
#     counter += 1
# print(numbers)
# while len(numbers) != 0:
#     min_number = 9999999999999
#     for number in numbers:
#         if number < min_number:
#             min_number = number
#     numbers.remove(number)
# print(min_number)
print("#"*50)
import random
numbers = []
numbers_sorted = []
counter = 0
while counter < 10:
    numbers.append(random.randint(1, 1000))
    counter += 1
print(numbers)
while len(numbers) != 0:
    min_number = 9999999999
    for number in numbers:
        if number < min_number:
            min_number = number
    numbers.remove(min_number)
    numbers_sorted.append(min_number)
print(numbers_sorted)