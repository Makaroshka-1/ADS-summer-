class Node:
    
    def __init__(self,data):
        self.data=data
        self.next=None

class Queue:

    def __init__(self):
        self.front=self.back=None

    def isEmpty(self):
        return self.front==None
    
    def enqueue(self,item):
        temp = Node(item)
        if self.back==None:
            self.front=self.back=temp
            return
        self.back.next = None
        self.back = temp

    def dequeue(self):
        if (self.isEmpty()): 
            return 
        temp = self.front
        self.front=temp.next
        if (self.front == None):
            self.back = None
    def peek_front(self):
        return self.front.data
    def peek_back(self):
        return self.back.data
Queue = Queue()
Queue.enqueue(1)
Queue.enqueue(2)
Queue.enqueue(3)
Queue.enqueue(4)
print(Queue.peek_back())
print(Queue.peek_front())

  # type: ignore