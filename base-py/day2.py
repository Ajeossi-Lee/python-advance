'''
高阶函数
'''

# map(function, list) 会根据提供的函数对指定序列做映射
my_list = [1, 2, 3, 4, 5]

def func(x):
    return x ** 2

res = map(func, my_list)
print(list(res))

# reduce(function, list) 函数会对参数序列中元素进⾏累计
import functools

my_list = [1, 2, 3, 4, 5]

def f(x1, x2):
    return x1 + x2

result = functools.reduce(f, my_list)
print(result)

# filter函数⽤于过滤序列, 过滤掉不符合条件的元素, 返回⼀个filter对象, 如果要转换为列表, 可以使⽤list来转换
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def f1(x):
    return x % 2 == 0
    
result = filter(f1, list1)
print(list(result))
