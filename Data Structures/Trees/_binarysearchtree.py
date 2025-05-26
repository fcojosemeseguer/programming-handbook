class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def getLeft(self):
        return self.left
    def getRight(self):
        return self.right
    def getData(self):
        return self.data
    def setData(self,val):
        self.data = val

class BinarySearchTree:
    def __init__(self, rootData):
        self.root = Node(rootData)
        self.level = 0

    def preOrderTrasversal(self, root, trav):
        if root is None:
            return
        else:
            stack_pre = []
            stack_pre.append(root)
            while stack_pre:
                w = stack_pre.pop()
                trav.append(w.data)
                if w:
                    if w.left != None:
                        stack_pre.append(w.left)
                    if w.right != None:
                        stack_pre.append(w.right)

    def inOrderTraversal(self, root, trav):
        if root is None:
            return
        else:
            stack_in = []
            stack_in.append(root)
            while stack_in:
                w = stack_in.pop()
                if w:
                    if w.left != None:
                        stack_in.append(w.left)
                    
                    trav.append(w.data)

                    if w.right != None:
                        stack_in.append(w.right)

