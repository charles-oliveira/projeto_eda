from pilha_encadeada import Stack
from pilha_duplamente_encadeada import  DoublyLinkedStack

def test_stack():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1
    assert stack.pop() is None
    print("Teste da pilha encadeada passou!")

def test_doubly_linked_stack():
    stack = DoublyLinkedStack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1
    assert stack.pop() is None
    print("Teste da pilha duplamente encadeada passou!")

if __name__ == "__main__":
    test_stack()
    test_doubly_linked_stack()


