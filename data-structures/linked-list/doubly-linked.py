class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """Append a new node to the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            print(f"Appended {data} as head of the list.")
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current
        print(f"Appended {data} to the end of the list.")

    def prepend(self, data):
        """Insert a new node at the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node
        print(f"Prepended {data} to the start of the list.")

    def delete_with_value(self, data):
        """Delete the first node with the specified value."""
        if not self.head:
            print("List is empty. Cannot delete.")
            return

        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:  # If head is to be deleted
                    self.head = current.next
                print(f"Deleted node with value {data}.")
                return
            current = current.next

        print(f"Node with value {data} not found.")

    def display(self):
        """Display the linked list."""
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

# Usage
dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.prepend(5)
dll.display()          # Output: 5 <-> 10 <-> 20 <-> None
dll.delete_with_value(10)
dll.display()          # Output: 5 <-> 20 <-> None
dll.delete_with_value(100)  # Output: Node with value 100 not found.
