class Node:    
    def __init__(self, data):
        self.data = data
        self.next = None

    def display_node(self):
        print(self.data, end=' ')

class LinkedList:

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
        walk = self.first
        while walk.next != None:
            walk = walk.next
        walk.next = Node(data)

    def insert_after(self, data, target):
        temp = Node(data)
        walk = self.first
        while walk != None and walk.data != target:
            walk = walk.next
            
        if walk is None:
            raise ValueError(f"Target node with data {target} not found in the list")
            
        temp.next = walk.next
        walk.next = temp

    """
    Delete Methods
    """
    
    def del_first(self):
        if (self.first != None):
            temp = self.first.data
            self.first = self.first.next
            return temp
        else:
            print('Underflow')

    def del_end(self):
        walk = self.first
        if (walk == None):
            raise ValueError("Underflow, the list is empty")
        elif (walk.next == None):
            temp = walk.data
            self.first = None
            return temp
        else: 
            while(walk.next.next != None):
                walk =walk.next
            temp = walk.next.data
            walk.next = None
            return temp
        
    def del_after(self, target):
        if self.first is None:
            raise ValueError("Underflow: tje list is empty")

        walk = self.first

        while walk is not None and walk.data != target:
            walk = walk.next

        if walk is None:
            raise ValueError(f"Target node with data {target} not found in the list")

        if walk.next is None:
            raise ValueError(f"No node exists after the target node {target}")

        temp = walk.next.data
        walk.next = walk.next.next  
        return temp
