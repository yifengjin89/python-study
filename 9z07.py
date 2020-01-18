# 1/14/2020

# String to Integer

class Solution:

    def stringToInteger(self, str):
        sign = 1
        stat = 0
        if str[0] == "-":
            sign = -1
            stat = 1
        num = 0
        # -123     123
        # num = 0   0 * 10 + 1 = 1
        # num = 1   1 * 10 + 2 = 12
        # num = 12  12 * 10 + 3 = 123

        for i in range(stat, len(str)):
            num = num * 10 + ord(str[i]) - ord("0")

        return num * sign

solution = Solution()
print(solution.stringToInteger("-123"))  # output: -123
print("===========================================================")


class Solution1:
    """
    @param str: An array of char
    @param offset: An integer
    @return: nothing
    """
    def rotateString(self, s, offset):
        # write your code here
        if len(s) > 0:
            offset = offset % len(s)
        # "a", "b", "c", "d", "e", "f", "g", "a", "b", "c", "d", "e", "f", "g"
        temp = (s * 2)[len(s) - offset: 2 * len(s) - offset]
        for i in range(len(temp)):
            s[i] = temp[i]
        return s
solution1 = Solution1()
list1 = ["a", "b", "c", "d", "e", "f", "g"]
print(solution1.rotateString(list1, 3))  # output: ['e', 'f', 'g', 'a', 'b', 'c', 'd']
print("===========================================================")

# 引用的赋值
# 函数传递的时候，是传递的引用
def modify(nums):   #  引用对象（nums） 重新指向新的数据 等价于 修改引用数据， nums = [1, 2, 3];
                    #  但是被引用对象不变 ==》 array = [4, 5, 6]
    print("nums = %s" % nums)  # output: nums = [4, 5, 6]
    nums = [1, 2, 3]
    print("nums = %s" % nums)  # output: nums = [1, 2, 3]；；但是 array 依然不变 = [4, 5, 6] 因为 nums引用的是array的地址
                               # ，重新赋值后，改变只是nums，并没有改变array

array = [4, 5, 6]
modify(array)
print("array = %s" % array)  # output: array = [4, 5, 6]

print("===========================================================")

def modify2(nums2):   # 引用对象 (nums2) 指向内部修改 等价于 修改引用数据，nums2[2] = 1000  ==>   nums2 = [4, 5, 1000]
                      # 同时修改被引用对象  ==》 array2 = [4, 5, 1000]
    print("nums2 = %s" % nums2)  # output: nums2 = [4, 5, 6]
    nums2[2] = 1000
    print("nums2 = %s" % nums2)  # output: nums2 = [4, 5, 1000]；；

array2 = [4, 5, 6]
modify2(array2)
print("array2 = %s" % array2)  # output: array2 = [4, 5, 1000]

# LinkedList Class的接口
class ListNode:

    def __init__(self, val):
        self.val = val    # assign value
        self.next = None  # Initialize next as null


class LinkedList:

    def __init__(self):
        # dummy 虚拟的哨兵节点
        self.dummy = ListNode(-1)

    def get(self, location):  # 读取操作 ； 获取location位置上的node的value
        p = self.dummy.next
        for i in range(location):
            p = p.next

        return p.val

    def contains(self, val):   # 查找操作 ； 判断链表中是否含有value值得node
        p = self.dummy.next
        while p is not None:
            if p.val == val:
                return True
            p = p.next

        return False

    def add(self, location, val):  # 插入操作 ； 在location的位置上插入一个值为value的node
        p = self.dummy
        for i in range(location):
            p = p.next

        node = ListNode(val)
        node.next = p.next
        p.next = node

    def remove(self, location):  # 删除操作 删除location位置上的元素
        p = self.dummy
        for i in range(location):
            p = p.next

        p.next = p.next.next

    def empty(self):
        return self.dummy.next is None


linkedList = LinkedList()

linkedList.dummy = ListNode(0)
head = ListNode(10)
second = ListNode(20)

linkedList.dummy.next = head
head.next = second

for i in range(3):
    linkedList.add(i, 8)
print(linkedList.get(2))  # output: 100
print(linkedList.contains(100))
