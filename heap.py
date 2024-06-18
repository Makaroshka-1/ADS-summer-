class MinHeap:
    def __init__(self,arr=None):
        self.heap = []
        self.size = 0
        if type(arr) == list:
            self.heap = arr.copy()

    def get_parent(self,i):
        return (i-1)//2
    
    def get_leftchild(self,i):
        return 2*i+1
    
    def get_rightchild(self,i):
        return 2*i+2
    
    def isEmpty(self):
        return self.size == 0
    
    def get_min(self):
        if self.isEmpty():
            return -1
        return self.heap[0]
    
    def swap(self,i,j):
        self.heap[i],self.heap[j]=self.heap[j],self.heap[i]

    def shift_up(self,i):
        while i > 0 and self.heap[i-1] < self.heap[self.get_parent(i)]:
            self.swap(i, self.get_parent(i))
            i = self.get_parent(i)
    
    def shift_down(self,i):
        while self.get_leftchild(i) < self.size:
            smaller_child = self.get_leftchild(i)
            if self.get_rightchild(i) < self.size and self.heap[self.get_rightchild(i)] < self.heap[smaller_child]:
                smaller_child = self.get_rightchild(i)

            if self.heap[i] > self.heap[smaller_child]:
                 self.swap(i, smaller_child)
            else:
                break
            i = smaller_child
    
    def insert(self,value):
        self.size+=1
        self.heap.append(value)
        self.shift_up(self.size)
    
    def update_by_index(self, index, new_value):
        old = self.heap[index]
        self.heap[index]=new_value
        if new_value<old:
            self.shift_up(index)
        else:
            self.shift_down(index)

    def remove_min(self):
        if self.isEmpty():
            return -1
        else:
            min_element = self.heap[0]
            self.heap[0]=self.heap[self.size-1]
            self.size-=1
            self.shift_down(0)
            return min_element

class PriorityQueue:

    def __init__(self):
        self.queue = MinHeap

    def isEmpty(self):
        return len(self.queue.heap)==0
    
    def enqueue(self, value):
        self.queue.insert(value)

    def dequeue(self):
        self.queue.remove_min()

    def peek(self):
        return self.queue.get_min()

    def change_priority(self,index, new):
        self.queue.update_by_index(index, new)



def heapsort(arr):
    heap = MinHeap(arr)
    for i in range(len(heap.heap)):
        print(heap.remove_min(), sep=' ')

Heap = MinHeap()
Heap.insert(2)
Heap.insert(3)
Heap.insert(4)
Heap.insert(5)
Heap.insert(6)
Heap.isEmpty()
print(Heap.get_min())
arr = [ 1,2,4,5,6,7,8,9,10]
heapsort(arr)


