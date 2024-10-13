# Задание
# Реализовать свой осмысленный декоратор. Пример, использованные в прошлых уроках использовать нельзя

# пример использования декоратора для проверки ввода оператора и деления на ноль в калькуляторе

# декоратор проверки операторов и деления на 0
def decorate(oper_zero):
    def inner(num1, operation, num2):
        if num2 == 0 and operation == "/":
            print(f"ОШИБКА на {num2} делить нельзя")
            return
        elif operation != "/" and operation != "-" and operation != "+" and operation != "*":
            print("ОШИБКА неверный оператор")
            return
        return oper_zero(num1, operation, num2)
    return inner


# функция ввода числа
def input_out(numbers):
    number = int(input(numbers))
    return number

# функция ввода оператора
def operat_out():
    operator = input("введите знак операции (+, -, *, /): ")
    return operator

# функция расчета
@decorate
def calc(num1, operation, num2):
    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '/':
        result = num1 / num2
    elif operation == '*':
        result = num1 * num2
    return result

# функция  запуска
def run():
    num1 = input_out("Введите первое число: ")
    operation = operat_out()
    num2 = input_out("Введите второе число: ")
    result = calc(num1, operation, num2)
    print("Результат: ", result)

run()

# DZ_2
# class calculator():
#     def input_otvet(self):
#         num1 = input("Введите первое число: ")
#         operation = input("введите знак операции (+, -, *, /): ")
#         num2 = input("Введите второе число: ")
#         otvet = "ОШИБКА"
#         if operation == '+':
#             otvet = num1 + num2
#         elif operation == '-':
#             otvet = num1 - num2
#         elif operation == '/':
#             otvet = num1 / num2
#         elif operation == '*':
#             otvet = num1 * num2
#         return otvet
#
# run = calculator()
# result = run.input_otvet()
# print("Результат: ", result)