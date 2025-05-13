class Node():

    def __init__(self, data):
        self.data = data
        self.next = None

    def display_node(self):
        print(self.data, end=' ')


class Queue():
    
    def __init__(self, data):
        self.first = Node(data)

    def insert_end(self, data):
        if self.first is None:
            self.first = Node(data)
            return

        elif self.first.next is None:
            self.first.next = Node(data)
            return
        
        walk = self.first
        while walk.next is not None:
            walk = walk.next

        walk.next = Node(data)

    def del_beginning(self):
        if self.first is None:
            return None
        temp = self.first.data
        self.first = self.first.next
        return temp
    
    def display(self):
        print('Queue:\t', end=' ')
        walk = self.first
        while walk is not None:
            walk.display_node()
            walk = walk.next
        print()
        
