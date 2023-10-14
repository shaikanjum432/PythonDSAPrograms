class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data
    
class SingleLinkedList:
    def __init__(self):
        self.head = None
 
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return '-->'.join(nodes)
    
l1 = SingleLinkedList()
print(l1)
n1 = Node("A")
l1.head = n1
print(l1)
n2 = Node('n')
n3 = Node('j')
n4 = Node('u')  
n1.next = n2
n2.next = n3
n3.next = n4
print(l1)  

