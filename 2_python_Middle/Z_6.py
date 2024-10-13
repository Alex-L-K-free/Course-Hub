# Middle Занятие 6. Больше практики
# Практическое занятие
# 1. Делаем очерёдность ходов
# 2. Делаем логику завершения игры
# 3. Добавляем автоматический ввод Крестика, или нолика
status_continium = "игра продолжается"
empty = "-"
row1 = "1"
row2 = "2"
row3 = "3"
cola = "a"
colb = "b"
colc = "c"
data = {
    row1: {
        cola: empty,
        colb: empty,
        colc: empty
    },
    row2: {
        cola: empty,
        colb: empty,
        colc: empty
    },
    row3: {
        cola: empty,
        colb: empty,
        colc: empty
    }
}

allowed_symbol = ["x", "o"]
allowed_rows = [row1, row2, row3]
allowed_cols = [cola, colb, colc]

def check_is_game_end():
    winner = status_continium
    empty_symbol = 0
    for dat in data.values():
        for d in dat.values():
            if d == empty:
                empty_symbol += 1
    # условия победы по строкам
    if (data[row1][cola] == data[row1][colb]) and (data[row1][cola] == data[row1][colc]) and (data[row1][cola] != empty):
        winner = data[row1][cola]
    elif (data[row2][cola] == data[row2][colb]) and (data[row2][cola] == data[row2][colc]) and (data[row2][cola] != empty):
        winner = data[row2][cola]
    elif (data[row3][cola] == data[row3][colb]) and (data[row3][cola] == data[row3][colc]) and (data[row3][cola] != empty):
        winner = data[row3][cola]
    # условия победы по колонкам
    elif (data[row1][cola] == data[row2][cola]) and (data[row1][cola] == data[row3][cola]) and (data[row1][cola] != empty):
        winner = data[row1][cola]
    elif (data[row1][colb] == data[row2][colb]) and (data[row1][colb] == data[row3][colb]) and (data[row1][colb] != empty):
        winner = data[row1][colb]
    elif (data[row1][colc] == data[row2][colc]) and (data[row1][colc] == data[row3][colc]) and (data[row1][colc] != empty):
        winner = data[row1][colc]
    # условия победы по диагонали
    elif (data[row1][cola] == data[row2][colb]) and (data[row1][cola] == data[row3][colc]) and (data[row1][cola] != empty):
        winner = data[row1][cola]
    elif (data[row1][colc] == data[row2][colb]) and (data[row1][colc] == data[row3][cola]) and (data[row1][colc] != empty):
        winner = data[row1][colc]
    # условия ничьей
    elif empty_symbol == 0:
        winner = "ничья"

    return winner

## функция ввода значений #
def input_value(input_value, value):
    colum = input_value[1].lower()
    if colum not in allowed_cols:
        print(f"[?] вы ввели неверную колонку: {colum}, разрешенные колонки: {allowed_cols}")
        return
    row = input_value[0]
    if row not in allowed_rows:
        print(f"[?] вы ввели неверную строку: {row}, разрешенные строки : {allowed_rows}")
        return
#    value = input_value[2]
    if (value in allowed_symbol) and (data[row][colum] == empty):
        data[row][colum] = value.upper()
    else:
        print(f"[?] вы потеряли ход, так как ввели запрещенный символ: {value}, разрешенные символы: {allowed_symbol}, или ячейка уже заполнена")
        return
#   pass

## функция вывода графической части в двух вариантах#
def print_game_fild():
    print("Данные вводятся в формате: 1а ")
    print(f"\t\ta\t\tb\t\tc\n")
    print(f"1\t\t{data[row1][cola]}\t\t{data[row1][colb]}\t\t{data[row1][colc]}\n")
    print(f"2\t\t{data[row2][cola]}\t\t{data[row2][colb]}\t\t{data[row2][colc]}\n")
    print(f"3\t\t{data[row3][cola]}\t\t{data[row3][colb]}\t\t{data[row3][colc]}\n")

print()

## функция запуска игры и ввода данных #
def run_game():
    print("игра Крестики-Нолики началась")
    print_game_fild()
    current_player = "x"
    while check_is_game_end() == status_continium:
        input_value(input(f"Ваш ход ( {current_player} ): "), current_player)
        print_game_fild()
        if current_player == "x":
            current_player = "o"
        else:
            current_player = "x"
    print(f"игра Крестики-Нолики закончилась, победил: {check_is_game_end()}")

run_game()
