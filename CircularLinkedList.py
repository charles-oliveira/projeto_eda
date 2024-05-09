class Node:
    def __init__(self):
        self.data = None
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_beginning(self, data):
        new_node = Node()
        new_node.data = data
        new_node.next = self.head
        if self.head is not None:
            last = self.head
            while last.next != self.head:
                last = last.next
            last.next = new_node
        else:
            new_node.next = new_node
        self.head = new_node

    def insert_end(self, data):
        new_node = Node()
        new_node.data = data
        if self.head is None:
            self.head = new_node
            self.head.next = self.head
        else:
            last = self.head
            while last.next != self.head:
                last = last.next
            last.next = new_node
            new_node.next = self.head
    
    def remove(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            last = self.head
            while last.next != self.head:
                last = last.next
            if self.head == self.head.next:
                self.head = None
            else:
                last.next = self.head.next
                self.head = self.head.next
        else:
            current = self.head
            while current.next != self.head:
                if current.next.data == data:
                    current.next = current.next.next
                    return
                current = current.next


    def search(self, data):
        if self.head is None:
            return False
        current = self.head
        while current.next != self.head:
            if current.data == data:
                return True
            current = current.next
        return False
    
    