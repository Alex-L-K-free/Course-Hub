# Разбор строки/списка через [:]
# Форматированные строки
# Полезные функции для строк: len, split, upper, lower, join, replace
# 1.Форматированные строки########################################################
# str1 = "привет"
# str2 = "Андрей"
# print(str1)
# str_res = f"{str1} {str2}"
# print(str_res)
# print (f"{str1} {str2}")
# print("Приветик %s" % str2)
# print("Приветик %s %s" % (str2, str1))
#
# str1 = 'Привет'
# str2 = 'Андрей'
# print(str1 + ' ' + str2)
# print('Приветик %s' % str2)
# print(f"{str1} {str2}")
# ##############################################
# 2.Разбор строки/списка через [:]########################################################
# text = "Мама мыла раму, раму мыла мама!!!"
# print(text)
# # 3. Идём слева направо
# print(text[:])
# # 1. До двоеточия с чего начинаем
# print(text[10:])
# # 2. После двоеточия до чего идём
# print(text[:10])
# for symbol in text:
#     print(F"{symbol} --------{type(symbol)}")
# print(text[2:10])
# print(text[:-10])
# print(text[-10:])

# 3. Полезные функции для строк: len, split, upper, lower, join, replace
text = "Мама мыла РАМУ, Раму мыла мама!!!"
# print(text)
# print(len(text))
# print(text.lower())
# print(text.upper())
# PASSWORD = 'привет'
# in_pass = input('Введите пароль: ')
# if in_pass.lower() == PASSWORD.lower():
#     print(f'Пароль верный({in_pass})')
# else:
#     print(f'Пароль НЕверный({in_pass})')
# text = "Мама мыла РАМУ, Раму мыла мама!!!"
# print(text)
# # print(text.split())
# for word in text.split(" "):
#     print (word)
# print(text.replace("мыла", "подмывала"))

numbers = ["1", "2", "3", "4"]
print("!!!".join(numbers))
