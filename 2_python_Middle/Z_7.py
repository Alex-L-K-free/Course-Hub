# Занятие 7. Оператор IN
# Оператор IN вместо длинного цикла

numbers = [1, 5, 12, 14, 9, 99]
num = 19
print(num in numbers)

result = False
for number in numbers:
    if number == num:
        result = True
print(result)