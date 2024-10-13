# 1. Создайте список years_list, содержащий год, в который вы родились, и каждый
# последующий год вплоть до вашего пятого дня рождения. Например, если вы
# родились в 1980 году, список будет выглядеть так: years_list = [1980, 1981,
# 1982, 1983, 1984, 1985].
# Если вам меньше пяти лет и вы уже читаете эту книгу, то я даже не знаю, что
# сказать.
years_list = [1978, 1979, 1980, 1981, 1982, 1983]

 # 2. В какой из годов, содержащихся в списке years_list, был ваш третий день рождения? Помните, в первый год вам было 0 лет.
print("мой третий день рождения ", years_list[3])

 # 3. В какой из годов, перечисленных в списке years_list, вам было больше всего лет?
print("мне было больше всего лет ", years_list[5])

# 4. Создайте список things, содержащий три элемента: "mozzarella", "cinderella",
# "salmonella".
things = ["mozzarella", "cinderella", "salmonella"]
print(things)

# 5. Напишите с большой буквы тот элемент списка things, который относится
# к человеку, а затем выведите список. Изменился ли элемент списка?
print(things)
print(things[1].title())
print(things[1][0].upper() + things[1][1:])

# 6. Переведите сырный элемент списка things в верхний регистр целиком и выведите список.
print(things[0].upper())

# 7. Удалите болезнь из списка things, получите Нобелевскую премию и затем выведите список на экран.
things.pop(2)
print(things)
things.remove("salmonella")
print(things)

# 8. Создайте список, который называется surprise и содержит элементы 'Groucho', 'Chico' и 'Harpo'.
surprise = ["Groucho", "Chico", "Harpo"]
print(surprise)

# 9. Напишите последний элемент списка surprise со строчной буквы, затем обратите его и напишите с прописной буквы.
surprise = ["Groucho", "Chico", "harpo"]
print(surprise)
print(surprise[2].title())
surprise.remove("harpo")
print(surprise)
surprise.append("Harpo")
print(surprise)

# 10. Создайте англо-французский словарь, который называется e2f, и выведите его на экран. Вот ваши первые слова: dog/chien, cat/chat и walrus/morse.
e2f = {
    "dog":"chien",
    "cat":"chat",
    "walrus":"morse"
}
# print(e2f)

# 11. Используя словарь e2f, выведите французский вариант слова walrus.
#print(e2f["walrus"])

# 12. Создайте французско-английский словарь f2e на основе словаря e2f. Используйте метод items.
f2e = {}
for eng, france in e2f.items():
    f2e[france] = eng
print(e2f)
print(f2e)

# 13. Используя словарь f2e, выведите английский вариант слова chien.
print(f2e["chien"])

# 14. Создайте и выведите на экран множество английских слов из ключей словаря e2f.
print(e2f.keys())
print(list(e2f.keys()))

# 15. Создайте многоуровневый словарь life. Используйте следующие строки для
# ключей верхнего уровня: 'animals', 'plants' и 'other'. Сделайте так, чтобы ключ
# 'animals' ссылался на другой словарь, имеющий ключи 'cats', 'octopi' и 'emus'.
# Сделайте так, чтобы ключ 'cats' ссылался на список строк со значениями 'Henri',
# 'Grumpy' и 'Lucy'. Остальные ключи должны ссылаться на пустые словари.
# life = {
#     "animals":{},
#     "plants":{},
#     "other":{},
# }
# print(life)
life = {
    "animals":{
        "cats": ["Henri", "Grumpy", "Lucy"],
        "octopi": {},
        "emus": {},
    },
    "plants":{},
    "other":{},
}
print(life)

# 16. Выведите на экран высокоуровневые ключи словаря life.
print(list(life.keys()))

# 17. Выведите на экран ключи life['animals'].
print(list(life["animals"].keys()))
# 18. Выведите значения life['animals']['cats'].
print(life['animals']['cats'])


