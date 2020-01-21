# 1/19/2020
# Stack  是一种容器，可以存入数据元素，访问元素，特点在于只能运行在容器的一端(top)进行加入数据(push)和输出数据(pop)的运算。
# 没有了位置概念，保证任何时候都可以访问，删除元素都是此前最后存入的的那个元素，确定了一种默认的访问顺序。
# 由于栈数据结构只允许在一端进行操作，因而按照后进先出的原理运作 (Last in, First out)
# 栈：描述的数据如何操作，  线性表：描述的是数据如何存放

# Queue 队列： 是只允许在一端进行插入操作，而在另一端进行删除操作的线性表。 队列是一种先进先出的线性表(First in, First out)，
# 允许插入的一端为队尾，允许删除的一端为队头。队列不允许在中间部位进行操作！假设队列是 q =(a1, a2, ... an),
# 那么a1就是队头元素,而an是队尾元素，这样我们就可以删除时，总是从a1开始, 而插入时，总是在队列最后，
# 这也比较符合我们通常生活中的习惯，排在第一个的优先出列，最后来的当然排在队伍最后.
# 队列的应用 ： BFS 广度优先搜索 一定是用队列实现的

# 栈 可以用List实现，也可以用链表实现
# Stack 的 操作


class Stack(object):

    def __init__(self):
        self.list = []  # 构造一个空列表

    def push(self, item):
        # 添加一个新的元素到栈顶
        self.list.append(item)

    def pop(self):
        # 弹出栈顶元素
        return self.list.pop()

    def peek(self):
        # 返回栈顶元素
        if self.list:
            return self.list[-1]
        else:
            return None

    def print_list(self):
        if self.is_empty():
            print("empty list")
            return
        for i in self.list:
            print(i, end=" ")
        print("")

    def is_empty(self):
        # 判断栈是否为空
        return self.list == []

    def size(self):
        # 返回栈的元素个数
        return len(self.list)


# Queue linkedList 操作

class Node(object):

    def __init__(self, item):
        self.item = item
        self.next = None


class Queue(object):

    def __init__(self):
        self.dummy = Node(-1)
        self.tail = self.dummy

    def enqueue(self, item):
        node = Node(item)
        self.tail.next = node
        self.tail = node

    def dequeue(self):
        self.dummy.next = self.dummy.next.next
        if self.dummy.next == None:
            self.tail = self.dummy


    def is_empty(self):
        return self.dummy.next == None

    def print_Queue(self):
        if self.is_empty():
            print("is empty")
        else:
            current = self.dummy.next
            while current != None:
                print(current.item, end=" ")
                current = current.next
            print("")

    def length(self):
        if self.is_empty():
            return 0
        else:
            count = 0
            current = self.dummy.next
            while current != None:
                count += 1
                current = current.next
            return count



# 内置 Queue 函数
# 队列的应用 ： BFS 广度优先搜索 一定是用队列实现的
import queue as Queue1

queue = Queue1.Queue()  # 使用 Queue 操作  （）括号内可以写 maxsize=  ； 不写的话 和 小于1 的 就是默认无限长

queue.put(10)  # 等价于 enqueue 操作，在队尾插入一个元素。如果队列是满的，该线程会阻塞(等待),
               #  直到空出一个位置来，让后在队尾放入元素
queue.put(20)
queue.put(30)

# get()方法从队头删除并返回一个项目，队列为空默认为阻塞线程(等待)，直到所有元素放入到队列之后，将其取走。
print(queue.get())  # 等价于 dequeue  从头部拿出元素  output: 10
print(queue.get())  # 等价于 dequeue  从头部拿出元素  output: 20
print(queue.get())  # 等价于 dequeue  从头部拿出元素  output: 30
print("=============================================")




if __name__ == "__main__":
    stack_obj = Stack()
    print(stack_obj.is_empty()) # check stack list is empty or not ; output: True
    stack_obj.push(1)           # push item 1 into stack list
    stack_obj.push(2)           # push item 2 into stack list
    stack_obj.push(3)           # push item 3 into stack list
    stack_obj.push(4)           # push item 4 into stack list
    stack_obj.print_list()      # print stack list  output： 1， 2， 3， 4
    print(stack_obj.pop())      # pop the last item in stack list  output: 4
    print(stack_obj.pop())      # pop the last item in stack list  output: 3
    stack_obj.print_list()      # print stack list  output： 1， 2
    print(stack_obj.is_empty()) # check stack list is empty or not ; output: False
    print(stack_obj.size())     # print stack list length; output: 2
    stack_obj.push(5)           # push item 5 into stack list
    print(stack_obj.peek())     # print the top of stack list; output: 5
    print("=============================================")

    queue_obj = Queue()
    print(queue_obj.is_empty())     # output: True
    print(queue_obj.length())       # output: 0
    queue_obj.enqueue(1)            # enqueue(append)  item(1) into queue
    queue_obj.enqueue(2)            # enqueue(append)  item(2) into queue
    queue_obj.enqueue(3)            # enqueue(append)  item(3) into queue
    queue_obj.enqueue(4)            # enqueue(append)  item(4) into queue
    queue_obj.print_Queue()         # print Queue; output: 1, 2, 3, 4
    print(queue_obj.is_empty())     # output: False
    print(queue_obj.length())       # print length of the Queue: output: 4
    print("=============================================")

    queue_obj.dequeue()             # dequeue first item in the queue
    queue_obj.print_Queue()      # output: 2, 3, 4
    queue_obj.dequeue()             # dequeue first item in the queue
    queue_obj.print_Queue()      # output: 3, 4
    queue_obj.enqueue(5)            # enqueue(append)  item(5) into queue
    queue_obj.print_Queue()      # output: 3, 4, 5
    queue_obj.dequeue()             # dequeue first item in the queue
    queue_obj.print_Queue()      # output: 4, 5
    queue_obj.dequeue()             # dequeue first item in the queue
    queue_obj.print_Queue()      # output: 5
    queue_obj.dequeue()             # dequeue first item in the queue
    queue_obj.print_Queue()      # output: is empty
    print("=============================================")
