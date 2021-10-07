from typing import Callable
from node import Node
from log import print_node

class BST:
    def __init__(self) -> None:
        self.root = None  # Node root

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
