# 1/22/2020
# 递归 recursion
# 递归的定义： 首先这个问题或者数据结构得是递归定义的
# 递归的出口： 什么时候递归终止
# 递归的拆解： 递归不终止的时候，如何分解问题

# 方式：
# 1. 写出临界条件
# 2. 找一次和上一次的关系
# 3. 假设当前函数已经能用，调用自身计算上一次的结果，再求出本次的结果

# fibonacci
# 递归的定义： 因为斐波那契数列满足 F(n) = F(n-1) + F(n-2)
# 递归的出口： n = 0 和 n = 1 的时候，问题规模足够小的时候
# 递归的拆解： return fibonacci(n-1) + fibonacci(n-2)

list1 = []
def f(n):
    list1.append(n)
    if n == 1 or n == 2:
        return 1

    return f(n-1) + f(n-2)


print("res = %d" % f(5))   # res = 3
for i in list1:
    print("f(%d)" % i, end=" ")  # output: f(5) f(4) f(3) f(2) f(1) f(2) f(3) f(2) f(1)


list2 = []
def f(n):
    list2.append(n)
    if n == 1 or n == 2:
        return 1

    return f(n-2) + f(n-1)

print("")

print("res = %d" % f(5))  # res = 3
for i in list2:
    print("f(%d)" % i, end=" ")  # output: f(5) f(3) f(1) f(2) f(4) f(2) f(3) f(1) f(2)

print("")
print("======================================")

# fibonacci loop
def fib(N):
    a = 0
    b = 1
    if N <= 0:
        return a
    if N == 2 or N == 1:
        return b
    while N > 0:
        a, b = b, a + b
        N -= 1
    return a

print(fib(3))

print("======================================")
def fib_loop(n):
    a, b = 0, 1  # f(0) = 0 , f(1) = 1
    for i in range(n):
        a, b = b, a + b    # f(n-1) + f(n-2)
    return a

print(fib_loop(6))
print("======================================")

# Tree 树
# 树的概念： 是一种抽象数据类型，用来模拟具有树状结构性质的数据集合，它由n(n>-1) 个有限节点组成一个具有层次关系的集合。
# 树： 好比一个公司
# * 由节点(node)组成
# * 每个节点有零个或多个子节点(child node) ； 这是一个manager，他管理很多人
# * 没有父节点的是根节点(root node) ； 公司的大BOSS
# * 每个非根节点只有一个父节点(parent node) ; 除了大BOSS， 每个人都有一个manager
# * 没有任何子节点的节点都叫叶子节点(leaf node) ； 底层的员工
# * 一颗树中，只有一个root node ； 大BOSS只允许有一个

# 二叉树(binary tree)
# * 每个节点 最多 有两个子节点
# * 两个子节点分别被称为左孩子(left node) 和 右孩子(right node)
# * 叶子节点： 没有孩子节点的节点
# * 不特别说明的话， 我们提到的树是指二叉树
# 二叉树的性质：
# 在二叉树的第i层上， 最多有 2^(i-1)个节点 比如在第3层，i = 3,  最多有 2^(3-1) = 4 个节点
# 深度为k的二叉树最多有 2^k - 1个节点  ； 比如深度为4， k = 4, 2^4 - 1 = 15 个节点
# 对于完全二叉树,若从上至下,从左到右编号，则编号为 i 的节点， 其左孩子编号必为 2i,其右孩子编号必为 2i + 1；其双亲编号必为 i/2.

# 完全二叉树(complete binary tree) : 除了最底层除外，其他所有层的节点都达到最大化(2)
# 若设二叉树的深度为h，除第 h 层外，其它各层 (1～h-1) 的结点数都达到最大个数，
# 第 h 层所有的结点都连续集中在最左边，这就是完全二叉树。

# 满二叉树(Full binary tree) : 所有层必须达到最大化

# 二叉排序树(binary search tree): 对于任何一个节点来说，它的左节点的值一定比它小， 它的右节点的值一定比它大
#             8
#           /   \
#          3     10
#         / \      \
#        1   6     14
#           / \    /
#          4   7  13
#  二分查找

# 常见的树的应用场景 ： html，编写这些东西的解析器的时候； 路由协议就是使用了树的算法； mysql数据库索引；文件系统的目录结构；


# 树的节点：
class TreeNode(object):

    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

# 二叉树树的实现:
class BinaryTree(object):

    def __init__(self):
        self.root = None

    def add(self, item):  # 添加新的 节点
        # 使用 广度优先遍历： 树结构横向遍历; 层次遍历添加节点
        node = TreeNode(item)  # 创建一个新的 node 节点
        if self.root == None:  # 如果根节点为空
            self.root = node   # 根节点指向 新的node
            return
        count = 0
        queue = [self.root]    # 创建一个 queue 列表，把根节点放入；  使用队列的形式遍历整个树结构；
        while queue:           # 遍历循环 直到 queue 列表为空; 空列表 return False； 列表不为空时，return True
            current_node = queue.pop(0)  # 删除 queue 列表中的第一个节点，命名一个current(当前) 节点 指向 那个被删除的节点
            if current_node.left == None:  # 如果 current 节点的 左节点(左孩子) 为空
                current_node.left = node   # 左节点 指向 新添加的 node
                return
            else:
                queue.append(current_node.left)  # 如果当前节点 的 左节点 不为空，把那个左节点放入queue列表中
            if current_node.right == None:  # 如果 current 节点的 右节点(右孩子) 为空
                current_node.right = node   # 右节点 指向 新添加的 node
                return
            else:
                queue.append(current_node.right)



    def breadth_travel(self):
        # 广度遍历(层次遍历)
        if self.root == None:  # 如果 根节点为空
            return             # 跳出
        queue = [self.root]    # 建立 queue 列表， 里面 包含 根节点
        while queue:           # 遍历循环 直到 queue 列表为空; 空列表 return False ；列表不为空时，return True
            current_node = queue.pop(0)  # 删除 queue 列表中的第一个节点，命名一个current(当前) 节点 指向 那个被删除的节点
            print(current_node.item, end=" ")      # print current 节点的 值
            if current_node.left != None:          # 如果 current 节点的 左节点(左孩子) 不为空
                queue.append(current_node.left)    # 将 current 节点的 左节点(左孩子) 添加到 queue列表的尾部
            if current_node.right !=  None:        # 如果 current 节点的 右节点(右孩子) 不为空
                queue.append(current_node.right)   # 将 current 节点的 右节点(右孩子) 添加到 queue列表的尾部


    def perOreder(self, node):  # 先序遍历  根 左 右
        if node == None:
            return
        print(node.item, end=" ")
        self.perOreder(node.left)
        self.perOreder(node.right)

    def inOrder(self, node): # 中序遍历  左 根 右
        if node == None:
            return
        self.inOrder(node.left)
        print(node.item, end=" ")
        self.inOrder(node.right)

    def postOrder(self, node): # 后续遍历 左 右 根
        if node == None:
            return
        self.postOrder(node.left)
        self.postOrder(node.right)
        print(node.item, end=" ")

    def leafSum(self, node):  # 求叶子节点的和  O(n) ； 树里的时间复杂度 都是O(n)；因为每个节点仅被访问一次
        if node == None:  # 如果node 节点为空
            return 0      # 返回 0
        if node.left == None and node.right == None:  # 如果左边是空，右边是空，说明这是个叶子节点
            return node.item                          # 返回叶子节点的值
        return self.leafSum(node.left) + self.leafSum(node.right)  # 返回叶子节点的加和

    def maxDepth(self, node):  # 求树的最大深度   O(n)  / 这题是用最大高度 ； 深度是对于节点而言，高度是对于子树或树而言
        if node == None:
            return 0
        if node.left == None and node.right == None: # 如果左边是空，右边是空，说明这是个叶子节点
            return 1  # 返回 1
        return max(self.maxDepth(node.left), self.maxDepth(node.right)) + 1  # 每递归一次，深度 + 1




if __name__ == "__main__":
    tree = BinaryTree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)

    tree.breadth_travel()    # 广度层次遍历 output： 0 1 2 3 4 5 6 7 8 9
    print("")
    tree.perOreder(tree.root)   #  根 左 右 output: 0 1 3 7 8 4 9 2 5 6
    print("")
    tree.inOrder(tree.root)     #  左 根 右 output: 7 3 8 1 9 4 0 5 2 6
    print("")
    tree.postOrder(tree.root)   #  左 右 根 output: 7 8 3 9 4 1 5 6 2 0
    print("")
    print(tree.leafSum(tree.root))  # output: 35
    print("")
    print(tree.maxDepth(tree.root))


    def reverse(x):
        """
        :type x: int
        :rtype: int
        """
        str1 = str(x)
        sign = 1
        start = 0
        j = 1

        print(str1)

        if str1[0] == "-":
            start = 1
            sign = -1

        num = ""
        for i in range(start, len(str1)):
            num += str1[- j]
            print("num", num)
            j += 1

        return sign * int(num)

n = 1234567
print(reverse(n))











