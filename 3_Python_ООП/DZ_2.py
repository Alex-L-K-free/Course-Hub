class Int:
    @staticmethod
    def str_num(num):
        return int(num)

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        setattr(instance, self.name, self.str_num(value))


class Calculator:
    @staticmethod
    def input_otvet():
        num1 = input("Введите первое число: ")
        num1 = Int.str_num(num1)
        operation = input("введите знак операции (+, -, *, /): ")
        num2 = input("Введите второе число: ")
        num2 = Int.str_num(num2)
        otvet = "ОШИБКА"
        if operation == "+":
            otvet = num1 + num2
        elif operation == "-":
            otvet = num1 - num2
        elif operation == "/":
            otvet = num1 / num2
        elif operation == "*":
            otvet = num1 * num2
        return otvet


run = Calculator()
result = run.input_otvet()
print("Результат: ", result)