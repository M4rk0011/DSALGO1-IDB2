from DeQueue import DeQueue

class dequeUsingStackAndQueue:
    def __init__(self):
        self.stack = []
        self.queue = DeQueue()

    def __len__(self):
        return len(self.stack) + len(self.queue)

    def is_empty(self):
        return not self.stack and self.queue.is_empty()

    def add_first(self, e):
        self.stack.append(e)

    def add_last(self, e):
        self.queue.add_last(e)

    def delete_first(self):
        if self.is_empty():
            raise Exception("Deque is empty")

        if not self.stack:
            while not self.queue.is_empty():
                self.stack.append(self.queue.delete_first())

        return self.stack.pop()

    def delete_last(self):
        if self.is_empty():
            raise Exception("Deque is empty")

        if self.queue.is_empty():
            while self.stack:
                self.queue.add_first(self.stack.pop())

        return self.queue.delete_last()

    def first(self):
        if self.is_empty():
            raise Exception("Deque is empty")

        if self.stack:
            return self.stack[-1]

        return self.queue.first()

    def last(self):
        if self.is_empty():
            raise Exception("Deque is empty")

        if self.queue.is_empty():
            return self.stack[0]

        return self.queue.last()