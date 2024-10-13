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