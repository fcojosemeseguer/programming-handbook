class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def display_node(self):
        print(self.data, end=' ')

class Stack:
    def __init__(self, data):
        self.first = Node(data)    

    def display(self):
        print('Stack:\t', end=' ')
        walk = self.first
        while walk is not None:
            walk.display_node()
            walk = walk.next
        print()

    """
    Insert Methods
    """

    def insert_end(self, data):
        if self.first is None:
            self.first = Node(data)
            return 
        
        walk = self.first
        while walk.next != None:
            walk = walk.next
        walk.next = Node(data)

    def del_end(self):
        if self.first is None:
            raise ValueError('Underflow, the stack is empty')
        
        if self.first.next is None:
            temp = self.first.data
            self.first = None
            return temp 
        
        walk = self.first    
        while walk.next.next is not None:
            walk = walk.next
        temp = walk.next.data
        walk.next = None
        return temp
        

