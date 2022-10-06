"""
装饰器
"""

#################### 1. 函数装饰器 ####################
# 添加输出⽇志的功能
def logging(fn):
    def inner(num1, num2):
        print("--正在努⼒计算--")
        fn(num1, num2)
        print("--ending--")
    return inner

# 使⽤装饰器装饰函数
@logging
def sum_num(a, b):
    result = a + b
    print(result)

sum_num(1, 2)


#################### 2. 装饰带有返回值的函数 ####################
# 添加输出⽇志的功能
def logging(fn):
    def inner(num1, num2):
        print("--正在努⼒计算--")
        result = fn(num1, num2)
        return result
    return inner

# 使⽤装饰器装饰函数
@logging
def sum_num(a, b):
    result = a + b
    return result

result = sum_num(1, 2)
print(result)


#################### 3. 装饰带有不定⻓参数的函数 ####################
# 添加输出⽇志的功能
def logging(fn):
    def inner(*args, **kwargs):
        print("--正在努⼒计算--")
        fn(*args, **kwargs)
    return inner

# 使⽤语法糖装饰函数
@logging
def sum_num(*args, **kwargs):
    result = 0
    for value in args:
        result += value
    for value in kwargs.values():
        result += value
    print(result)
    
sum_num(1, 2, a=10)


#################### 4. 多个装饰器的使⽤示例代码 ####################
def make_div(func):
    """对被装饰的函数的返回值 div标签"""
    def inner():
        return "<div>" + func() + "</div>"
    return inner

def make_p(func):
    """对被装饰的函数的返回值 p标签"""
    def inner():
        return "<p>" + func() + "</p>"
    return inner

# 装饰过程: 1 content = make_p(content) 2 content = make_div
# content = make_div(make_p(content))
@make_div
@make_p
def content():
    return "⼈⽣苦短"

result = content()
print(result)


#################### 5. 带有参数的装饰器 ####################
# 在装饰器外⾯再包裹上⼀个函数，让最外⾯的函数接收参数，返回的是装饰器，因为@符号后⾯必须是装饰器实例。
# 添加输出⽇志的功能
def logging(flag):
    def decorator(fn):
        def inner(num1, num2):
            if flag == "+":
                print("--正在努⼒加法计算--")
            elif flag == "-":
                print("--正在努⼒减法计算--")
            result = fn(num1, num2)
            return result
        return inner
    # 返回装饰器
    return decorator

# 使⽤装饰器装饰函数
@logging("+")
def add(a, b):
    result = a + b
    return result

@logging("-")
def sub(a, b):
    result = a - b
    return result

result = add(1, 2)
print(result)
result = sub(1, 2)
print(result)
'''
使⽤带有参数的装饰器，其实是在装饰器外⾯⼜包裹了⼀个函数，
使⽤该函数接收参数，返回是装饰器，因为 @ 符号需要配合装饰器实例使⽤
'''

#################### 6. 类装饰器的使⽤ ####################
# 通过定义⼀个类来装饰函
class Check(object):
    def __init__(self, fn):
        # 初始化操作在此完成
        self.__fn = fn
    
    # 实现__call__⽅法，表示对象是⼀个可调⽤对象，可以像调⽤函数⼀样
    def __call__(self, *args, **kwargs):
        # 添加装饰功能
        print("请先登陆...")
        self.__fn()

@Check
def comment():
    print("发表评论")

comment()

'''
要想类的实例对象能够像函数⼀样调⽤，需要在类⾥⾯使⽤call⽅法，
把类的实例变成可调⽤对象(callable)，也就是说可以像调⽤函数⼀样进⾏调⽤。

在call⽅法⾥进⾏对fn函数的装饰，可以添加额外的功能。
'''
