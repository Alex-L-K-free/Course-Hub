# Middle Занятие 5. Практика
# Практическое занятие
# 1. Выбираем лучшую архитектуру хранения данных для игры
# 2. Пишем функцию для вывода данных
# 3. Пишем функцию для ввода данных
data = {
    "1": {
        "a": "-",
        "b": "-",
        "c": "-"
    },
    "2": {
        "a": "-",
        "b": "-",
        "c": "-"
    },
    "3": {
        "a": "-",
        "b": "-",
        "c": "-"
    }
}


## функция ввода значений #
def input_value(input_value):
    colum = input_value[1]
    row = input_value[0]
    value = input_value[2]
    data[row][colum] = value
#   pass


## функция вывода графической части в двух вариантах#
def print_game_fild():
## вариант вывод циклом #
#    print("Данные вводятся в формате: 1а0 или 1ах")
#    print(f"\t\ta\t\tb\t\tc\n")
#    for key, value in data.items():
#       print (f"{key}\t\t{value["a"]}\t\t{value["b"]}\t\t{value["c"]}\n")
## вариант вывод строками #
    print("Данные вводятся в формате: 1а0 или 1ах")
    print(f"\t\ta\t\tb\t\tc\n")
    print(f"1\t\t{data["1"]["a"]}\t\t{data["1"]["b"]}\t\t{data["1"]["c"]}\n")
    print(f"2\t\t{data["2"]["a"]}\t\t{data["2"]["b"]}\t\t{data["2"]["c"]}\n")
    print(f"3\t\t{data["3"]["a"]}\t\t{data["3"]["b"]}\t\t{data["3"]["c"]}\n")


print()

## функция запуска игры и ввода данных #
def run_game():
    print("игра Крестики-Нолики началась")
    print_game_fild()
    input_value(input("Введите знак: "))
    print_game_fild()
    input_value(input("Введите знак: "))
    print_game_fild()
    input_value(input("Введите знак: "))
    print_game_fild()


run_game()