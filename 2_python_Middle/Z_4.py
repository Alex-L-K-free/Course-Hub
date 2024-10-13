# Занятие 4. Рекурсия и Стек
# 1. Как и где хранятся наши переменные
# 2. Что такое стек
# 3. Что такое рекурсия
# пример как делать не надо:
# def do_sum_x2(num1, num2, counter):
#     print(f"{counter}, {num1 * num2 * 2}")
#     counter += 1
#     do_sum_x2 (num1,num2,counter)
# do_sum_x2(10,5, 1)
# do_sum_x2(20,5, 1)

def number_plus1(number):
    result = number + 1
    print(result)
    return result

def number_plus2(number):
    plus_number = number + 2
    print(plus_number)
    result = number_plus1(plus_number)
    return result

def number_plus3(number):
    plus_number = number + 3
    print(plus_number)
    result = number_plus2(plus_number)
    return result

def number_x2(number):
    x2_number = number * 2
    print(x2_number)
    result = number_plus3(x2_number)
    return result

print(number_x2(2))
