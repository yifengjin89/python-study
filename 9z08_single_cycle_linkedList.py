# 1/18/2020
# single_cycle_linkedList

class Node(object):  # 节点类 ； 构造节点 node
    # 节点   需要属性 ==> node = Node（10）  需要 item 和 指向下一个区域的空间 next
    def __init__(self, item):
        self.item = item  # node 属性 ==》 item ； 数据；                   node = Node（10）
        self.next = None  # node 属性 ==》 next ； 链接区；下一个节点的位置； node.next  ；
        # node1.next = node2  等号 等价于 把两个节点串联起来  ； node1.next 区域指向 node2 这个节点


class Single_cycle_LinkedList(object):  # 链表类 ： 单向循环链表

    def __init__(self, node=None):  # 把第一个构造的节点 默认成头节点， 如果不传头节点， 默认为空链表
        self.head = node
        if node:
            node.next = self.head

    def is_empty(self):
        # 判断链表是否为空
        return self.head == None

    def length(self):
        # 判断链表长度
        current = self.head
        if self.is_empty():
            return 0
        count = 1
        while current.next != self.head:
            count += 1
            current = current.next  # 当前的节点 指向 下一个节点

        return count

    def travel(self):
        # 遍历整个链表
        current = self.head
        if self.is_empty():
            print("is empty LinkedList")
            return
        while current.next != self.head:
            print(current.item, end=" ")  # 打印 不换行
            current = current.next  # 当前的节点 指向 下一个节点
        # 退出循环，current指向尾节点， 但尾结点未打印
        print(current.item)
        print("")  # 换行

    def add(self, item):
        # 从链表头部添加元素  头插法   time complexity O(1)  <  List的头插法 O(n)
        node = Node(item)  # 先创造一个想要添加的节点
        if self.is_empty():  # 如果是空链表
            self.head = node  # 头节点指向 新插入的node 节点
            node.next = self.head  # node 节点 指向 头节点
        else:
            current = self.head  # current 指向 头节点
            while current.next != self.head:  # 循环 直到 走到尾结点
                current = current.next       # current 指向尾结点
            node.next = self.head  # 要插入的节点的next区域 指向 原来第一个节点
            self.head = node  # 把头节点 指向 新添加的节点
            current.next = self.head  # 尾结点 指向 新插入得的node(这时已经是头节点了头节点了)


    def append(self, item):
        # 从链表尾部添加元素   尾插法    time complexity O(n)  >  List的尾插法 O(1)
        node = Node(item)  # 先创造一个想要添加的节点
        if self.is_empty():  # 如果是空链表
            self.head = node  # 头节点 指向 要添加的节点
            node.next = self.head  # 新插入的节点 指向 头节点
        else:
            current = self.head   # current 指向 头节点
            while current.next != self.head:  # 一直走到尾结点
                current = current.next  # current 指向尾结点

            current.next = node  # 尾结点的next区域 指向 要添加的新节点
            node.next = self.head  # 新插入的node 指向 头节点


    def insert(self, position, item):
        # 从指定位置添加元素          #  time complexity O(n)  ==  List的中间插入法 O(n)
        if position <= 0:  # 如果position <= 0, 就使用头插法
            self.add(item)
        elif position > self.length() - 1:  # 如果position > 链表长度 -1， 就使用尾插法
            self.append(item)
        else:
            node = Node(item)  # 创造一个节点
            pre = self.head  # 创造一个 pre， 指向头节点
            count = 0
            while count < position - 1:  # 计数遍历； pre 现在是头节点，
                # 每次遍历， pre 就到达下一个节点并且在到达要插入的position之前一个节点停止
                count += 1
                pre = pre.next  # 让pre 到达 position - 1 的节点位置；当循环结束后，pre 指向 position-1 节点的位置

            node.next = pre.next  # 让要插入的新节点的next区域 指向 pre.next区域  就是原来position上的节点
            pre.next = node  # 让要插入position的之前的节点的 next 区域 (pre.next) 指向 新节点

    def remove(self, item):
        # 删除节点
        if self.is_empty():
            return
        pre = None  # 创造一个pre 指向 None
        current = self.head  # 创造一个current， 指向头节点
        while current.next != self.head:  # 遍历整个链表
            if current.item == item:  # 判断 current 节点的item 等于 要删除的元素
                if current == self.head:  # 判断 current 节点 是否 指向 头节点
                    # 头节点的情况 ； 在头部删除
                    # 找尾结点
                    tail = self.head
                    while tail.next != self.head:
                        tail = tail.next

                    self.head = current.next
                    tail.next = self.head
                else:
                    # 中间节点的情况   在中间删除
                    pre.next = current.next  # 反之， pre 节点的 next 区域 指向  current 节点的 next 区域
                return  # 已经删除了元素， 跳出循环
            else:
                pre = current  # pre 节点 指向 current 节点 ；等于每次往后移一位
                current = current.next  # current 节点 指向 下一个节点 ；  等于每次往后移一位
        # 跳出循环， 到达尾结点 ；  在尾部删除
        if current.item == item:
            if current == self.head:  # 链表只有一个节点
                self.head = None
            else:
                pre.next = self.head




    def search(self, item):
        # 查找节点是否存在         # 访问元素  time complexity O(n)  >  List的中间插入法 O(1)
        if self.is_empty():
            return False
        current = self.head
        while current != None:
            if current.item == item:
                return True
            else:
                current = current.next
        if current.item == item:
            return True
        return False


if __name__ == "__main__":
    linkList_obj = Single_cycle_LinkedList()
    print(linkList_obj.is_empty())  # 判断是否为空链表  output：True
    print(linkList_obj.length())  # 判断链表长度     output： 0
    linkList_obj.travel()
    print("=====================================")


    linkList_obj.append(2)  # 尾插入 元素 2
    linkList_obj.add(100)  # 头插入 元素 100
    linkList_obj.append(3)  # 尾插入 元素 3
    linkList_obj.add(200)  # 头插入 元素 200
    linkList_obj.travel()  # output: 200, 100, 2, 3
    linkList_obj.insert(-1, 20)  # position <= 0, 相当于在头部插入元素 20
    linkList_obj.insert(2, 60)  # position > 0, 相当于在下标 2 插入元素 60
    linkList_obj.insert(8, 90)  # position > 链表长度, 相当于在尾部插入元素 90
    linkList_obj.travel()  # output:  20， 200， 60， 100， 2， 3， 90
    linkList_obj.remove(20)   # 删除元素 20
    linkList_obj.travel()     # output ：200， 60， 100， 2， 3， 90
    linkList_obj.remove(90)   # 删除元素 90
    linkList_obj.travel()     # output： 200， 60， 100， 2， 3
    linkList_obj.remove(100)  # 删除元素 100
    linkList_obj.travel()     # output: 200, 60, 2, 3
    print("=====================================")
'''

   

  
    print("=====================================")

    linkList_obj.insert(10, 30)  # position > 链表的长度，相当于在尾部插入元素 30
    linkList_obj.travel()  # output: 20, 100, 1, 2, 3, 30
    print("=====================================")

    linkList_obj.insert(2, 200)  # position = 2； 在下标为2 的位置 插入元素 200
    linkList_obj.travel()  # output: 20, 100, 200, 1, 2, 3, 30
    print("=====================================")

    linkList_obj.append(4)
    linkList_obj.append(5)
    linkList_obj.append(6)
    print(linkList_obj.is_empty())  # 判断是否为空链表  output：False
    print(linkList_obj.length())  # 判断链表长度     output： 10
    linkList_obj.travel()  # 遍历打印所有链表内的元素  output: 20, 100, 200, 1, 2, 3, 30, 4, 5, 6
    print("=====================================")

    print(linkList_obj.search(100))  # output: True
    linkList_obj.remove(200)  # output ： 20 100 1 2 3 30 4 5 6
    linkList_obj.travel()
    linkList_obj.remove(20)  # output ： 100 1 2 3 30 4 5 6
    linkList_obj.travel()
    linkList_obj.remove(6)  # output ：  100 1 2 3 30 4 5
    linkList_obj.travel()
    print("=====================================")

'''


