class dequeUsingStack:
    def __init__(self):
        self.S_in = []
        self.S_out = []

    def __len__(self):
        return len(self.S_in) + len(self.S_out)

    def is_empty(self):
        return not self.S_in and not self.S_out

    def display(self):
        return self.S_in + self.S_out[::-1]

    def add_first(self, e):
        self.S_in.append(e)

    def add_last(self, e):
        self.S_out.append(e)

    def delete_first(self):
        if self.is_empty():
            raise Exception("Deque is empty")

        if not self.S_in:
            while self.S_out:
                self.S_in.append(self.S_out.pop())

        return self.S_in.pop()

    def delete_last(self):
        if self.is_empty():
            raise Exception("Deque is empty")

        if not self.S_out:
            while self.S_in:
                self.S_out.append(self.S_in.pop())

        return self.S_out.pop()

    def first(self):
        if self.is_empty():
            raise Exception("Deque is empty")

        if not self.S_in:
            while self.S_out:
                self.S_in.append(self.S_out.pop())

        return self.S_in[-1]

    def last(self):
        if self.is_empty():
            raise Exception("Deque is empty")

        if not self.S_out:
            while self.S_in:
                self.S_out.append(self.S_in.pop())

        return self.S_out[-1]