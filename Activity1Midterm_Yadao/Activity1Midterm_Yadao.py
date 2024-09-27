class Stack:
    def __init__(self):
        self.items = []

    def isempty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isempty():
            return self.items.pop()
        else:
            return "Stack is empty"

    def size(self):
        return len(self.items)

    def top(self):
        if not self.isempty():
            return self.items[-1]
        else:
            return "Stack is empty"


S = Stack()
S.push(5)
S.push(3)

print("Lenght:",len(S.items))
print("Pop:",S.pop())
print("Stack Empty:",S.isempty())
print("Pop:",S.pop())
print("Stack Empty:",S.isempty())
print("Pop:",S.pop())
S.push(7)
S.push(9)
print("Top Element:",S.top())
S.push(4)
print("Lenght:",len(S.items))
print("Pop:",S.pop())
S.push(6)
S.push(8)
print("Pop:",S.pop())

S.push(5)
S.push(3)

print("Pop:",S.pop())
S.push(7)
S.push(9)
print("Top Element:",S.top())
S.push(4)
print("Lenght:",len(S.items))
print("Pop:",S.pop())
S.push(6)
S.push(8)
print("Pop:",S.pop())

stack = []

def push(val):
    stack.append(val)

def pop():
    if len(stack) == 0:
        return None
    return stack.pop()

push(5)
push(3)
print(pop())
push(2)
push(8)
print(pop())
print(pop())
push(9)
push(1)
print(pop())
push(7)
push(6)
print(pop())
print(pop())
push(4)
print(pop())
print(pop())
print(pop())

