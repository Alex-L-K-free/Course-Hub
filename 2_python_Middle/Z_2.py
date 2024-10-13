# 1. Создаём функцию с параметрами
# 2. Оптимизируем нашу программу

#МОЕ
# import time
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
# # do_lesson_stage("1111", 3)
# # do_lesson_stage("2222", 3)
# # do_lesson_stage("3333", 3)
#
# def do_lesson_stage(text_to_print, time_to_sleep=3):
#     print(text_to_print)
#     time.sleep(time_to_sleep)
#
# do_lesson_stage("1.урок литературы начался")
# do_lesson_stage("2.учитель спросил про домашку")
# do_lesson_stage("3.в классе тишина никто не сделал домашку")
# do_lesson_stage("5.Вовочка начал решать")
# calculate_expression()
# do_lesson_stage("6.Маша начал решать")
# calculate_expression()

# ИЗ УРОКА
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


def do_lesson_stage(text_to_print, time_to_sleep=1):
    print(text_to_print)
    time.sleep(time_to_sleep)


do_lesson_stage('1. Урок литературы начался')
do_lesson_stage('2. Учитель спросил про домашку')
do_lesson_stage('3. В классе тихина, никто не сделал домашку')
do_lesson_stage('4. Учитель разозлился и вызвал к доске Вовочку')
do_lesson_stage('5. Вовочка начал решать пример', 3)
calculate_expression()
time.sleep(1)
do_lesson_stage('7. Учитель вазвал Машу')
do_lesson_stage('8. Маша начала решать пример', 2)
calculate_expression()
time.sleep(1)
do_lesson_stage('9. Маша получила 5')
do_lesson_stage('10. Урок закончился')
