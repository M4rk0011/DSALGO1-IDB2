# Linked Deque Implementation
class _DoublyLinkedBase:
    class _Node:
        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next

    def __init__(self):
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, self._header, None)
        self._header._next = self._trailer
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        new_node = self._Node(e, predecessor, successor)
        predecessor._next = new_node
        successor._prev = new_node
        self._size += 1

    def delete_first(self):
        if self.is_empty():
            raise Exception("Deque is empty!")
        return self._delete_node(self._header._next)

    def _delete_node(self, node):
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        return node._element

    def insert_last(self, e):
        self._insert_between(e, self._trailer._prev, self._trailer)

    def __str__(self):
        elements = []
        current = self._header._next
        while current is not self._trailer:
            elements.append(current._element)
            current = current._next
        return str(elements)

class LinkedDeque(_DoublyLinkedBase):
    def first(self):
        if self.is_empty():
            raise Exception("Deque is empty!")
        return self._header._next._element

# Linked Queue Implementation
class LinkedQueue:
    class _Node:
        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def enqueue(self, e):
        newest = self._Node(e, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer

# Linked Stack Implementation
class LinkedStack:
    class _Node:
        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def push(self, e):
        self._head = self._Node(e, self._head)
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise Exception("The stack is empty!")
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer


def activity_1():
    D = LinkedDeque()
    for i in range(1, 9):
        D.insert_last(i)

    print("Original Deque:", D)


    Q = LinkedQueue()
    while not D.is_empty():
        Q.enqueue(D.delete_first())

    for _ in range(3):
        D.insert_last(Q.dequeue())

    D.insert_last(Q.dequeue())
    while not Q.is_empty():
        D.insert_last(Q.dequeue())

    print("Rearranged Deque using Queue:", D)


    S = LinkedStack()
    for _ in range(5):
        S.push(D.delete_first())

    D.insert_last(S.pop())
    for _ in range(4):
        D.insert_last(S.pop())

    print("Rearranged Deque using Stack:", D)


activity_1()