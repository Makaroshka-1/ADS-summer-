class Node:

    def __init__(self,value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def isEmpty(self):
        if self.head == None:
            return True
        return False
    
    def push(self,value):
        if self.head == None:
            self.head = Node(value)
        else:
            newnode = Node(value)
            newnode.next=self.head
            self.head = newnode
        self.size +=1

    def pop(self):
        if self.isEmpty():
            return None
        poppednode = self.head
        self.head = self.head.next
        self.size-=1
        return poppednode.value
        

    def peek(self):
        if self.isEmpty():
            return None
        self.head.value

    def get_size(self):
        return self.size
        
Stack = Stack()
print(Stack.get_size())
Stack.push(1)
Stack.push(2)
Stack.push(5)
Stack.push(3)
print(Stack.get_size())
Stack.pop()
Stack.pop()
Stack.pop()
print(Stack.get_size())


