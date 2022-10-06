# 1、列表推导式
[i for i in range(10) if i % 2 == 0]
# 不仅高效, 而且简洁易懂

# 2、enumerate获取列表索引和值

# 3、zip函数对两个大小相等的可迭代对象进行遍历

# 4、序列解包
first, second, *rest = 0, 1, 2, 3
(a, b), (c, d) = (1, 2), (3, 4)

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
"""
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
yield 语句
生成器提供了一种优雅的方法，可以让编写返回元素序列的函数所需的代码变得简单、高效
基于yield语句， 生成器可以暂停函数并返回一个中间结果
该函数会保存执行上下文，稍后在必要时可以恢复

每次你需要返回一个序列的函数或在循环中运行的函数时，都应该考虑使用生成器
"""
def fibonacci():
    a, b = 0, 1
    while True:
        yield a, b
        a, b = b, a + b

"""
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

# 作为一个函数 contextlib模块
"""

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
