# 1/16/2020

# 变量的本质
a = 10
b = 20
a, b = b, a

# 在python中，一切皆对象；  变量 a 保存的并不是 10 这个值， 而是保存 10 这个对象 的地址
# 变量 a 仅仅是个名字，或者说是引用，a 真正代表的是一块内存，这个内存里保存是地址，这个地址指向什么，也就代表a这个变量是什么
# ；这就是python和别的语言的区别
# node1： item = 10; next = node2
# node2:  item = 20; next
# 这里 node1 的 next = node2 并不是指在node1的节点数据区域中把node2 放进来了；而是表示next 这个标签指向了node2这个数据区域
# next区域存储了node2 的地址，并不是 node.next 等于 node2

# linkedList  链表
# 链表特点：对分散的存储空间能达到充分的利用，能存储大型数据，有时候内存无法分配出大型连续空间给大型数据，这时候链表就派上用场了。
# 但是缺点在于会有额外的空间开销，多占内存，存取元素的时候无法达到O(1)的效果，只能从头往后去遍历。
# 时间复杂度  访问元素： O(n) ； 头部插入/删除 O(1);  尾部插入/删除O(n)  ;  在中间插入/删除 O(n)
# 对于链表来说 插入O(n)操作耗时是在遍历上

# List特点：优点在于存取元素的时候可以通过O(1)的方式一次性定位，但是缺点在于存储空间必须要是连续的，一旦有动态的改变，
# 整个存储区都要改变。当保存大型数据的时候，如果没有这么多的连续存储空间，List就达不到要求了
# 时间复杂度  访问元素： O(1) ； 头部插入/删除 O(n);  尾部插入/删除O(1)  ;  在中间插入/删除 O(n)
# 对于List来说 插入O(n)操作耗时是在数据搬迁上


class Node(object):  # 节点类 ； 构造节点 node
     # 节点   需要属性 ==> node = Node（10）  需要 item 和 指向下一个区域的空间
    def __init__(self, item):
        self.item = item     # node 属性 ==》 item ； 数据；                   node = Node（10）
        self.next = None     # node 属性 ==》 next ； 链接区；下一个节点的位置； node.next  ；
        # node1.next = node2  等号 等价于 把两个节点串联起来  ； node1.next 区域指向 node2 这个节点


class LinkedList(object):  # 链表类 ： 单链表

    def __init__(self, node=None):  # 把第一个构造的节点 默认成头节点， 如果不传头节点， 默认为空链表
        self.head = node


    def is_empty(self):
        # 判断链表是否为空
        return self.head == None

    def length(self):
        # 判断链表长度
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.next      # 当前的节点 指向 下一个节点

        return count

    def travel(self):
        # 遍历整个链表
        current = self.head
        while current != None:
            print(current.item, end=" ")  # 打印 不换行
            current = current.next    # 当前的节点 指向 下一个节点
        print("")  # 换行


    def add(self, item):
        # 从链表头部添加元素  头插法   time complexity O(1)  <  List的头插法 O(n)
        node = Node(item)         # 先创造一个想要添加的节点
        node.next = self.head     # 要插入的节点的next区域 指向 原来第一个节点
        self.head = node          # 把头节点 指向 新添加的节点



    def append(self, item):
        # 从链表尾部添加元素   尾插法    time complexity O(n)  >  List的尾插法 O(1)
        node = Node(item)      # 先创造一个想要添加的节点
        if self.is_empty():    # 如果是空链表
            self.head = node  # 直接指向要添加的节点
        else:
            current = self.head
            while current.next != None:  # 一直走到尾结点
                current = current.next

            current.next = node  # 尾结点的next区域 指向 要添加的新节点


    def insert(self, position, item):
        # 从指定位置添加元素          #  time complexity O(n)  ==  List的中间插入法 O(n)
        if position <= 0:         # 如果position <= 0, 就使用头插法
            self.add(item)
        elif position > self.length() - 1:  # 如果position > 链表长度 -1， 就使用尾插法
            self.append(item)
        else:
            node = Node(item)      # 创造一个节点
            pre = self.head        # 创造一个 pre， 指向头节点
            count = 0
            while count < position - 1:  # 计数遍历； pre 现在是头节点，
                                         # 每次遍历， pre 就到达下一个节点并且在到达要插入的position之前一个节点停止
                count += 1
                pre = pre.next    # 让pre 到达 position - 1 的节点位置；当循环结束后，pre 指向 position-1 节点的位置


            node.next = pre.next   # 让要插入的新节点的next区域 指向 pre.next区域  就是原来position上的节点
            pre.next = node        # 让要插入position的之前的节点的 next 区域 (pre.next) 指向 新节点



    def remove(self, item):
        # 删除节点
        pre = None             # 创造一个pre 指向 None
        current = self.head    # 创造一个current， 指向头节点
        while current != None:        # 遍历整个链表
            if current.item == item:    # 判断 current 节点的item 等于 要删除的元素
                if current == self.head:   # 判断 current 节点 是否 指向 头节点
                    self.head = current.next  # 如果是， 头节点 指向 头节点后面一个节点
                else:
                    pre.next = current.next   # 反之， pre 节点的 next 区域 指向  current 节点的 next 区域
                break   # 已经删除了元素， 跳出循环
            else:
                pre = current      # pre 节点 指向 current 节点 ；等于每次往后移一位
                current = current.next  # current 节点 指向 下一个节点 ；  等于每次往后移一位


    def search(self, item):
        # 查找节点是否存在         # 访问元素  time complexity O(n)  >  List的中间插入法 O(1)
        current = self.head
        while current != None:
            if current.item == item:
                return True
            else:
                current = current.next
        return False





if __name__ == "__main__":
    linkList_obj = LinkedList()
    print(linkList_obj.is_empty())      # 判断是否为空链表  output：True
    print(linkList_obj.length())        # 判断链表长度     output： 0
    print("=====================================")

    linkList_obj.add(100)           # 头插入 元素 100
    linkList_obj.append(2)  # 尾插入 元素 2
    linkList_obj.append(3)          # 尾插入 元素 3
    linkList_obj.travel()           # output: 100, 1, 2, 3
    print("=====================================")

    linkList_obj.insert(-1, 20)      # position <= 0, 相当于在头部插入元素 20
    linkList_obj.travel()           # output:  20, 100, 1, 2, 3
    print("=====================================")

    linkList_obj.insert(10, 30)     # position > 链表的长度，相当于在尾部插入元素 30
    linkList_obj.travel()           # output: 20, 100, 1, 2, 3, 30
    print("=====================================")

    linkList_obj.insert(2, 200)     # position = 2； 在下标为2 的位置 插入元素 200
    linkList_obj.travel()           # output: 20, 100, 200, 1, 2, 3, 30
    print("=====================================")

    linkList_obj.append(4)
    linkList_obj.append(5)
    linkList_obj.append(6)
    print(linkList_obj.is_empty())  # 判断是否为空链表  output：False
    print(linkList_obj.length())    # 判断链表长度     output： 10
    linkList_obj.travel()           # 遍历打印所有链表内的元素  output: 20, 100, 200, 1, 2, 3, 30, 4, 5, 6
    print("=====================================")

    print(linkList_obj.search(100))  # output: True
    linkList_obj.remove(200)      # output ： 20 100 1 2 3 30 4 5 6
    linkList_obj.travel()
    linkList_obj.remove(20)       # output ： 100 1 2 3 30 4 5 6
    linkList_obj.travel()
    linkList_obj.remove(6)       # output ：  100 1 2 3 30 4 5
    linkList_obj.travel()
    print("=====================================")


    

