"""
1、列表推导式
[i for i in range(10) if i % 2 == 0]
不仅高效, 而且简洁易懂

2、enumerate获取列表索引和值

3、zip函数对两个大小相等的可迭代对象进行遍历

4、序列解包
first, second, *rest = 0, 1, 2, 3
(a, b), (c, d) = (1, 2), (3, 4)
"""

"""
注意: 在复制和遍历字典的操作中, 最坏情况复杂度中的n是字典曾经达到的最大元素数目, 而不是当前元素数目
在某些情况下, 如果需要频繁遍历某个字典, 那么最好创建一个新的字典对象, 而不是仅在旧字典中删除元素

collections模块
    - namedtuple
    - deque
    - ChainMap
    - Counter
    - OrderedDict
    - defaultdict
"""

"""
迭代器
迭代器只不过是一个实现了迭代器协议的容器对象。
它基于以下两个方法:
    __next__ : 返回容器的下一个元素。
    __iter__ : 返回迭代器本身。
迭代器可以利用内置的iter函数和一个序列来创建

class CountDown:
    def __init__(self, step):
        self.step = step

    def __next__(self):
        '''Return the next element'''
        if self.step <= 0:
            raise StopIteration
        self.step -= 1
        return self.step

    def __iter__(self):
        '''Return the iterator itself'''
        return self

for ele in CountDown(4):
    print(ele)
"""

"""
yield 语句
生成器提供了一种优雅的方法，可以让编写返回元素序列的函数所需的代码变得简单、高效
基于yield语句，生成器可以暂停函数并返回一个中间结果
该函数会保存执行上下文，稍后在必要时可以恢复

def fibonacci():
    a, b = 0, 1
    while True:
        yield a, b
        a, b = b, a + b

每次你需要返回一个序列的函数或在循环中运行的函数时，都应该考虑使用生成器
"""

"""
装饰器
Python装饰器的作用是使函数包装与方法包装(一个函数，接受函数并返回其增强函数)变得更容易阅读和理解

装饰器通常是一个命名的对象(不允许使用lambda表达式)，在被(装饰函数)调用时接受单一参数，并返回另一个可调用对象
这里用的是 "可调用(callable)", 而不是之前以为的 "函数"
事实上，任何可调用对象(任何实现了 __call__ 方法的对象都是可调用的)都可以用作装饰器，
它们返回的对象往往也不是简单的函数，而是实现了自己的 __call__ 方法的更复杂的类的实例。


# 作为一个函数
# 编写自定义装饰器有许多方法，但最简单的方法就是编写一个函数，返回包装原始函数调用的一个子函数
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

# 应用
1、参数检查
2、缓存
3、代理
4、上下文提供者
"""

"""
上下文管理器 with语句
    - 关闭一个文件
    - 释放一个锁
    - 创建一个临时的代码补丁
    - 在特殊环境中运行受保护的代码

作为一个类
任何实现了，上下文管理器协议(context manager protocol)的对象都可以用作上下文管理器
该协议包含两个特殊方法：
    # https://docs.python.org/3.3/reference/datamodel.html
    __enter__(self): 
    __exit__(self, exc_ type, exc_ value, traceback)
    
执行with语句的过程如下:
    - 调用 __enter__ 方法 任何返回值都会绑定到指定的as子句
    - 执行内部代码块
    - 调用 __exit__ 方法

class ContextIllustrator:
    def __enter__(self):
        print('entering context')

    def __exit__(self, exc_type, exc_value, traceback):
        print('leaving context')

        if exc_type is None:
            print('with no error')
        else:
            print(f'with an error {exc_value}')


with ContextIllustrator():
    print("inside")

# 作为一个函数 contextlib模块
"""






