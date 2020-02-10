# 1/13/2020
# set
# 类似dict， 是一组key的集合， 不存储value；  本质： 无序和无重复的集合
# 创建set需要一个list或者tuple或者dict作为输入集合
# 重复元素自动被过滤

s1 = set([1, 2, 3, 4, 5, 5, 6, 6])
print("s1 =%s" % s1)  # output: s1 ={1, 2, 3, 4, 5, 6}

s2 = set((1, 1, 2, 2, 3))
print("s2 =%s" % s2)  # output: s2 ={1, 2, 3}

s3 = set({1: "good", 2: "nice"})
print("s3 =%s" % s3)  # output: s3 ={1, 2}

s4 = {1, 3, 5, 5}
print("s4 =%s" % s4)  # output: s4 = {1, 3, 5}

s4.add(6)  # add 不能添加list 和 dict 元素
print("s4 =%s" % s4)  # output: s4 = {1, 3, 5, 6}
print("===========================================================")

s4.update([6, 7, 8, 9, "good"])  # update 可以添加 list，tuple， string打碎插入
print("s4 =%s" % s4)  # output: s4 ={1, 3, 5, 6, 7, 8, 9, 'good'}
s4.update("nice")
print("s4 =%s" % s4)  # output: s4 ={1, 3, 5, 6, 7, 8, 9, 'i', 'e', 'c', 'n', 'good'} 无序！
print("===========================================================")

s4.remove(1)
print("s4 =%s" % s4)  # output: s4 ={3, 5, 6, 7, 8, 9, 'i', 'e', 'c', 'n', 'good'} 无序！

s5 = set([1, 2, 3])
s6 = {2, 3, 4}
s7 = s5 & s6  # 交集
print("s7 = %s" % s7)  # output: {2, 3}

s8 = s5 | s6  # 并集
print("s7 = %s" % s8)  # output: {1, 2, 3, 4}
print("===========================================================")

# 可迭代对象： 可以直接作用于for循环的对象统称为可迭代对象（Iterable）。
# 可以用isinstance()去判断一个对象是否是Iterable对象
# 可以直接作用于for的数据类型一般分两种
# 1. 集合数据类型， 例如list， tuple， dict， set， string
# 2. 是generator, 包括生成器和带yield的generator function


# 迭代器： 不但可以作用于for循环， 还可以被next()函数不断调用返回并返回下一个值，
# 直到最后跑出一个StopIteration错误表示无法继续返回下一个值

# 可以被next() 函数调用并不断返回下一个值的对象被称为迭代器

# （Iterator)对象 ： 可以使用isinstance（）函数判断一个对象是否是Iterator对象
l = (x for x in [1, 2, 3])
print(next(l))  # output: 1
print(next(l))  # output: 2
print(next(l))  # output: 3

# 转换成Iterator对象
l1 = iter([1, 2, 3, 4, 5])
print(next(l1))  # output：1
print(next(l1))  # output: 2
print("===========================================================")


# 值传递： 传递的不可变类型; string, tuple, number是不可变类型
def fun1(num):
    num = 10
    print(num)


temp = 20
fun1(temp)  # output： 10
print(temp)  # output： 20


# 引用传递： 传递的可变类型； list, dict, set 是可变的
def fun2(lis):
    lis[0] = 100
    print(lis)


list1 = [1, 2, 3]
fun2(list1)  # output: [100, 2, 3]
print(list1)  # output: [100, 2, 3]
print("===========================================================")
# 匿名函数 ； lambda
sum = lambda num1, num2: num1 + num2
print(sum(1, 2))  # output: 3


# 加了星号(*)的变量存放所有未命名的变量参数，如果在函数调用时没有指定参数，他就是个空元祖
def fun2(name, *args):
    print(name)
    for x in args:
        print(x)


fun2("sunck", "good", "nice", "handsome")  # output: sunck   good  nice  handsome


def mySum(*l):
    sum = 0
    for i in l:
        sum += i
    return sum


print(mySum(1, 2, 3, 4, 5))  # output: 15
print("===========================================================")


# **kwargs 代表键值对的参数字典，和 *args 类似
def func3(**kwargs):
    print(kwargs)


func3(x=1, y=2, z=3)  # output: {'x': 1, 'y': 2, 'z': 3}


# 接收任意参数
def func4(*args, **kwargs):
    pass  # 代表空语句


print("===========================================================")


# 装饰器
def func5():
    print("sunch is a good man")


def outer(fun):
    def inner():
        print("********************")
        func5()

    return inner


f = outer(func5)
f()  # output: ******************** ;  sunch is a good man

print("===========================================================")
# 程序异常
try:
    print(5 / 0)
except (NameError, ZeroDivisionError):
    print("出现了NameError or ZeroDivisionError")
    # output: 出现了NameError or ZeroDivisionError
print("===========================================================")

# 读写文件
# 读文件
path = r"C:\Users\tony_\PycharmProjects\9Zhang_01\python-study\file1.txt"
f = open(path, "r", encoding="utf-8")

# 读文件内容
str1 = f.read()
print(str1) # outpur: Sunck is a good man, Sunck is a handsome man.
            # Sunck is a nice man.

print("===========================================================")
# 一个完整的读文件过程
try:
    f1 = open(path, "r", encoding="utf-8")
    print(f1.read())
finally:
    if f1:
        f1.close()

print("===========================================================")

# 使用 with 读取文件， 文件自动关闭
with open(path, "r", encoding="utf-8") as f2:
    print(f2.read())

print("===========================================================")