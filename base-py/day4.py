"""
闭包
"""

# 定义⼀个外部函数
def func_out(num1):
    # 定义⼀个内部函数
    def func_inner(num2):
        nonlocal num1 # 告诉解释器，此处使⽤的是 外部变量a
        # 修改外部变量num1
        num1 = 10
        # 内部函数使⽤了外部函数的变量(num1)
        result = num1 + num2
        print("结果是:", result)

    print(num1)
    func_inner(1)
    print(num1)
        # 外部函数返回了内部函数，这⾥返回的内部函数就是闭包
    return func_inner
# 创建闭包实例
f = func_out(1)
# 执⾏闭包
f(2)
