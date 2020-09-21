class bstNode {
    data: any;
    right: bstNode;
    left: bstNode;
    constructor(data) {
        this.data = data;
    }
}

class BinarySearchTree {
    root: bstNode;
    constructor(data: any) {
        this.root = new bstNode(data)
    }

    searchTree(data: any, node: bstNode): bstNode {
        if (node.data === data) {
            return node;
        }
        if(data < node.data) {
            this.searchTree(data, node.left)
        }
        if(data > node.data) {
            this.searchTree(data, node.right)
        }
    }

    getChildren(node: bstNode, children: bstNode[] = []): bstNode[] {
        if (node.left) {
            children.push(node.left)
            children = this.getChildren(node.left, children);
        }
        if (node.right) {
            children.push(node.right)
            children = this.getChildren(node.right, children);
        }
        return children
    }

    add(data: any, node: bstNode = this.root): void {
        if (data < node.data) {
            if(node.left) {
                this.add(data, node.left)
            } else {
                node.left = new bstNode(data)
            }
        } else if (data > node.data) {
            if(node.right) {
                this.add(data, node.right)
            } else {
                node.right = new bstNode(data)
            }
        }
    }

    change(data: any, update: any, node: bstNode = this.root): void {
        this.searchTree(data, node).data = update
    }

    remove(data: any, node: bstNode = this.root): void {
        let children: bstNode[] = []
        if (this.root.data = data) return; // error condition to prevent internal deletion of BST
        if (node.left.data = data) {
            children = this.getChildren(node.left);
            node.left = null;
        }
        if(node.right.data = data) {
            children = this.getChildren(node.right);
            node.right = null;
        }
        children.forEach((child) => {this.add(child.data)})
    }
}

let tree = new BinarySearchTree(7)
console.log(tree)