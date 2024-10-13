# Занятие 4. Args и Kwargs
# - Распаковка списков и кортежей через *
# - args и kwargs

# 1
a, *b, c = ['a', 'b', 1, 2, 3, 4, 5]
print(a)
print(b)
print(c)
# 2
print('=' * 80)
nums = [5, 10]
print(list(range(10)))
print(list(range(5, 10)))
print(list(range(*nums)))
# 3
print('=' * 80)
print(1, 2, 3)
print(*[1, 2, 3])
a, b, c = [1, 2, 3]
print(a, b, c)
# 4
print('=' * 80)
print('=' * 80)
def ab(a, b):
    print(a, b)
elems = ['a', 'b']
ab('a', 'b')
ab(*elems)
ab(*['a', 'b'])
ab('a', 'b')
# 5
print('=' * 80)
def super_sum1(numbers):
    res = 0
    for number in numbers:
        res += number
        print(f'Сумма = {res}')
super_sum1([1, 2, 3, 4, 5])
print('=' * 80)
def super_sum2(*numbers):
    res = 0
    for number in numbers:
        res += number
        print(f'Сумма = {res}')
super_sum2(1, 2, 3, 4, 5)
print('=' * 80)
# 6
print(1, 2, 3, 4)
print(1, 2, 3, 4, sep='\n')
# 7
print('=' * 80)
def func(arg1, arg2, *args, **kwargs):
    print(arg1)
    print(arg2)
    print(args)
    print(kwargs)
func(
    1, 2, 'a', 'b', 'EEEEEEE', [1, 2, 3],
    key1='123', key2='abc', key3='123'
)