class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

    def display_node(self):
        print(self.data, end=' ')
    
class DoublyLinkedList:

    def __init__(self, data):
        self.first = Node(data)

    
    def display(self):
        print('List:\t', end=' ')
        walk = self.first
        while walk != None:
            walk.display_node()
            walk = walk.next
        print()
   

    """
    Insert Methods
    """

    def insert_beg(self,data):
        temp = Node(data)
        temp.next = self.first
        self.first = temp

    def insert_end(self, data):
        
        if self.first is None:
            self.first = Node(data)
            return 
        
        walk = self.first
        while walk.next is not None:
            walk = walk.next
        walk.next = Node(data)

    def insert_after(self, data, target):
        walk = self.first

        while walk is not None and walk.data != target:
            walk = walk.next

        if walk is None:
            raise ValueError("Target Not Found")

        temp = Node(data)
        walk_next = walk.next  # Store the next node

        walk.next = temp
        temp.prev = walk
        temp.next = walk_next

        if walk_next is not None:
            walk_next.prev = temp


    """
    Delete Methods
    """

    def del_first(self):
        if self.first is None:
            raise ValueError('Underflow, the list is empty')

        temp = self.first.data
        self.first = self.first.next
        if self.first is not None:
            self.first.prev = None

        return temp

    def del_end(self):
        if self.first is None:
            raise ValueError("Underflow: The list is empty")

        if self.first.next is None:
            temp = self.first.data
            self.first = None  # Remove the only node
            return temp

        walk = self.first

        while walk.next.next is not None:
            walk = walk.next

        temp = walk.next.data
        walk.next = None  
        return temp
        
    def del_after(self, target):
        if self.first is None:
            raise ValueError("Underflow: The list is empty")

        walk = self.first

        while walk is not None and walk.data != target:
            walk = walk.next

        if walk is None:
            raise ValueError("Target Not Found")

        if walk.next is None:
            raise ValueError(f"No node exists after the target node {target}")
        temp = walk.next.data
        walk.next = walk.next.next  

        if walk.next is not None:
            walk.next.prev = walk

        return temp