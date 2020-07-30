class Trie {
    // initialize the root node
    root: TrieNode;
    constructor() {
        // assign a value to the root node
        this.root = new TrieNode();
    }

    addWord(word: string): void {
        // initialize the node to the root node
        let trieNode = this.root;

        // iterate through the letters of the added word
        for (const letter of word) {
            if (trieNode.has(letter)) {
                // if the trie node has the current letter as its children,
                // redefine the current trie node to the child node with that letter
                trieNode = trieNode.get(letter);
            } else {
                // if the trie node doesn't have any children with that letter
                // initialize a new child node with that letter
                trieNode = trieNode.setLetter(letter);
            }
        }

        // last TrieNode is the end of a word
        trieNode.isCompleteWord = true;
    }
}

class TrieNode {
    // initialize children to be a map of characters to TrieNodes
    children: Map<string, TrieNode>;
    // initialize variable to determine if the node represents the end of a complete word
    isCompleteWord: boolean;

    constructor() {
        // initialize the TrieNode defaults
        this.isCompleteWord = false;
        this.children = new Map<string, TrieNode>();
    }

    // check if the TrieNode has (in its map) a child for the specified letter
    has(letter: string): boolean {
        return this.children.has(letter)
    }

    // add a Map pair for a new letter and TrieNode to the current TrieNode's children
    setLetter(letter: string): TrieNode {
        // initialize the new trieNode
        const trieNode = new TrieNode();
        // add a new child node
        this.children.set(letter, trieNode);
        // return the newly created and associated trieNode
        return trieNode;
    }

    // get the child trieNode associated with the given letter
    get(letter: string): TrieNode {
        return this.children.get(letter)
    }
}