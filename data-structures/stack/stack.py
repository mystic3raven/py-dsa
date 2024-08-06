class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

# Usage
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())  # Output: 3
print(stack.peek())  # Output: 2

# Stack using collections.deque

from collections import deque

class Stack:
    def __init__(self):
        self.stack = deque()

    def push(self, item):
        self.stack.append(item)
        print(f"Pushed {item} onto the stack.")

    def pop(self):
        if not self.is_empty():
            item = self.stack.pop()
            print(f"Popped {item} from the stack.")
            return item
        else:
            print("Stack is empty. Cannot pop.")

    def peek(self):
        if not self.is_empty():
            print(f"Top of the stack is {self.stack[-1]}.")
            return self.stack[-1]
        else:
            print("Stack is empty.")

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

# Usage
stack = Stack()
stack.push(10)
stack.push(20)
stack.peek()       # Output: Top of the stack is 20.
stack.pop()        # Output: Popped 20 from the stack.
stack.pop()        # Output: Popped 10 from the stack.
stack.pop()        # Output: Stack is empty. Cannot pop.


# Stack using Custom Linked List

from collections import deque

class Stack:
    def __init__(self):
        self.stack = deque()

    def push(self, item):
        self.stack.append(item)
        print(f"Pushed {item} onto the stack.")

    def pop(self):
        if not self.is_empty():
            item = self.stack.pop()
            print(f"Popped {item} from the stack.")
            return item
        else:
            print("Stack is empty. Cannot pop.")

    def peek(self):
        if not self.is_empty():
            print(f"Top of the stack is {self.stack[-1]}.")
            return self.stack[-1]
        else:
            print("Stack is empty.")

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

# Usage
stack = Stack()
stack.push(10)
stack.push(20)
stack.peek()       # Output: Top of the stack is 20.
stack.pop()        # Output: Popped 20 from the stack.
stack.pop()        # Output: Popped 10 from the stack.
stack.pop()        # Output: Stack is empty. Cannot pop.


