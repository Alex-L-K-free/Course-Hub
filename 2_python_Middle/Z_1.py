# Занятие 1. Функции
# 1. Для чего нужны функции
# 2. Как написать свою функции
# def calculate_expression():
#     num1 = int(input("введите число 1: "))
#     znak = input("введите знак: ")
#     num2 = int(input("введите число 2: "))
#     if znak == "+":
#         print(f"{num1} {znak} {num2} = {num1 + num2}")
#     elif znak == "-":
#         print("Разность = ", num1 - num2)
#     elif znak == "*":
#         print("Произведение = ", num1 * num2)
#     elif znak == "/":
#         print("Деление = ", num1 / num2)
#     else:
#         print (f"знак {znak} не поддерживается")
# # calculate_expression()
# import time
# print ("1.урок литературы начался")
# time.sleep(3)
# print ("2.учитель спросил про домашку")
# time.sleep(3)
# print ("3.в классе тишина никто не сделал домашку")
# time.sleep(3)
# print ("5.Вовочка начал решать")
# time.sleep(3)
# calculate_expression()
# time.sleep(3)
# print ("5.Маша начал решать")
# time.sleep(3)
#
# calculate_expression()

import time

def calculate_expression():
    num1 = int(input('Введите число 1: '))
    znak = input('Введите знак: ')
    num2 = int(input('Введите число 2: '))
    if znak == '+':
        print(f'{num1} {znak} {num2} = {num1 + num2}')
    elif znak == '-':
        print(f'{num1} {znak} {num2} = {num1 - num2}')
    elif znak == '*':
        print(f'{num1} {znak} {num2} = {num1 * num2}')
    elif znak == '/':
        print(f'{num1} {znak} {num2} = {num1 / num2}')
    else:
        print(f'Знак {znak} не поддерживается текущей версией программы')

#calculate_expression()
print('1. Урок литературы начался')
time.sleep(1)
print('2. Учитель спросил про домашку')
time.sleep(1)
print('3. В классе тихина, никто не сделал домашку')
time.sleep(1)
print('4. Учитель разозлился и вызвал к доске Вовочку')
time.sleep(1)
print('5. Вовочка начал решать пример')
time.sleep(1)
calculate_expression()
time.sleep(1)
print('6. Вовочка получил 2 балла')
time.sleep(1)
print('7. Учитель вазвал Машу')
time.sleep(1)
print('8. Маша начала решать пример')
time.sleep(1)
calculate_expression()
print('9. Маша получила 5')
time.sleep(1)
print('10. Урок закончился')
time.sleep(1)
