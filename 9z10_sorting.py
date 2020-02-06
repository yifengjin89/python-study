# 2/4/2020
# sorting


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


def merge_sort(list):
    if len(list) == 1:  # 如果 只有一个元素在数组里 ； 跳出递归
        return
    mid = len(list) // 2  # 切割点； 中间元素
    L = list[:mid]        # 左半部分元素
    R = list[mid:]        # 右半部分元素

    merge_sort(L)        # 对左半部分进行递归； 不断地把list 分成 左半部分和右半部分； 直到只剩一个元素
    merge_sort(R)        # 对右半部分进行递归； 不断地把list 分成 左半部分和右半部分； 直到只剩一个元素

    i = j = k = 0        # index
    while i < len(L) and j < len(R):  # 在 i < 左半部分的长度 和 j < 右半部分的长度时候进行循环；第一次是2个单一元素进行比较
        if L[i] < R[j]:               # 如果 左半部分的元素 小于 右边部分的元素；
            list[k] = L[i]            # list[]里的第 k 个元素 被替换成 左边部分的那个元素
            i += 1                    # i 下标 指向 下一个元素； 同时；如果i 下标的值 == L左半部分的长度；循环结束
        else:
            list[k] = R[j]             # 反之；list[]里的第 k 个元素 被替换成 右半部分的那个元素
            j += 1                     # j 下标 指向 下一个元素； 同时；如果j 下标的值 == R右半部分的长度；循环结束
        k += 1                         # 不管那个元素 替换掉 原本list[]第k个元素； index k 都要往后移一位

    while i < len(L):   # 如果说 i < 左半部分的长度；那必然还有元素没有被替换进list里
        list[k] = L[i]  # 在list[k]的位置 替换 左半部分的那个元素
        i += 1          # i 下标 指向 下一个元素； 同时；如果i 下标的值 == L左半部分的长度；循环结束
        k += 1          # index k 往后移一位

    while j < len(R):   # 如果说 j < 右半部分的长度；那必然还有元素没有被替换进list里
        list[k] = R[j]  # 在list[k]的位置 替换 左半部分的那个元素
        j += 1          # j 下标 指向 下一个元素； 同时；如果j 下标的值 == R右半部分的长度；循环结束
        k += 1          # index k 往后移一位


arr = [3, 5, 6, 3, 2, 1, 4, 7, 9, 8]
merge_sort(arr)
print("merge sort: %s" % arr)  # output: [1, 2, 3, 3, 4, 5, 6, 7, 8, 9]

