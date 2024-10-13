# Занятие 8. Быстрый способ начать зарабатывать Telegram боты. Основы
# 1. Что такое телеграм боты и зачем это нам
# 2. Как и где взять токен
# 3. Установка библиотек
# 4. Запуск первого бота
# https://t.me/vbmkibmgugnfhutmgoihng_bot
# pip install pyTelegramBotAPI
# https://t.me/BotFather

import telebot

bot = telebot.TeleBot("6983632931:AAE-O9DFRE_1Ais7L-JzsqmrbUMrTUb2z8A")


@bot.message_handler(content_types=['text'])
def answer(message):
#	print(message.text)
	bot.send_message(message.chat.id, f'Ты написал мне: {message.text}')

# командна вечной работы бота
bot.infinity_polling()