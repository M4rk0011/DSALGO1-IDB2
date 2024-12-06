from dequeUsingStack import dequeUsingStack as dequeUsingStack
from dequeUsingStackAndQueue import dequeUsingStackAndQueue as dequeUsingStackAndQueue
from DLS import DLS as DLS

double = DLS()
deque = dequeUsingStack()
D = dequeUsingStackAndQueue()

print("Deque using STACK:")
deque.add_first(1)
print("First number that was added on the stack is:  ", deque.delete_first())
deque.add_last(2)
print("The number that was added on the last stack is: ", deque.delete_first())
deque.add_first(3)
deque.add_last(8)
deque.add_last(9)
print("The first number in the stack is: ", deque.first())
print("The last number in the stack is: ", deque.last())
print("Checking if the stack is empty: ", deque.is_empty())
print()


print("Deque using Stack and Queue:")
D.add_first(5)
print("First number that was added is:  ", D.delete_first())
D.add_last(2)
print("The number that was added is: ", D.delete_first())
D.add_first(1)
D.add_last(7)
D.add_last(8)
print("The first number is: ", D.first())
print("The last number is: ", D.last())
print("Checking if the stack is empty: ", D.is_empty())
print()


print("Deque using LinkedStack And LinkedQueue:")
double.add_first(6)
double.add_last(10)
double.add_first(16)
double.add_first(75)
double.add_first(21)
print("The first number is: ", double.first())
print("The last number is: ", double.last())
print("Checking if the stack is empty: ", double.is_empty())
print()