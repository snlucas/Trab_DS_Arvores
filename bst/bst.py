from typing import Callable

from log.log import print_node


class Node:
    def __init__(self, key: int) -> None:
        self.key = key  # Node value
        self.left = None  # Left child pointer reference
        self.right = None  # Right child pointer reference


class BST:
    def __init__(self) -> None:
        self.root = None  # Node root

    def insert(self, node: Node) -> None:
        if self.root is None:  # Empty Tree
            self.root = node
        else:
            self.insert_node(self.root, node)

    def insert_node(self, root: Node, node: Node) -> None:
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

    # Using visitor pattern
    # BST Traverse
    def in_order(self, f: Callable = print_node):
        self.in_order_node(self.root, f)

    def in_order_node(self, node: Node, f: Callable):
        # Nil is the stop point
        # So, it runs recursively until None
        if node is not None:
            # Traverse left -> root -> right
            self.in_order_node(node.left, f)
            f(node.key)
            self.in_order_node(node.right, f)

    def pre_order(self, f: Callable = print_node):
        self.pre_order_node(self.root, f)

    def pre_order_node(self, node, f: Callable):
        if node is not None:
            # Traverse root -> left -> right
            f(node.key)
            self.pre_order_node(node.left, f)
            self.pre_order_node(node.right, f)

    def post_order(self, f: Callable = print_node):
        self.post_order_node(self.root, f)

    def post_order_node(self, node: Node, f: Callable):
        if node is not None:
            # Traverse left -> right -> root
            self.post_order_node(node.left, f)
            self.post_order_node(node.right, f)
            f(node.key)
