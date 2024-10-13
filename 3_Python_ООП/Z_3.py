# Занятие 3. Объекты с уникальными значениями
# - Свои уникальные значения у объектов
# - Конструктор и Деструктор(Инициализатор и финализатор)

class Cat:
    def __init__(self, name='Кот', age=1):
        self.name = name
        self.age = age
        print(f'Кот {name} родился')

    def __del__(self):
        print(f'Кот {self.name} закончился')


cat1 = Cat('Вася', 3)
cat2 = Cat('Муся', 3)
cat3 = Cat()
print(f'Кот {cat3.name} закончился')

print(cat1.name)
# print(cat2.name)
# print(cat3.name)

# cat4 = {
#     'name': 'Василий',
#     'age': 2
# }
# print(cat1.__dict__)
# print(cat4)