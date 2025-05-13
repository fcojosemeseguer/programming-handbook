class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Points to the next node

class CircularLinkedList:
    def __init__(self):
        self.first = None  # First node of the list

    def insert_end(self, data):
        new_node = Node(data)
        if self.first is None:
            self.first = new_node
            new_node.next = self.first  # Point to itself (circular)
            return
        
        walk = self.first
        while walk.next != self.first:  # Traverse until last node
            walk = walk.next
        
        walk.next = new_node
        new_node.next = self.first  # Maintain circular link

    def display(self, count=10):  # Limit display to prevent infinite loop
        if self.first is None:
            print("List is empty")
            return
        temp = self.first.data
        walk = self.first
        for _ in range(count):  # Display limited nodes to avoid infinite loop
            print(walk.data, end=" -> ")
            walk = walk.next
            if walk == self.first:
                break
        print(f'Back to first :({temp})')

