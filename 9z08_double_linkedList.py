# 1/17/2020
# Double LinkedList 双链表

class Node(object):

    def __init__(self, item):
        self.item = item
        self.prev = None
        self.next = None   # node 属性 ==》 next ； 链接区；下一个节点的位置； node.next  ；
        # node1.next = node2  等号 等价于 把两个节点串联起来  ； node1.next 区域指向 node2 这个节点
        # 所有的 next 区域 和 prev 区域 指向的 都是 节点！， 并不指向 节点的next 区域 或者 prev 区域


class DoubleLinkedList(object):

    def __init__(self, node=None):
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
            current = current.next  # 当前的节点 指向 下一个节点

        return count

    def travel(self):
        # 遍历整个链表
        current = self.head
        while current != None:
            print(current.item, end=" ")  # 打印 不换行
            current = current.next  # 当前的节点 指向 下一个节点
        print("")  # 换行

    def add(self, item):
        # 从链表头部添加元素  头插法   time complexity O(1)  <  List的头插法 O(n)
        node = Node(item)  # 先创造一个想要添加的节点
        if self.is_empty():  # 如果是空链表
            self.head = node  # 直接指向要添加的节点
        else:
            node.next = self.head  # 新插入的 node 节点 的next区域 指向 头节点   node.next ==> 连接 head 节点
            self.head = node  # 头节点 指向 新插入的 node 节点
            node.next.prev = node  # 被 新节点 node  插入的 节点，也就是第二个节点的 prev区域 指向 新插入的 node 节点
                                 ### 双链表 添加操作##   #  第二个节点 node.next.prev 区域 连接 node 节点(head)节点


    def append(self, item):
        # 从链表尾部添加元素   尾插法    time complexity O(n)  >  List的尾插法 O(1)
        node = Node(item)  # 先创造一个想要添加的节点
        if self.is_empty():  # 如果是空链表
            self.head = node  # 直接指向要添加的节点
        else:
            current = self.head
            while current.next != None:  # 一直走到尾结点
                current = current.next

            current.next = node  # 尾结点的next区域 指向 要添加的新节点
            node.prev = current  ### 双链表 添加操作##  要添加的 node.prev区域 指向 current 节点

    def insert(self, position, item):
        # 从指定位置添加元素          #  time complexity O(n)  ==  List的中间插入法 O(n)
        if position <= 0:  # 如果position <= 0, 就使用头插法
            self.add(item)
        elif position > self.length() - 1:  # 如果position > 链表长度 -1， 就使用尾插法
            self.append(item)
        else:
            node = Node(item)  # 创造一个节点
            ###  pre = self.head  # 创造一个 pre， 指向头节点
            current = self.head   # 创造一个 current， 指向头节点
            count = 0
            while count < position:  # 计数遍历； pre 现在是头节点，
                # 每次遍历， pre 就到达下一个节点并且在到达要插入的position之前一个节点停止
                count += 1
                #pre = pre.next  # 让pre 到达 position - 1 的节点位置；当循环结束后，pre 指向 position-1 节点的位置
                current = current.next  # 让current到达 position 的节点位置;当循环结束后，current 指向 position 节点的位置.

            node.next = current  # 让要插入的新节点的next区域 指向 current 区域  就是原来position上的节点
            node.prev = current.prev  # 让要插入的新节点的prev区域 指向 current 之前一个的节点prev 区域
            current.prev.next = node  # 让 current 原来前一个节点的next区域 指向 新插入的 node 节点
            current.prev = node      # 让 current 的 prev 区域 指向 新插入的 node 节点


    def remove(self, item):
        # 删除节点
        # pre = None  # 创造一个pre 指向 None
        current = self.head  # 创造一个current， 指向头节点
        while current != None:  # 遍历整个链表
            if current.item == item:  # 判断 current 节点的item 等于 要删除的元素
                if current == self.head:  # 判断 current 节点 是否 指向 头节点；是否只有一个节点在链表中
                    self.head = current.next  # 如果是，就说明只有一个节点在链表里；头节点 指向 None； 那就删除了
                    if current.next:   # 如果 current.next 不是 None
                        current.next.prev = None   # current 节点的下一个节点 的 prev 区域 指向 None； 就是删除了
                else:
                    current.prev.next = current.next  # current的 之前一个节点的next区域 指向 current 下一个的 节点
                    if current.next:
                        current.next.prev = current.prev  # current的 next(下一个)节点的 prev 区域 指向 current之前的一个的节点
                break  # 已经删除了元素， 跳出循环
            else:
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
    linkList_obj = DoubleLinkedList()
    print(linkList_obj.is_empty())  # 判断是否为空链表  output：True
    print(linkList_obj.length())  # 判断链表长度     output： 0
    print("=====================================")

    linkList_obj.add(100)   # 头插入 元素 100
    print(linkList_obj.is_empty())  # 判断是否为空链表  output：False
    print(linkList_obj.length())  # 判断链表长度     output： 1
    print("=====================================")

    linkList_obj.add(200)  # 头插入 元素 200
    linkList_obj.append(500)
    linkList_obj.travel()  # output: 200, 100, 500
    linkList_obj.add(300)  # 头插入 元素 300
    linkList_obj.append(600)
    linkList_obj.travel()  # output: 300, 200, 100, 500, 600
    linkList_obj.insert(3, 800)   # 在下标3的位置 插入 元素 800
    linkList_obj.travel()  # output: 300, 200, 100, 800, 500, 600
    linkList_obj.remove(200)
    linkList_obj.travel()  # output: 300, 100, 800, 500, 600
    linkList_obj.remove(300)
    linkList_obj.travel()  # output: 100, 800, 500, 600
    linkList_obj.remove(600)
    linkList_obj.travel()  # output: 100, 800, 500
    linkList_obj.insert(-1, 600)  # 在下标-1的位置 插入 元素 600
    linkList_obj.travel()  # output: 600, 100, 800, 500
    print("=====================================")
