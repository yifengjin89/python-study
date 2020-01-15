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
