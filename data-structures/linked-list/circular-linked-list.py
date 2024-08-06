class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """Append a new node to the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            print(f"Appended {data} as head of the circular list.")
            return
        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = new_node
        new_node.next = self.head
        print(f"Appended {data} to the end of the circular list.")

    def prepend(self, data):
        """Insert a new node at the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head

        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = new_node
        self.head = new_node
        print(f"Prepended {data} to the start of the circular list.")

    def display(self):
        """Display the circular linked list."""
        nodes = []
        current = self.head
        while True:
            nodes.append(str(current.data))
            current = current.next
            if current == self.head:
                break
        print(" -> ".join(nodes) + " -> HEAD")

# Usage
cll = CircularLinkedList()
cll.append(10)
cll.append(20)
cll.prepend(5)
cll.display()  # Output: 5 -> 10 -> 20 -> HEAD
