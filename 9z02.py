# 1/3/2020
# List

list1 = [1, 2, 3, 4, 5]
print(list1[2:4])  # output : [3, 4]
print(3 in list1)  # 检查元素在list中   # output : True
sum = 0
index = 0
while index < len(list1):  # average
    sum += list1[index]
    index += 1
print("sum = %d , average = %d" % (sum, sum / len(list1)))
# output: sum = 15, average = 3
print("===========================================================")

list2 = [9, 10, 11]
list1.extend([7, 8])
list1.insert(1, 100)  # 在下标处添加一个元素， 原数据位置顺延
list1.extend(list2)  # 追加另一个列表中的多个值， 合并列表
print("list1 = %s" % list1)
# output:  list1 = [1, 100, 2, 3, 4, 5, 7, 8, 9, 10, 11]

list1.remove(100)  # 按元素内容移除  把 数据 ‘100’ 第一个匹配结果移除了
list1.pop()  # 按下标移除
print("list1 = %s" % list1)
# output:  list1 = [1, 2, 3, 4, 5, 7, 8, 9, 10]

list3 = [1, 2, 3, 3, 4, 3, 5, 2, 3, 6, 7, 3]
count_3 = list3.count(3)  # 查看元素在列表中出现的次数
i = 0
while i < count_3:  # 移除所有‘3’ 在list3 里
    list3.remove(3)
    i += 1
print("list3 after remove '3' = %s" % list3)
# output: list3 after remove '3' = [1, 2, 4, 5, 2, 6, 7]

list3.sort()
print("sort list3 %s" % list3)
# output: sort list3 [1, 2, 2, 4, 5, 6, 7]

list3.reverse()
print("reverse list3 %s" % list3)
# output: reverse list3 [7, 6, 5, 4, 2, 2, 1]
print("===========================================================")

nums = [3, 1, 7, 9, 6, 2, 2, 5, 8, 9]
print("nums = %s" % nums)
# output: nums = [3, 1, 7, 9, 6, 2, 2, 5, 8, 9]
if nums[0] > nums[1]:   # second max integer
    max = nums[0]
    sec = nums[1]
else:
    max = nums[1]
    sec = nums[0]
i = 2
while i < len(nums):
    if nums[i] > max:
        sec = max
        max = nums[i]
    if nums[i] > sec and nums[i] < max:
        sec = nums[i]
    i += 1
print("second max = %d" % sec)
# output: second max = 8

def secondMax(nums):  # second max integer
    nums.sort()
    count = nums.count(nums[len(nums) - 1])  # max(nums)
    i = 0
    while i < count:
        nums.pop()
        i += 1
    return nums[len(nums) - 1]
secMax = secondMax(nums)
print("second max integer: %d" % secMax)
# output: second max = 8
print("===========================================================")

# Word count
str = "    sunck   is a   good   man !"
str = str.strip()  #左对齐
print(str)
# output : sunck   is a   good   man !

i = 0
count = 0
while i < len(str):
    while str[i] != " ":
        i += 1
        if i == len(str):
            break
    count += 1
    if i == len(str):
        break
    while str[i] == " ":
        i += 1

print("word count = %d" % count)
# output : word count = 6
print("===========================================================")

num1 = 10
if num1 > 15:
    print("111")
elif num1 < 18:
    print("222")
elif num1 < 22:
    print("333")
print("===========================================================")

