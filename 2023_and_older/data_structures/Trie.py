class TrieNode:
    """A Node in a Trie structure"""

    def __init__(self, char):
        self.char = char
        self.isEnd = False
        self.counter = 0
        self.children = {}

class Trie(object):
    """A Trie object"""

    def __init__(self):
        """
        The trie has at least the root node.
        The root node does not store any character
        """
        self.root = TrieNode("")
    
    def insert(self, word):
        """Insert a node into the Trie graph"""
        node = self.root

        # loop through Trie to determine for partial or complete existance of the word
        # when no child containing the next char is found, add a child node containing the char
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                # child not found, add char child element
                newNode = TrieNode(char)
                node.children[char] = newNode
                node = newNode

        # end of word reached
        node.isEnd = True

        # Increment the counter to indicate that we see this word once more
        node.counter += 1

    def dfs(self, node, prefix):
        """Depth-first search of the Trie"""
    
        if node.isEnd:
            self.output.append((prefix + node.char, node.counter))

        for child in node.children.values():
            self.dfs(child, prefix + node.char)
        
    def query(self, x):
        """Given an input (prefix), retrieve all words stored in the trie with that prefix,
        sorting the words by the number of times they have been inserted
        """

        self.output = []
        node = self.root

        for char in x:
            if char in node.children:
                node = node.children[char]
            else:
                return []
        
        self.dfs(node,x[:-1])

        return sorted(self.output, key = lambda x: x[1], reverse=True)

t = Trie()
t.insert("was")
t.insert("word")
t.insert("war")
t.insert("what")
t.insert("where")
t.insert("what")
print(t.query("wh"))