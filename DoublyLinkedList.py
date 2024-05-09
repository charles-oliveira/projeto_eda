class Node:
    def __init__(self):
        self.data = None
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        
    def insert_beginning(self, data):
        new_node = Node()
        new_node.data = data
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def insert_end(self, data):
        new_node = Node()
        new_node.data = data
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last
    
    def remove(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                return
            current = current.next

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False
    

