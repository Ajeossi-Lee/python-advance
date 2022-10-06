"""
类

案例：
class DistinctError(ValueError):
    '''如果向DistinctDict添加重复值，则引发这个错误'''


class DistinctDict(dict):
    '''不接受重复值的字典'''

    def __setitem__(self, key, value):
        if value in self.values():
            if (
                (key in self and self[key] != value) or
                key not in self
            ):
                raise DistinctError(
                    "This value already exists for different key"
                )
        super().__setitem__(key, value)


d = DistinctDict()
d['key'] = 'value'
d['other_key'] = 'value'

"""

"""
# Todo: ???
# super
class Mama:
    def says(self):
        print('do your homework')

class Sister(Mama):
    def says(self):
        super().says()
        print('and clean your bedroom')

super的简化形式(不传入任何参数)可以在方法内部使用，但super的使用并不限于方法
在代码中需要调用给定实例的超类方法的任何地方都可以使用它
不过，如果super不在方法内部使用，那么必须给出如下参数:
anita = Sister()
super(anita.__class__, anita)
>> do your homework

"""


class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    def __repr__(self):
        return f"Pizza with {' and '.join(self.toppings)}"

    @classmethod
    def recommend(cls):
        '''推荐任意馅料( toppings)的某种披萨'''
        return cls(['spam', 'ham', 'eggs'])


class VikingPizza(Pizza):
    @classmethod
    def recommend(cls):
        '''推荐与super相同的内容，但多加了午餐肉(spam)'''
        recommended = super().recommend()
        recommended.toppings += ['spam'] * 5
        return recommended

print(Pizza.recommend())
print(VikingPizza.recommend())


# 继承类的方法解析顺序 __mro__

# 高级属性访问模式

"""
# 描述符
__set__
__get__
__delete__
__getattribute__(): 属性查找 

属性获取: (隐式地调用__getattribute__())
instance.attribute
getattr(instance, 'attribute')
查找顺序:
1.验证该属性是否为实例的类对象的数据描述符
2.如果不是，就查看该属性是否能在实例对象的__dict__中找到。
3.最后，查看该属性是否为实例的类对象的非数据描述符

hasattr: 判断是否存在属性

property: 内置的描述符类型

__slots__: 为指定的类设置一个静态属性列表
限制一组可用的属性，但是可以向派生类中添加新属性
"""

# 元类编程

# 代码生成 
# exec、eval和compile