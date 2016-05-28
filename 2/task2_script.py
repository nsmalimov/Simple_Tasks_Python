from functools import reduce

list1 = [1, 2, 3, 4, 0]


def foldl(list, char_op):
    if char_op == '+':
        return reduce(lambda x, y: x + y, list1)
    if char_op == '*':
        return reduce(lambda x, y: x * y, list1)
    if char_op == '/':
        try:
            num_0 = list1.index(0)
            if num_0 != len(list1) - 1:
                return '0 in the list'
        except:
            None
        return reduce(lambda x, y: x / y, list1)


print foldl(list1, '+')


def foldr(list, char_op):
    if char_op == '+':
        return reduce(lambda x, y: x + y, reversed(list1))
    if char_op == '*':
        return reduce(lambda x, y: x * y, reversed(list1))
    if char_op == '/':
        try:
            num_0 = list1.index(0)
            if num_0 != 0:
                return '0 in the list'
        except:
            None
        return reduce(lambda x, y: x / y, reversed(list1))


print foldr(list1, '+')


def func_mult(x):
    return x * x


def map_func(func, list):
    m = 0
    while m < len(list):
        list[m] = func(list[m])
        m = m + 1
    return list


list2 = [2, 2]
print map_func(func_mult, list2)
