class LinkedStack:
    '''LIFO STack implementation using a singly linked list for storage.'''

    #---------------- nested _Node class ----------------
    class _Node:
        '''Lightweight non public class for storing a singly linked node.'''
        __slots__ = '_element', '_next' #streamline memory usage

        def __init__(self, element, next):
            self._element = element
            self._next = next

    #--------------- stack methods ----------------
    def __init__(self):
        '''Create an empty Stack'''
        self._head = None
        self._size = 0
    def __len__(self):
        '''Return the number of elements in the stack'''
        return self._size
    def is_empty(self):
        '''Return True if the stack is empty.'''
        return self._size == 0
    
    def push(self, e):
        '''Add element e to the top of the stack.'''
        self._head = self._Node(e, self._head)
        self._size += 1
    def top(self):
        '''Return but do not remove the element at the top of the stack'''
        '''Raise empty exception if the stack is empty!'''
        if self.is_empty():
            raise Exception('Stack is empty')
        return self._head._element #top of the stack is the head of the list
    def pop(self):
        '''Remove and return the elements fro mthe top of the stack (LIFO)'''
        '''Raise Empty exception if the stack is empty!'''
        if self.is_empty():
            raise Exception("The stack is empty!")
        answer = self._head._element
        self._head = self._head._next
        self._size -=1
        return answer

class DequeUsingTwoStacks:
    def __init__(self):
        self.stack1 = LinkedStack()
        self.stack2 = LinkedStack()

    def is_empty(self):
        return self.stack1.is_empty() and self.stack2.is_empty()

    def add_to_front(self, item):
        self.stack1.push(item)

    def add_to_rear(self, item):
        self.stack2.push(item)

    def remove_from_front(self):
        if self.stack1.is_empty():
            while not self.stack2.is_empty():
                self.stack1.push(self.stack2.pop())
        return self.stack1.pop()

    def remove_from_rear(self):
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.pop()