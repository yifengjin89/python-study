# 1/6/2020
# Tuple
# 节省内存空间，并且可以作为KEY 在 dict内
# List 转 hash， 要先转Tuple
tuple1 = (1, 2, 3, 2, [5, 6, 7])
t2 = list(tuple1)
print(t2)
# output: [1, 2, 3, 2, [5, 6, 7]]
tuple2 = (10,)
print(tuple2) # output: (10,) 当只有一个元素在tuple里， 必须加逗号
print("===========================================================")

# List 去重复
a = [11, 22, 33, 11, 22, 33]
b = []
for i in a:
    if i not in b:
        b.append(i)
print("去重操作前：")
print(a)  # output : [11, 22, 33, 11, 22, 33]
print("去重操作后：")
print(b)  # output : [11, 22, 33]
print("===========================================================")

# string  count word  #spilt 切割符
str1 = "sunck,,is,,,a,good,,man"
list1 = str1.split(",")
count = 0
print("list1 = %s " % (list1))
# output: list1 = ['sunck', '', 'is', '', '', 'a', 'good', '', 'man']

for i in list1:
    if len(i) > 0:
        count += 1
print("count word = %d" % count)
# output: count word = 5

print("===========================================================")
str2 = " ".join(list1)  # 以指定的字符串分隔符，组合成一个字符串
print("重组被分割的字符串： %s" % str2)
# output: 重组被分割的字符串： sunck  is   a good  man

list2 = str2.split()
print("list2 = %s " % list2)
# output : list2 = ['sunck', 'is', 'a', 'good', 'man']

str3 = " ".join(list2)
print("str3 :  %s" % str3)
# output : str3 :  sunck is a good man

print("===========================================================")

# String replace
str3 = "sunck is a good good good man"
str4 = str3.replace("good", "nice", 1)
print("str3: %s" % str3)
# output : str3: sunck is a good good good man
print("replace good to nice : %s" % str4)
# output: replace good to nice : sunck is a nice good good man

print("===========================================================")
# isalnum :  string contain 字母 or 数字， return True
str4 = "123"
str5 = "123ABC"
print(str4.isalnum())  # output: True
print(str5.isalnum())  # output: True

print("===========================================================")

# dict 字典
# 和list 比较： 优点：查找和插入的速度极快，不会随着key-value的增加而变慢
#              缺点： 需要占用大量内存，内存浪费多
# 使用字典， 学生姓名为Key， 成绩为 Value
dict1 = {"Tom": 60, "Lilei": 70}
# 元素的访问   获取：字典名[key]
print("Tom : %s" % dict1["Tom"])
# output: Tom : 60

print("Tom : %s" % dict1.get("Tom"))
# output: Tom : 60

ret = dict1.get("Tom")
if ret == None:
    print("None")
else:
    print("Get it")
# output: Get it

print("===========================================================")
# 添加 ，修改 和删除
dict1["Hameimei"] = 90  # dict1 里没有这个key， 就是添加
dict1["Lilei"] = 80  # dict1 里面有个这个key， 就是修改
dict1["Lilei"] = dict1["Lilei"] + 1
dict1.pop("Tom")  # 删除 key
print("dict1 = %s" % dict1)
# output: dict1 = {'Lilei': 81, 'Hameimei': 90}

for key in dict1.keys():  # print key only
    print(key)
    # output : Lilei Hameimei

for value in dict1.values():  # print value only
    print(value)
    # output : 81   90

for k, v in dict1.items():  # print both key, value
    print(k, v)
    '''
     output :
      Lilei 81
      Hameimei 90
    '''
print("===========================================================")
# Using dict to count word
str5 = "sunck is a good man!  sunck is a good man! sunck is a nice man!" \
       " sunck is a big man!, sunck is a cool man!"
dict2 = {}
list3 = str5.split(" ")  # 1. 以空格切割字符串
print("list3 = %s" % list3)
# output: list3 = ['sunck', 'is', 'a', 'good', 'man!', '', 'sunck', 'is', 'a', 'good', 'man!', 'sunck', 'is',
# 'a', 'nice', 'man!', 'sunck', 'is', 'a', 'big', 'man!,', 'sunck', 'is', 'a', 'cool', 'man!']

for KEY in list3:  # 2. 循环处理列表中的每个元素
    c = dict2.get(KEY)  # 3. 以元素当做KEY 去一个字典中提取数据
    if c == None:  # 4. 如果没有提取到， 就以该元素作为KEY，1作为value 存进字典
        dict2[KEY] = 1  # 添加 KEY into dict2
        # 例子： if c == none, dict2 = {'sunck': 1, 'is': 1, 'a': 1, 'good': 1, 'man!': 1, '': 1}
    else:  # 5. 如果提取到，将对应的KEY的value修改， 值加1
        dict2[KEY] += 1  # 修改 KEY 的 value
        # 例子： else, dict2 = {'sunck': 2, 'is': 2, 'a': 1, 'good': 1, 'man!': 1, '': 1}
print("dict2 %s" % dict2)
# output: dict2 {'sunck': 5, 'is': 5, 'a': 5, 'good': 2, 'man!': 4, '': 1, 'nice': 1, 'big': 1, 'man!,': 1, 'cool': 1}

print("count 'sunck' in dict2 : %s" % dict2.get("sunck"))
# output: count 'sunck' in dict2 : 5

print("count 'sunck' in list3 : %s" % list3.count("sunck"))
# output: count 'sunck' in list3 : 5

print("===========================================================")
# 练习  时间加1sec
time = "11:25:59"
def timeplus(time):
    timeSplit = time.split(":")
    hour = int(timeSplit[0])
    min = int(timeSplit[1])
    sec = int(timeSplit[2])
    sec += 1
    if sec == 60:
        min += 1
        sec = 0
        if min == 60:
            hour += 1
            min = 0
            if hour == 24:
                hour = 0
    print("time now : %s, after + 1 second,  %.2d: %.2d：%.2d" % (time, hour, min, sec))
timeplus(time)
# output: time now : 11:25:59, after + 1 second,  11: 26：00

print("===========================================================")