from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()

    def peek(self):
        if not self.is_empty():
            return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

# Usage
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())  # Output: 1
print(queue.peek())  # Output: 2


# Queue using collections.deque
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        print(f"Enqueued {item} into the queue.")

    def dequeue(self):
        if not self.is_empty():
            item = self.queue.pop(0)
            print(f"Dequeued {item} from the queue.")
            return item
        else:
            print("Queue is empty. Cannot dequeue.")

    def peek(self):
        if not self.is_empty():
            print(f"Front of the queue is {self.queue[0]}.")
            return self.queue[0]
        else:
            print("Queue is empty.")

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

# Usage
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.peek()       # Output: Front of the queue is 10.
queue.dequeue()    # Output: Dequeued 10 from the queue.
queue.dequeue()    # Output: Dequeued 20 from the queue.
queue.dequeue()    # Output: Queue is empty. Cannot dequeue.

# Queue using collections.Queue

from queue import Queue

# Initialize a queue
queue = Queue()

# Enqueue items
queue.put(10)
print("Enqueued 10 into the queue.")
queue.put(20)
print("Enqueued 20 into the queue.")

# Peek at the front of the queue
if not queue.empty():
    front_item = queue.queue[0]
    print(f"Front of the queue is {front_item}.")

# Dequeue items
if not queue.empty():
    dequeued_item = queue.get()
    print(f"Dequeued {dequeued_item} from the queue.")
if not queue.empty():
    dequeued_item = queue.get()
    print(f"Dequeued {dequeued_item} from the queue.")

# Check if the queue is empty
if queue.empty():
    print("Queue is empty.")

