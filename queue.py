class Node:
    
    def __init__(self,data):
        self.data=data
        self.next=None

class Queue:

    def __init__(self):
        self.front=self.rear=None

    def isEmpty(self):
        return self.front==None
    
    def enqueue(self,item):
        temp = Node(item)
        if self.rear==None:
            self.front=self.rear=temp
            return
        self.rear.next=temp
        self.rear = temp

    def dequeue(self):
        if (self.isEmpty()): 
            return 
        temp = self.front
        self.front=temp.next
        if (self.front == None):
            self.rear = None
    def peek_front(self):
        return self.front.data
    def peek_back(self):
        return self.rear.data
Queue = Queue()
Queue.enqueue(1)
Queue.enqueue(2)
Queue.enqueue(3)
Queue.enqueue(4)
print(Queue.peek_back())
print(Queue.peek_front())


 # type: ignore