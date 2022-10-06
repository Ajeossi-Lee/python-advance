"""
装饰器
Python装饰器的作用是使函数包装与方法包装(一个函数，接受函数并返回其增强函数)变得更容易阅读和理解

装饰器通常是一个命名的对象(不允许使用lambda表达式)，在被(装饰函数)调用时接受单一参数，并返回另一个可调用对象
这里用的是 "可调用(callable)", 而不是之前以为的 "函数"
事实上，任何可调用对象(任何实现了 __call__ 方法的对象都是可调用的)都可以用作装饰器，
它们返回的对象往往也不是简单的函数，而是实现了自己的 __call__ 方法的更复杂的类的实例。

# 作为一个函数
# 编写自定义装饰器有许多方法，但最简单的方法就是编写一个函数，返回包装原始函数调用的一个子函数
"""
def myDecorator(function):
    def wrapper(*arg, **kwargs):
        # 在调用原始函数之前，做点什么
        print('...starting')
        result = function(*arg, **kwargs)
        #在函数调用之后，做点什么
        print('...done')
        #并返回结果
        return result
    #返回wrapper作为装饰函数
    return wrapper

@myDecorator
def sum(x, y):
    return x + y

print(sum(1, 2))


# 作为一个类
import time
class Timer:
    def __init__(self, func) -> None:
        self.func = func

    def __call__(self, *args, **kwargs):
        start = time.time()
        ret = self.func(*args, **kwargs)
        print(f'Time: {time.time()-start}')
        return ret


@Timer
def add(a, b):
    time.sleep(1)
    return a+b


print(add(2, 3))


# 参数化装饰器 
# 需要用到第二层包装
def repeat(number=3):
    ''' 多次重复执行装饰函数
    返回最后一次原始函数调用的值作为结果
    :param number:重复次数，默认值是3
    '''
    def actual_decorator(function):
        def wrapper(*args, **kwargs):
            result = None
            for _ in range (number):
                result = function(*args, **kwargs)
            return result
        return wrapper
    return actual_decorator

@repeat(2)
def foo():
    print('foo')

foo()


# 保存内省的装饰器
# 使用装饰器的常见错误是在使用装饰器时不保存函数元数据(主要是文档字符串和原始函数名)

from functools import wraps
def preserving_decorator(function):
    @wraps(function)
    def wrapped(*args, **kwargs):
        '''包装函数内部文档'''
        return function(*args, ** kwargs)
    return wrapped


@preserving_decorator
def function_with_important_docstring():
    '''这是我们想要保存的重要文档字符串'''

print(function_with_important_docstring.__name__)
print(function_with_important_docstring.__doc__)
