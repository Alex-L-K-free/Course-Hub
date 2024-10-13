# Занятие 2. Сравнение объекта со словарём
# Отличие объекта и словаря

class Cat:
    age = 2
    name = 'Муся'

cat1 = {
    'age': 2,
    'name': 'Василий',
}
cat2 = Cat()
cat3 = Cat()

print(cat1['name'])
print(cat2.name)
print(cat3.name)

print(cat1)
print(cat2.__dict__)