class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, e):
        self.queue.append(e)
        print(f"Enqueued: {e}")

    def dequeue(self):
        if not self.is_empty():
            dequeued = self.queue.pop(0)
            print(f"Dequeued: {dequeued}")
            return dequeued
        else:
            print("Queue is empty")
            return "Queue is empty"

    def first(self):
        if not self.is_empty():
            first_elem = self.queue[0]
            print(f"First element: {first_elem}")
            return first_elem
        else:
            print("Queue is empty")
            return "Queue is empty"

    def is_empty(self):
        empty = len(self.queue) == 0
        print(f"Queue is empty: {empty}")
        return empty

    def __len__(self):
        queue_length = len(self.queue)
        print(f"Queue length: {queue_length}")
        return queue_length


Q = Queue()
Q.enqueue(5)
Q.enqueue(3)
Q.dequeue()
Q.enqueue(2)
Q.enqueue(8)
Q.dequeue()
Q.dequeue()
Q.is_empty()
Q.dequeue()
Q.is_empty()
Q.enqueue(9)
Q.enqueue(7)
Q.first()
Q.enqueue(6)
len(Q)
Q.dequeue()
