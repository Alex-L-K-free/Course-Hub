# Задание 3.
# ДЗ
# 1. Реализовать логику для удаления продуктов из корзины
# 2. Реализовать логику для списания(удаления) бонусов
# (i) __sub__ и __rsub__
# Чек-поинт №8
# Реализовать методы __sub__ и __rsub__ :
# 1. Для удаления одного набора продуктов из другого набора продуктов
# 2. Реализовать удаление бонусных баллов (Products - целое число)



class Products:
    def __init__(self, products, bonuses=0):
       self.products = products
       self.bonuses = len(products)

    def price(self):
        return (sum(self.products.values()) - self.bonuses)

    def __sub__(self, other):
        if isinstance(other, int):
            return Products(self.products, self.bonuses - other)
        elif isinstance(other, Products):
            new_products = {}
            for product, price in self.products.items():
                if product not in other.products:
                    new_products[product] = price
            for product, price in new_products.items():
                if product not in other.products:
                    new_products[product] = price
            return Products(new_products)

    def __rsub__(self, other):
        if isinstance(other, int):
            return Products(self.products, self.bonuses - other)

my_basket = Products({"Молоко": 2, "Сыр": 3, "Кефир" : 4, "Хлеб" : 5})

print(f"Моя корзина с бонусами - {my_basket.price()}{" руб"}. {my_basket.products}")
print("#"*100)

del_products = Products({"Сыр": 3,"Кефир" : 4 })
print(f"Удаляемый продукт из корзины - {del_products.products}")
new_basket = my_basket - del_products

print(f"Моя корзина с бонусами  {new_basket.price()}{" руб"}. {new_basket.products}")