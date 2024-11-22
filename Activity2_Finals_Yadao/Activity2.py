#1
class LinkedStack:
    '''LIFO Stack implementation using a singly linked list for storage.'''
    #---------------- nested _Node class ----------------
    class _Node:
        '''Lightweight non-public class for storing a singly linked node.'''
        __slots__ = '_element', '_next'  # streamline memory usage

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
        if self.is_empty():
            raise Exception('Stack is empty')
        return self._head._element

    def pop(self):
        '''Remove and return the elements from the top of the stack (LIFO)'''
        if self.is_empty():
            raise Exception("The stack is empty!")
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer

def evaluate_postfix(expression):
    stack = LinkedStack()
    operators = {'+', '-', '*', '/'}

    for token in expression.split():
        if token not in operators:
            stack.push(float(token))
        else:
            b = stack.pop()
            a = stack.pop()

            if token == '+':
                stack.push(a + b)
            elif token == '-':
                stack.push(a - b)
            elif token == '*':
                stack.push(a * b)
            elif token == '/':
                stack.push(a / b)

    return stack.pop()

# Example usage
postfix_expression = "5 2 + 8 3 - * 4 /"
result = evaluate_postfix(postfix_expression)
print(f"The result of the postfix expression '{postfix_expression}' is: {result}")

#2
class PositionalList:
    class _Node:
        __slots__ = '_element', '_prev', '_next'

        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next

    class Position:
        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):

            return self._node._element

        def __eq__(self, other):

            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):

            return not (self == other)

    def __init__(self):
        '''Create an empty list.'''
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, self._header, None)
        self._header._next = self._trailer
        self._size = 0

    def __len__(self):

        return self._size

    def is_empty(self):

        return self._size == 0

    def _validate(self, p):

        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._next is None:
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):

        if node is self._header or node is self._trailer:
            return None  # boundary violation
        else:
            return self.Position(self, node)

    def first(self):

        return self._make_position(self._header._next)

    def last(self):

        return self._make_position(self._trailer._prev)

    def before(self, p):

        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p):

        node = self._validate(p)
        return self._make_position(node._next)

    def __iter__(self):

        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    def _insert_between(self, e, predecessor, successor):

        node = self._Node(e, predecessor, successor)
        predecessor._next = node
        successor._prev = node
        self._size += 1
        return self._make_position(node)

    def add_first(self, e):

        return self._insert_between(e, self._header, self._header._next)

    def add_last(self, e):

        return self._insert_between(e, self._trailer._prev, self._trailer)

    def add_before(self, p, e):

        original = self._validate(p)
        return self._insert_between(e, original._prev, original)

    def add_after(self, p, e):

        original = self._validate(p)
        return self._insert_between(e, original, original._next)

    def delete(self, p):

        original = self._validate(p)
        element = original._element
        original._prev._next = original._next
        original._next._prev = original._prev
        original._prev = original._next = original._element = None  # deprecate node
        self._size -= 1
        return element

    def replace(self, p, e):

        original = self._validate(p)
        old_value = original._element
        original._element = e
        return old_value

def insertion_sort(arr, ascending=True):
    pos_list = PositionalList()
    for item in arr:
        pos_list.add_last(item)

    if ascending:
        sorted_arr = sorted(pos_list)
    else:
        sorted_arr = sorted(pos_list, reverse=True)

    return sorted_arr

# Example usage
numbers = [1, 72, 81, 25, 65, 91, 11]
ascending_sorted = insertion_sort(numbers, ascending=True)
descending_sorted = insertion_sort(numbers, ascending=False)

print("Sorted in ascending order:", ascending_sorted)
print("Sorted in descending order:", descending_sorted)
