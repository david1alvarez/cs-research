class Node():
    def __init__(self, data, n):
        self.data = data
        self.children = []
        self.n = n
        self.isEnd = False

    def insert(self, data):
        if self.data is not None:
            if len(self.children) < self.n:
                self.children.append(Node(data, self.n))
            else:
                index = next(i for i,child in enumerate(self.children) if len(child.children) < self.n)
                if index is not None:
                    self.children[index].insert(data)
                else:
                    self.children[0].insert(data)
                
        else:
            self.data = data
        
    def dfs(self, value):
        """Preform a depth-first search on the tree"""
        if self.data == value:
            print(f'{value} exists!')
        else:
            for child in self.children:
                child.dfs(value)

    def bfs(self, value):
        if self.data == value:
            print(f'{value} exists!')
        elif self.children:
            for child in self.children:
                child.bfs(value)
            
    
    def query(self, value, useDfs=True):
        if useDfs:
            self.dfs(value)
        else:
            self.bfs(value)

    
    def printTree(self):
        print(self.data)
        if self.children:
            for child in self.children:
                child.printTree()


threeTree = Node(12,4)
threeTree.insert(5)
threeTree.insert(1)
threeTree.insert(2)
threeTree.insert(25)
threeTree.insert(3)
threeTree.insert(6)
threeTree.insert(13)
threeTree.insert(15)
threeTree.insert(55)
threeTree.insert(5.2)
threeTree.insert("fish")

threeTree.printTree()
threeTree.query(5)