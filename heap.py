class MinHeap:
    def __init__(self, arr=None):
        self.heap = []
        self.size = 0
        if type(arr) == list:
            self.heap = arr.copy()
            self.size = len(arr)
            self.build_heap()
    
    def build_heap(self):
        for i in range((self.size // 2) - 1, -1, -1):
            self.shift_down(i)

    def get_parent_index(self, i):
        return (i - 1) // 2
    
    def get_leftchild_index(self, i):
        return 2 * i + 1
    
    def get_rightchild_index(self, i):
        return 2 * i + 2
    
    def isEmpty(self):
        return len(self.heap) == 0
    
    def get_min(self):
        if self.isEmpty():
            return -1
        return self.heap[0]
    
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def shift_up(self, i):
        while i > 0 and self.heap[i] < self.heap[self.get_parent_index(i)]:
            parent_index = self.get_parent_index(i)
            self.swap(i, parent_index)
            i = parent_index
    
    def shift_down(self, i):
        while self.get_leftchild_index(i) < self.size:
            left = self.get_leftchild_index(i)
            right = self.get_rightchild_index(i)
            smallest = left

            if right < self.size and self.heap[right] < self.heap[left]:
                smallest = right

            if self.heap[i] > self.heap[smallest]:
                self.swap(i, smallest)
                i = smallest
            else:
                break
    
    def insert(self, value):
        self.size += 1
        self.heap.append(value)
        self.shift_up(self.size - 1)
    
    def update_by_index(self, index, new_value):
        old = self.heap[index]
        self.heap[index] = new_value
        if new_value < old:
            self.shift_up(index)
        else:
            self.shift_down(index)

    def remove_min(self):
        if self.isEmpty():
            return -1
        min_element = self.heap[0]
        self.heap[0] = self.heap[self.size - 1]
        self.size -= 1
        self.heap.pop()
        self.shift_down(0)
        return min_element

class PriorityQueue:
    def __init__(self):
        self.queue = MinHeap()

    def isEmpty(self):
        return self.queue.isEmpty()
    
    def enqueue(self, value):
        self.queue.insert(value)

    def dequeue(self):
        return self.queue.remove_min()

    def peek(self):
        return self.queue.get_min()

    def change_priority(self, index, new_value):
        self.queue.update_by_index(index, new_value)

def heapsort(arr):
    Heap = MinHeap(arr)
    sorted_array = []
    while not Heap.isEmpty():
        sorted_array.append(Heap.remove_min())
    return sorted_array

Heap = MinHeap()
Heap.insert(2)
Heap.insert(3)
Heap.insert(4)
Heap.insert(5)
Heap.insert(6)
print(Heap.isEmpty())  
print(Heap.get_min())  
print(heapsort(Heap.heap))  
