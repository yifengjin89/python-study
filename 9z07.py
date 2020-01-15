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