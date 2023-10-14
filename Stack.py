class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __repr__(self):
        return str(self.value)

class LinkedList(object):
    def __init__(self, head = None):
        self.head = head
    
    def append(self,new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
    
    def insert_first(self, new_element):
        new_element.next = self.head
        self.head = new_element
    
    def delete_first(self):
        deleted =  self.head
        if self.head:
            self.head = self.head.next
            deleted.next = None
        return deleted

class Stack(object):
    def __init__(self, top = None):
        self.ll = LinkedList(top)
    
    def push(self,new_element):
        self.ll.insert_first(new_element)
    
    def pop(self):
        if self.ll.head:
            return self.ll.delete_first()
        else:
            return None
        
#Test cases
e1 = Element(100)
e2 = Element(200)
e3 = Element(300)
e4 = Element(400)

#Start setting up Stack
st = Stack(e1)

#test functionality
st.push(e2)
st.push(e3)
print (st.pop().value)
print (st.pop().value)
print (st.pop().value)
st.push(e4)
print (st.pop().value)