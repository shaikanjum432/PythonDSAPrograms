"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""
class Element(object):
    def __init__(self,value):
        self.value = value
        self.next = None
    def __repr__(self):
        return str(self.value)

class LinkedList(object):
    def __init__(self, head = None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
    def get_position(self, position):
        if position < 1:
            return
        current = self.head
        count = 1
        while(current):
            if count == position:
                return current
            count +=1
            current = current.next
        return None
    
    """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
    def insert(self,new_element, position):

        new_node = Element(new_element)
        if position == 1:
            new_node.next = self.head
            self.head = new_node
            return
        
        current = self.head
        count = 1

        while current and count <position:
            if count == position-1:
                new_node.next = current.next
                current.next = new_node
                return
            count +=1
            current = current.next
        print("Out of Range")
    
    """Delete the first node with a given value."""
    def delete(self, value):
        current = self.head
        previous = None
        found = False

        while current is not None and not found:
            if current.value == value:
                found = True
            else:
                previous = current
                current = current.next
        if found:
            if previous is None:
                self.head = current.next
            else:
                previous.next = current.next
        else:
            print("Value not found in the list")

#Test cases
#Set up some Elements
e1 = Element(100)
e2 = Element(200)
e3 = Element(300)
e4 = Element(400)

#Start setting up a LinkedList
l1 = LinkedList(e1)
l1.append(e2)
l1.append(e3)

#Test get_position
#should print 300
print(l1.head.next.next.value)
#should print 300
print(l1.get_position(3).value)

#Test insert
l1.insert(e4,3)
#Should print 400 now
print(l1.get_position(3).value)

#Test delete
l1.delete(100)
#Should print 200
print(l1.get_position(1).value)
#Should print 400
print(l1.get_position(2).value)
#Should print 300
print(l1.get_position(3).value)
    

