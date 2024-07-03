class FruitHashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, fruit, price):
        index = self.hash_function(fruit)
        if self.table[index] is None:
            self.table[index] = []
        for pair in self.table[index]:
            if pair[0] == fruit:
                pair[1] = price
                return
        self.table[index].append([fruit, price])

    def search(self, fruit):
        index = self.hash_function(fruit)
        if self.table[index] is None:
            return None
        for pair in self.table[index]:
            if pair[0] == fruit:
                return pair[1]
        return None

    def delete(self, fruit):
        index = self.hash_function(fruit)
        if self.table[index] is None:
            return False
        for i, pair in enumerate(self.table[index]):
            if pair[0] == fruit:
                self.table[index].pop(i)
                return True
        return False

def main():
    fruit_prices = FruitHashTable()
    
    fruit_prices.insert("apple", 1.5)
    fruit_prices.insert("banana", 0.75)
    fruit_prices.insert("cherry", 3.0)
    fruit_prices.insert("date", 2.0)
    
    print("Price of apple:", fruit_prices.search("apple"))  
    print("Price of banana:", fruit_prices.search("banana"))  
    print("Price of cherry:", fruit_prices.search("cherry"))  
    print("Price of date:", fruit_prices.search("date"))  
    print("Price of fig:", fruit_prices.search("fig"))  

    print("Deleting 'banana':", fruit_prices.delete("banana"))  
    print("Price of banana after deletion:", fruit_prices.search("banana"))  
 
main()
