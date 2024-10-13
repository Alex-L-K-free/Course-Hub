# 1. Найти сумму цифр числа, кроме самой левой цифры(Самый старший разряд)
print("1. Найти сумму цифр числа, кроме самой левой цифры(Самый старший разряд) (используется пример из занятия №22)")
number = -2345
sum_res = 0
number = abs(number)
# строка для уменьшения числа
number = int(str(number)[1:])
while number != 0:
    division_res = number % 10
    print('Остаток: ', division_res)
    sum_res += division_res
    number = int(number / 10)
    print('Число', number)
print("ОТВЕТ:")
print('Сумма цифр числа = ', sum_res)
print("#"*150)

# 2. Найти минимальное нечётное число из случайного набора чисел(Сгенерировать случайный набор чисел)
print("2. Найти минимальное нечётное число из случайного набора чисел(Сгенерировать случайный набор чисел) (используется пример из занятия №22)")
import random
numbers = []
counter = 0
while counter < 10:
    numbers.append(random.randint(1, 100))
    counter += 1
min_number = float('inf')
for number in numbers:
    if number < min_number:
        min_number = number
min_even = float('inf')
for number in numbers:
    if number % 2 == 1 and number < min_even:
        min_even = number
print("Сгенерированный набор чисел:", numbers)
print("ОТВЕТ:")
if min_even != float('inf'):
    print("Минимальное нечетное число из набора:", min_even)
else:
    print("В наборе нет нечетных чисел.")
print("#"*150)

# 3. Отсортировать список от большему к меньшему не используя функцию sort()
print("3. Отсортировать список от большему к меньшему не используя функцию sort() (используется пример из занятия №22)")
import random
numbers = []
numbers_sorted = []
counter = 0
while counter < 10:
    numbers.append(random.randint(1, 100))
    counter += 1
print("Сгенерированный набор чисел:", numbers)
while len(numbers) != 0:
    max_number = -9999999999
    for number in numbers:
        if number > max_number:
            max_number = number
    numbers.remove(max_number)
    numbers_sorted.append(max_number)
print("ОТВЕТ:")
print("Отсортированный список от большего к меньшему:", numbers_sorted)
print("#"*150)