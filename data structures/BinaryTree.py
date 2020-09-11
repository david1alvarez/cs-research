class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    
    def insert(self, data):
        if self.data is not None:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
            # on data == self.data, do nothing as that node already exists
        else:
            self.data = data

    def findVal(self, lookupVal):
        if lookupVal < self.data:
            if self.left is None:
                return str(lookupVal)+" not found"
            return self.left.findVal(lookupVal)
        elif lookupVal > self.data:
            if self.right is None:
                return str(lookupVal)+" not found"
            return self.right.findVal(lookupVal)
        else:
            return str(self.data) + " found"
    
    def printTree(self):
        if self.left:
            self.left.printTree()
        print( self.data),
        if self.right:
            self.right.printTree()

root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
print(root.findVal(7))
print(root.findVal(14))