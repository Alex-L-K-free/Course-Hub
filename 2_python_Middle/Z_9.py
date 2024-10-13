# Middle Занятие 9. Практика
# Игра в телеграм боте

# 1. Адаптируем нашу игру на телеграм бота
# 2. Играем в игру

# Игра Крестики-нолики
STATUS_CONTINUE = 'игра прдолжается!'
EMPTY = '_'
ROW1 = '1'
ROW2 = '2'
ROW3 = '3'
COLA = 'a'
COLB = 'b'
COLC = 'c'
data = {
    ROW1: {
        COLA: EMPTY,
        COLB: EMPTY,
        COLC: EMPTY,
    },
    ROW2: {
        COLA: EMPTY,
        COLB: EMPTY,
        COLC: EMPTY,
    },
    ROW3: {
        COLA: EMPTY,
        COLB: EMPTY,
        COLC: EMPTY,
    }
}
allowed_symbols = ['X', 'O']
allowed_rows = [ROW1, ROW2, ROW3]
allowed_cols = [COLA, COLB, COLC]


def check_is_game_end():
    winner = STATUS_CONTINUE

    empty_symbols = 0
    for dat in data.values():
        for d in dat.values():
            if d == EMPTY:
                empty_symbols += 1

    # Условия победы по строкам
    if (data[ROW1][COLA] == data[ROW1][COLB]) and (data[ROW1][COLA] == data[ROW1][COLC]) and (data[ROW1][COLA] != EMPTY):
        winner = data[ROW1][COLA]
    elif (data[ROW2][COLA] == data[ROW2][COLB]) and (data[ROW2][COLA] == data[ROW2][COLC]) and (data[ROW2][COLA] != EMPTY):
        winner = data[ROW2][COLA]
    elif (data[ROW3][COLA] == data[ROW3][COLB]) and (data[ROW3][COLA] == data[ROW3][COLC]) and (data[ROW3][COLA] != EMPTY):
        winner = data[ROW3][COLA]
    # Условия победы по колонкам
    elif (data[ROW1][COLA] == data[ROW2][COLA]) and (data[ROW1][COLA] == data[ROW3][COLA]) and (data[ROW1][COLA] != EMPTY):
        winner = data[ROW1][COLA]
    elif (data[ROW1][COLB] == data[ROW2][COLB]) and (data[ROW1][COLB] == data[ROW3][COLB]) and (data[ROW1][COLB] != EMPTY):
        winner = data[ROW1][COLB]
    elif (data[ROW1][COLC] == data[ROW2][COLC]) and (data[ROW1][COLC] == data[ROW3][COLC]) and (data[ROW1][COLC] != EMPTY):
        winner = data[ROW1][COLC]
    # Условия победы по диагоналям
    elif (data[ROW1][COLA] == data[ROW2][COLB]) and (data[ROW1][COLA] == data[ROW3][COLC]) and (data[ROW1][COLA] != EMPTY):
        winner = data[ROW1][COLA]
    elif (data[ROW1][COLC] == data[ROW2][COLB]) and (data[ROW1][COLC] == data[ROW3][COLA]) and (data[ROW1][COLC] != EMPTY):
        winner = data[ROW1][COLC]
    # Все ячейки заполнены, но победа не обнаружена
    elif empty_symbols == 0:
        winner = 'Ничья'

    return winner


def input_value(input_value, value):
    column = input_value[1].lower()
    if column not in allowed_cols:
        return f'[?] Вы ввели неверную колонку: {column}, разрешённые колонки: {allowed_cols}. Вы потеряли ход'

    row = input_value[0]
    if row not in allowed_rows:
        return f'[?] Вы ввели неверную строку: {row}, разрешённые колонки: {allowed_rows}. Вы потеряли ход'

    if (value in allowed_symbols) and (data[row][column] == EMPTY):
        data[row][column] = value
        return 'Ход принят'
    else:
        return f'[?] Вы потеряли ход, так как ввели запрещённый символ: {value}, разрешённые символы: {allowed_symbols}. Или ячейка уже заполнена'


def print_game_field():
    str_result = 'Данные вводятся в формате: 1a\n'
    str_result += f" \t\ta\t\tb\t\tc\n"
    str_result += f"1\t\t{data[ROW1][COLA]}\t\t{data[ROW1][COLB]}\t\t{data[ROW1][COLC]}\n"
    str_result += f"2\t\t{data[ROW2][COLA]}\t\t{data[ROW2][COLB]}\t\t{data[ROW2][COLC]}\n"
    str_result += f"3\t\t{data[ROW3][COLA]}\t\t{data[ROW3][COLB]}\t\t{data[ROW3][COLC]}\n"
    return str_result


def clear_data():
    data[ROW1] = {
        COLA: EMPTY,
        COLB: EMPTY,
        COLC: EMPTY
    }
    data[ROW2] = {
        COLA: EMPTY,
        COLB: EMPTY,
        COLC: EMPTY
    }
    data[ROW3] = {
        COLA: EMPTY,
        COLB: EMPTY,
        COLC: EMPTY
    }


# Создание бота для игры
# pip install pyTelegramBotAPI
# https://t.me/BotFather

import telebot
import Z_9_game_logic

bot = telebot.TeleBot("6983632931:AAE-O9DFRE_1Ais7L-JzsqmrbUMrTUb2z8A")
CURRENT_PLAYER = ['X']


@bot.message_handler(commands=['start'])
def start_game(message):
	Z_9_game_logic.clear_data()
	bot.send_message(message.chat.id, f'Новая игра началась')
	bot.send_message(message.chat.id, Z_9_game_logic.print_game_field())
	bot.send_message(message.chat.id, f'Вах ход: {CURRENT_PLAYER[0]}')


@bot.message_handler(content_types=['text'])
def start_game(message):
	bot.send_message(
		message.chat.id,
		Z_9_game_logic.input_value(message.text, CURRENT_PLAYER[0])
	)
	if Z_9_game_logic.check_is_game_end() == Z_9_game_logic.STATUS_CONTINUE:
		bot.send_message(
			message.chat.id,
			Z_9_game_logic.print_game_field()
		)
		if CURRENT_PLAYER[0] == 'X':
			CURRENT_PLAYER[0] = 'O'
		else:
			CURRENT_PLAYER[0] = 'X'
		bot.send_message(
			message.chat.id,
			f'Сейчас ходит: {CURRENT_PLAYER[0]}'
		)
	else:
		bot.send_message(message.chat.id, f'Игра закончена, победа: {Z_9_game_logic.check_is_game_end()}')


bot.infinity_polling()
