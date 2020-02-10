# 1/7/2020
# Function
import math


# root of equation . Given an equation ax^2 + bx + c = 0. Find root of equation
# 求根公式x=[-b ± √(b²-4ac)]/2a
def rootOfEquation(a, b, c):
    if b * b - 4 * a * c < 0:  # 判断方程是否有根  如果 <0 , 就是没有根， 返回空的list
        return []
    if b * b - 4 * a * c == 0:  # 判断方程是否只有一个根， 如果只有一个根， 返回 -b / 2a
        return [-b / (2.0 * a)]

    delta = math.sqrt(b * b - 4 * a * c)
    return sorted([(-b - delta) / (2.0 * a), (-b + delta) / (2.0 * a)])
    # return -b ± √(b²-4ac)]/2a  要求返回 [小的在前， 大的在后] ， 所以使用sorted 排序


root = rootOfEquation(-4, 56, 288)
print(root)  # output: [-4.0, 18.0]

# class 类 与 对象 object 的定义和使用
'''
什么是对象：
小狗
电脑
汽车

对象的属性：
小狗： 四条腿
汽车： 四个轮子， 方向盘
电脑： 屏幕， 键盘

对象的行为：
小狗： 汪汪叫
汽车： 加减速，转弯
电脑： 运行程序，播放视频
'''
print("===========================================================")


class Dog():

    def __init__(self, name, age):  # 构造函数
        self.name = name  # 属性   # pubilc member ；/ self.name 可以直接调用
        self.age = age  # 属性

    def speak(self):  # 行为 或者 叫 方法    self 是对象本身
        return "Wow"  # 返回行为


dog1 = Dog("Wangcai", 19)  # dog 是 对象
print(dog1.name)  # output: Wangcai
print(dog1.age)  # output: 19
print(dog1.speak())  # output: Wangcai： Wow
print(hasattr(dog1, "name"))  # 查看 是否有 “name” 的属性 或 方法  output: return True

print(getattr(dog1, "name"))  # 等价 dog1.name   属性 不用加（）  output:  Wangcai

print(getattr(dog1, "speak"))  # 等价 dog1.speak  output:  speak 的地址

print(getattr(dog1, "speak")())  # 等价 dog1.speak()  方法 必须加 （）  output:  Wow

setattr(dog1, "weight", 30)  # 设置一个属性
print(dog1.weight)  # output： 30

print("===========================================================")


class Person:
    # private member :  安全， 更好的进行控制 ； 访问私有属性，必须通过类的方法
    def __init__(self, name):
        self.__name = name  # private member

    def get_name(self):  # 访问私有属性的方法
        return self.__name

    def set_name(self, name):
        assert len(name) <= 10  # 限制“name” 长度 <= 10； 如果set_name:"linghu chong" , 长度超过10， 就不允许了
        self.__name = name


p = Person("Lingpz")
# if print(p.__name), it does not work because p.__name is private
# private 只能在class的内部去访问他,例如 get_name(self)
print(p.get_name())  # output: Lingpz
p.set_name("Ling Chong")
print(p.get_name())  # output: Ling Chong
print("===========================================================")


class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):  # 转换成字符串 ；  等价 toString
        return "[%s, %s]" % (self.x, self.y)

    def __add__(self, other):  # add method       # v1 = self.x, self.y = [1, 2] , v2 = other.x, other. y = [3, 4]
        return Vector(self.x + other.x, self.y + other.y)


v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1)  # if not using def __str__(self) method, output: <__main__.Vector object at 0x000001F87FF4CF98>

print(v2)  # if using def __str__(self) method, output: [1, 2]

v3 = v1 + v2  # v1 = self.x, self.y = [1, 2] , v2 = other.x, other. y = [3, 4]

# print(v3)  if not using def __add__(self, other) method, can not operate add method and also occur error
print(v3)  # using def __add__(self, other) method, output: [4, 6]
print("===========================================================")


# 类的继承
class Animal:  # 父类

    def __init__(self, name):
        self.name = name
        self._color = "red"

    def get_color(self):        # public
        return self._color

    def _get_color(self):       # protected  单下划线 _get_color
        return self._color

    def __get_color(self):      # private    双下划线 __get_color
        return self._color

    def speak(self):
        return "LOL"


class Dog(Animal):  # 继承父类 Animal

    def __init__(self, name):
        Animal.__init__(self, name)

    def speak(self):
        return self.name + ": Wow"


class Cat(Animal):  # 继承父类 Animal

    def __init__(self, name):
        Animal.__init__(self, name)


dog2 = Dog("Ruhua")
print(dog2.name)     # output: Ruhua
print(dog2.speak())  # output: Ruhua: Wow  # 重新定义了speak ； 并且覆盖了父类的speak
print(dog2.get_color())  # output: red    # public, it can be used
print(dog2._get_color())  # output: red    # protected, it can be used
# print(dog2.__get_color())  # private , can not be used, it occur error

cat2 = Cat("Xiaomao")
print(cat2.name)   # output: Xiaomao
print(cat2.speak())  # output: LOL     # 直接调用父类的speak
print(isinstance(dog2, Dog))          # 判断是否是继承关系  output： True
print(isinstance(dog2, Animal))       #  output： True
print("===========================================================")

# try/ except
a, b = None, None
try:
    a = 2
except:
    a = 100
else:
    b = 200

print(a, b)  # output : 2   200  # a 没有发生异常，运行 a = 2,  else: b = 200
print("===========================================================")
a, b = None, None
try:
    a[1] = 2
except:
    a = 100
else:
    b = 200

print(a, b)  # output: 100  None   # a 发生异常， 运行 except a = 100, 没有运行 else， 所以 b = None
print("===========================================================")
