class Node:
    def __init__(self, key: int) -> None:
        self.key = key  # Node value
        self.left = None  # Left child pointer reference
        self.right = None  # Right child pointer reference


class BST:
    def __init__(self) -> None:
        self.root = None  # Node root

    def insert(node: Node) -> None:
        if self.root is None:  # Empty Tree
            self.root = node
        else:
            self.insert_node(self.root, node)

    def insert_node(root: Node, node: Node) -> None:
        if root.key > node.key:
            # Check if the left side of the Root is empty
            if root.left is None:
                root.left = node
            else:
                self.insert_node(root.left, node)  # Recursively add node
        else:
            # Check if the right side of the Root is empty
            if root.right is None:
                root.right = node
            else:
                self.insert_node(root.right, node)  # Recursively add node
