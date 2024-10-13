# Занятие 6. Метод __new__ и Singleton
# - Метод __new__
# - Singleton
# - Как и где хранятся ссылочные типы данных
# - super()

class Dog:
    def __new__(cls, *args, **kwargs):
        print(f'__new__ | {cls}')
        return super().__new__(cls)

    def __init__(self):
        print(f'__init__ | {self}')

dog1 = Dog()
print(dog1)



class DB:
    db_conector = None

    def __new__(cls, *args, **kwargs):
        if DB.db_conector is None:
            DB.db_conector = super().__new__(cls)
        return DB.db_conector

    def __init__(self, login, password):
        self.login = login
        self.password = password

    def save_data(self):
        print('Данные Сохранены')


    def delete_data(self):
        print('Данные Удалены')

    def __str__(self):
        return f'{self.login} | {self.password} | {id(self)}'


# db_conector1 = DB('postgres1', 'postgres1')
# db_conector2 = DB('postgres2', 'postgres2')

for i in range(1, 3):
    db_coonnector = DB('postgres1', 'postgres1')
    print(db_coonnector)
    db_coonnector.save_data()