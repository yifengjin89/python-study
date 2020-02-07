# 2/4/2020
# sorting

a = [1, 3, 4, 5, 2]
b = sorted(a)
print(a)  # output: a 不改变 ； [1, 3, 4, 5, 2]
print(b)  # output: [1, 2, 3, 4, 5]
# 如果想让 a 在原地改变，那就调用a 的内置排序算法
a.sort()  # 内置排序算法
print(a)  # output: [1, 2, 3, 4, 5]

def bubble_sort(list):  # bubble sort  # Time complexity： O(n^2);  best: O(n): 表示遍历一遍发现没有任何可以交换的元素
    for i in range(len(list) - 1):  # 控制循环次数 [5, 4, 3, 2, 7]  循环到 n - 1 的位置 [2], 因为最后一位已经是最大数字
        count = 0
        for j in range(len(list) - 1 - i):  # 班长从头走到尾；每走完一遍，最大的数字就到队伍尾部,所以不需要再查一次；(n-1-i)
            if list[j] > list[j + 1]:  #
                list[j], list[j + 1] = list[j + 1], list[j]
                count += 1
        if 0 == count:
            return


l = [6, 5, 4, 1, 2, 3]
print("before sort %s" % l)  # output: before sort [6, 5, 4, 1, 2, 3]
(bubble_sort(l))
print("after bubble sort %s" % l)  # output: after bubble sort [1, 2, 3, 4, 5, 6]


def selection_sort(list):
    for i in range(len(list) - 1):  # 控制循环次数 [5, 4, 3, 2, 7]  循环到 n - 1 的位置 [2], 因为最后一位已经是最大数字
        min_index = i  # setting min_index = first index ==> list[i]
        for j in range(i + 1, len(list)):  # 从第二位开始，因为要第一位设置成min_index，要和第二位的比较大小
            if list[min_index] > list[j]:  # 如果 list[min_index] > list[j] ==> 5 > 4
                min_index = j  # setting min_index = j ==>  ( j = 下标 1) ==>  (min_index = 元素 4)
        list[i], list[min_index] = list[min_index], list[i]  # 交换list[i]和list[min_index]的位置；元素4和元素 5 的位置；
        # 从右边无序的数列中找出最小的元素放到左边； 操作右边无序状态


print("")
l1 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print("before selection sort %s" % l1)  # output: before sort [6, 5, 4, 1, 2, 3]
(selection_sort(l1))
print("after selection sort %s" % l1)  # output: after bubble sort [1, 2, 3, 4, 5, 6]


def insert_sort(list):  # 从右边无序的数列中 的第一个 与 左边的有序数列进行对比
    # worse O(n^2);  best: O(n)
    for i in range(1, len(list)):  # 控制循环次数 start: 从第二位 i = 1 ; end: last
        for j in range(i, 0, -1):  # 从 start 第二位 j = 1 ;  end: 0 ;  every time - 1
            if list[j] < list[j - 1]:  # 如果 list[n] < list[n - 1] ;
                list[j], list[j - 1] = list[j - 1], list[j]  # 交换位置；每交换一次，都要再和当前位置的前一个元素再进行比较
            else:  # 如果 当前位置 比 前一位的 大
                break  # 跳出


print("")
l2 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print("before insert sort %s" % l2)  # output: before insert sort [54, 26, 93, 17, 77, 31, 44, 55, 20]
(insert_sort(l2))
print("after insert sort %s" % l2)  # output: after insert sort [17, 20, 26, 31, 44, 54, 55, 77, 93]


def merge_sort(list): # time complexity O(nlogn); space: O(n) # 递归空间复杂度 logn
    if len(list) == 1:  # 如果 只有一个元素在数组里 ； 跳出递归
        return
    mid = len(list) // 2  # 切割点； 中间元素
    left = list[:mid]        # 左半部分元素
    right = list[mid:]        # 右半部分元素

    merge_sort(left)        # 对左半部分进行递归； 不断地把list 分成 左半部分和右半部分； 直到只剩一个元素
    merge_sort(right)        # 对右半部分进行递归； 不断地把list 分成 左半部分和右半部分； 直到只剩一个元素

    i = j = k = 0        # index
    while i < len(left) and j < len(right):  # 在 i < 左半部分的长度 和 j < 右半部分的长度时候进行循环；第一次是2个单一元素进行比较
        if left[i] < right[j]:               # 如果 左半部分的元素 小于 右边部分的元素；
            list[k] = left[i]            # list[]里的第 k 个元素 被替换成 左边部分的那个元素
            i += 1                    # i 下标 指向 下一个元素； 同时；如果i 下标的值 == L左半部分的长度；循环结束
        else:
            list[k] = right[j]             # 反之；list[]里的第 k 个元素 被替换成 右半部分的那个元素
            j += 1                     # j 下标 指向 下一个元素； 同时；如果j 下标的值 == R右半部分的长度；循环结束
        k += 1                         # 不管那个元素 替换掉 原本list[]第k个元素； index k 都要往后移一位

    while i < len(left):   # 如果说 i < 左半部分的长度；那必然还有元素没有被替换进list里
        list[k] = left[i]  # 在list[k]的位置 替换 左半部分的那个元素
        i += 1          # i 下标 指向 下一个元素； 同时；如果i 下标的值 == L左半部分的长度；循环结束
        k += 1          # index k 往后移一位

    while j < len(right):   # 如果说 j < 右半部分的长度；那必然还有元素没有被替换进list里
        list[k] = right[j]  # 在list[k]的位置 替换 左半部分的那个元素
        j += 1          # j 下标 指向 下一个元素； 同时；如果j 下标的值 == R右半部分的长度；循环结束
        k += 1          # index k 往后移一位


arr = [3, 5, 6, 3, 2, 1, 4, 7, 9, 8]
merge_sort(arr)
print("merge sort: %s" % arr)  # output: [1, 2, 3, 3, 4, 5, 6, 7, 8, 9]


def quick_sort(ary, start, end):  # time complexity: average: O(nlogn) ; worth：O(n^2);  space: O(logn)
    if start >= end:  # 递归出口： start >= end;  ==> 分割区间直到 2个下标指针重合
        return

    pivot = ary[start]  # pivot 基准数 = ary[0] 第一位
    # import random;  pivot = ary[random.randint(start, end)] 随机选取下标；防止出现 最坏情况 O(n^2)
    left = start  # 左边的区间 = start ==> 0
    right = end   # 右边的区间 = end ==> len(ary) - 1

    while left <= right:   # 在左边区间的下标 <= 右边区间的下标的时候做循环；
        while left <= right and ary[left] < pivot:  # 在左边区间的下标 <= 右边区间的下标和左边区间的元素< 准值的时候做循环；
            left += 1   # 左边区间下标 + 1
        # [5, 4, 3, 5, 6, 9, 8, 7, 2, 1]
        # [1, 4, 3, 2, 6, 9, 8, 7, 5, 5]
        while left <= right and ary[right] > pivot: # 在左边区间的下标 <= 右边区间的下标和右边区间的元素> 准值的时候做循环；
            right -= 1  # 右边区间下标 - 1

        if left <= right: # 如果左边区间的下标值 <= 右边区间的下标准：
            ary[left], ary[right] = ary[right], ary[left] # 交换左边区间， 右边区间下标位置上的元素
            left += 1   # 左边区间下标 + 1
            right -= 1  # 右边区间下标 - 1
    # 关系 start < right < left < end
    quick_sort(ary, start, right)  # 递归 分割区间；从ary[0] ~ 上一次的循环退出的 right 的位置
    quick_sort(ary, left, end)     # 递归 分割区间；从上一次的循环退出的 left 的位置 ~ ary[end]
    # [3, 4, 2, 5, 1] pivot = 3 ==> [1, 4, 2, 5, 3] ==> [1, 2, 4, 5, 3] 循环退出
    # 递归部分：[1, 2] pi= 1; | [4, 5, 3] pi= 4;  ==> [1, 2] [3 ||5, 4] ==> [1, 2] [3]|[4, 5];pi= 4; ==>[1, 2, 3, 4, 5]
    # 递归空间复杂度 logn

arr = [5, 4, 3, 5, 6, 9, 8, 7, 2 ,1]
print("before quick sort: %s" % arr)  # output: before quick sort: [5, 4, 3, 5, 6, 9, 8, 7, 2, 1]
quick_sort(arr, 0, len(arr) - 1)
print("after quick sort: %s" % arr)   # output: after quick sort: [1, 2, 3, 4, 5, 5, 6, 7, 8, 9]






