class DeQueue:
    DEFAULT_CAPACITY = 8
    def __init__(self):
        self._data = [None] * DeQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def display(self):
        return self._data

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        return self._data[self._front]

    def last(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        back = (self._front + self._size -1) % len(self._data)
        return self._data[back]

    def delete_first(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def delete_last(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        answer = self._data[(self._front + self._size) -1 % len(self._data)]
        self._data[(self._front + self._size) - 1 % len(self._data)] = None
        self._size -= 1
        return answer

    def add_first(self, e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        self._front = (self._front - 1) % len(self._data)
        self._data[self._front] = e
        self._size += 1

    def add_last(self, e):
        if (self._size == len(self._data)):
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def _resize(self, cap):
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0
