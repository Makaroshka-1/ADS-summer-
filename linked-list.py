class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
 
class Linked_list:

    def __init__(self):
        self.head = None
        self.size = 0
    
    def isEmpty(self):
        return self.head == None
    
    def push_front(self,value):

        new_node=Node(value)

        if self.isEmpty():
            self.head  = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size +=1

    def push_back(self,value):
        new_node = Node(value)

        if self.isEmpty():
            self.head = new_node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next= new_node
        self.size +=1

    def get_head(self):
        return self.head.data      

    def get_size(self):
        return self.size
    
    def pop_head(self,):
        if self.isEmpty():
            return -1
        else: 
            self.head = self.head.next            
        self.size -=1        


new_list = Linked_list()
new_list.push_front(5)
new_list.push_front(6)
new_list.push_back(4)
print(new_list.get_head())
print(new_list.get_size())
new_list.pop_head()
print(new_list.get_size())
print(new_list.get_head())



    
    


