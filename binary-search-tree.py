class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data 

def insert(node, data):
    if node is None:
        return Node(data)
    else:
        if data < node.data:
            node.left = insert(node.left, data)
        elif data > node.data:
            node.right = insert(node.right, data)
    return node
        
def search(node, target):
    if node is None:
        return None 
    elif node.data == target:
        return node
    elif target < node.data:
        return search(node.left, target)
    else:
        return search(node.right, target)
            
