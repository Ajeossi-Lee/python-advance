"""
f-string
字符串格式化输出
"""

name = 'lee'
age = 29

format_string = f'my name is {name} and age is {age}'
print(format_string)

format_string1 = f'my name is {{name}} and age is {{age}}'
print(format_string1)

number_add = f'3 + 5 = {3 + 5}'
print(number_add)

float_object = 0.99 
print(f'float is {float_object}')

"""
eval + repr
copy 浅拷贝
"""

info = 'ajeossi'
list_object = eval('[' + ','.join([repr(i) for i in info]) + ']')
print(list_object)
print(type(list_object))

heros = ['孙悟空', '林冲', '赵子龙', '李云龙']
hero_copy = heros.copy()
print(heros == hero_copy)
heros.append('黄继光')
print(heros)
print(hero_copy)

obj = {
    'Name': 'Zara', 
    'Age': 7, 
    'Class': 'First',
    'nums': [1, 3, 5, 7]
}
# 浅拷贝
obj_copy = obj.copy()
obj['nums'].append(9)
print(obj)
print(obj_copy)
