from LinkedQueue import LinkedQueue as LinkedQueue
from LinkedStack import LinkedStack as LinkedStack

class DLS:
    def __init__(self):
        # Create a stack for the front and a queue for the back
        self.stack = LinkedStack()
        self.queue = LinkedQueue()

    def __len__(self):
        # Total number of elements in the deque is the sum of the stack and queue sizes
        return len(self.stack) + len(self.queue)

    def is_empty(self):
        # The deque is empty if both the stack and the queue are empty
        return self.stack.is_empty() and self.queue.is_empty()

    def display(self):
        # Combine the front (from stack) and back (from queue) for display
        stack_elements = []
        current = self.stack._head  # Traverse stack
        while current is not None:
            stack_elements.append(current._element)
            current = current._next
        stack_elements.reverse()  # Reverse stack to get front-to-back order

        queue_elements = []
        current = self.queue._head  # Traverse queue
        while current is not None:
            queue_elements.append(current._element)
            current = current._next

        return stack_elements + queue_elements  # Display front to back

    def add_first(self, e):
        # Push element to the stack (front of the deque)
        self.stack.push(e)

    def add_last(self, e):
        # Enqueue element to the queue (back of the deque)
        self.queue.enqueue(e)

    def delete_first(self):
        # Remove and return the front element of the deque
        if self.is_empty():
            raise Exception("Deque is empty")

        if self.stack.is_empty():
            # If the stack is empty, transfer elements from the queue to the stack
            while not self.queue.is_empty():
                self.stack.push(self.queue.dequeue())

        # Now pop from the stack (front)
        return self.stack.pop()

    def delete_last(self):
        # Remove and return the last element of the deque
        if self.is_empty():
            raise Exception("Deque is empty")

        if self.queue.is_empty():
            # If the queue is empty, transfer elements from the stack to the queue
            while not self.stack.is_empty():
                self.queue.enqueue(self.stack.pop())

        # Now dequeue from the queue (back)
        return self.queue.dequeue()

    def first(self):
        # Access the first element of the deque without removing it
        if self.is_empty():
            raise Exception("Deque is empty")

        if self.stack.is_empty():
            # If the stack is empty, transfer elements from the queue to the stack
            while not self.queue.is_empty():
                self.stack.push(self.queue.dequeue())

        return self.stack.top()  # Peek at the top of the stack (front of the deque)

    def last(self):
        # Access the last element of the deque without removing it
        if self.is_empty():
            raise Exception("Deque is empty")

        if self.queue.is_empty():
            # If the queue is empty, transfer elements from the stack to the queue
            while not self.stack.is_empty():
                self.queue.enqueue(self.stack.pop())

        return self.queue.first()