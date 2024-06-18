class Node:
    def __init__(self,value,):
        self.value=value
        self.next = None
        self.prev = None

class Doubly_linked_list:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def isEmpty(self):
        return self.size == 0
    
    def add_head(self,value):
        node = Node(value)
        if self.isEmpty():
            self.head=self.tail=node
        else:
            node.next = self.head
            self.head.next = node
            self.head = node
        self.size+=1


    def add_tail(self,value):
        node = Node(value)
        if self.isEmpty():
            self.head = self.tail = node
        else:
            node.prev = self.head
            self.tail.next = node 
            self.tail = node
        self.size +=1
    
    def remove_head(self):
        if self.isEmpty():
            return 
        else:
            
            self.head = self.head.next
            if self.head == None:
                self.tail = None
            else:
                self.head.prev = None
            self.size -=1
        

    def remove_tail(self):
        if self.isEmpty():
            return
        else:
            
            self.tail = self.tail.prev
            if self.tail == None:
                self.head = None
            else:
                self.tail.next=None
            self.size -=1

        
    def peek_head(self):
        if self.isEmpty():
            return -1  
        return self.head.value
    
    def peek_tail(self):
        if self.isEmpty():
            return -1
        return self.tail.value

new_list = Doubly_linked_list()
