from enum import Enum
from bst.bst import BST, Node


class AVL(BST):
    def __init__(self) -> None:
        super().__init__()  # Add root


    # === Adding insert ===
    def insert(self, key: int) -> None:
        self.root = self.insert_node(self.root, key)


    def insert_node(self, node: Node, key: int) -> Node:
        if node is None:
            return Node(key)
        elif key < node.key:
            node.left = self.insert_node(node.left, key)
        elif key > node.key:
            node.right = self.insert_node(node.right, key)
        else:
            return node

        # Balance Tree
        balance_factor = self.get_balance_factor(node)
        balance_factor_dict = self.balance_factor()
        
        if balance_factor == balance_factor_dict['UNBALANCED_LEFT']:
            if key < node.left.key:
                node = self.rotation_ll(node)
            else:
                return self.rotation_lr(node)
        if balance_factor == balance_factor_dict['UNBALANCED_RIGHT']:
            if key > node.right.key:
                node = self.rotation_rr(node)
            else:
                return self.rotation_rl(node)
        else:
            return node


    # === Adding remove ===
    def remove(self, key: int) -> Node: pass


    # === Adding search ===
    def search(self, key: int) -> bool:
        return self.search_node(self.root, key)

    def search_node(self, node: Node, key: int) -> bool:
        if node is None:
            return False
        elif key < node.key:
            # Haven't finded yet, and value is less than what's in the node.
            # So, recursevely search left 'till find it.
            return self.search_node(node.left, key)
        elif key > node.key:
            # Haven't finded yet, and value is bigger than what's in the node.
            # So, recursevely search right 'till find it.
            return self.search_node(node.right, key)
        else:
            return True  # Finded

    # === Adding getHeight ===
    def get_node_height(self, node: Node) -> int:
        # Recursevely get tree height
        
        # Nil leaves
        if node is None:
            return -1

        # +1 supports nil leaves.
        # So when we have a leaf, it doesn't have any 
        # left or right key.
        # We'll have something like max(-1, -1) in that situation.
        # It obviously returns -1. 
        # So to solve this problem we need to add one to this operation.
        # Now we have something like this:
        # max(-1, -1) + 1. Which returns (-1 + 1) = 0. So we have a leaf.
        # Next steps will search for left and right nodes, and do the same way.  
        return max(self.get_node_height(node.left), self.get_node_height(node.right)) + 1


    # === Adding balance factor ===
    def get_balance_factor(self, node: Node):
        # We do have to balance our tree to keep h = O(lg n)
        deep_difference = self.get_node_height(node.left) - self.get_node_height(node.right)

        balance_factor = self.balance_factor()

        if deep_difference == -2:
            return balance_factor['UNBALANCED_RIGHT']
        elif deep_difference == -1:
            return balance_factor['LIGHTLY_UNBALANCED_RIGHT']
        elif deep_difference == 1:
            return balance_factor['LIGHTLY_UNBALANCED_LEFT']
        elif deep_difference == 2:
            return balance_factor['UNBALANCED_LEFT']
        else:
            return balance_factor['BALANCED']



    def rotation_ll(self, node: Node) -> Node:
        # Left-Left Rotation
        # Simple Right Rotation
        # (Heavy left)
        #
        # E.g. leaf: 1, child: 2, root: 3
        # ........pivot: child, right leaf: root
        # ........left child: 1, right child: 3, root: 2
        #
        #            3                           2
        #          /                          /    \
        #       2            ->            1        3
        #     /
        #  1

        # tmp -> pivot node
        tmp = node.left
        node.left, tmp.right = tmp.right, node

        return tmp


    def rotation_rr(self, node: Node) -> Node:
        # Right-Right Rotation
        # Simplet Left Rotation
        # (Heavy right)
        #
        # E.g. leaf: 3, child: 2, root: 1
        # ........pivot: child, left leaf: root
        # ........left child: 1, right child: 3, root: 2
        #
        #      3                                 2
        #       \                             /    \
        #        2           ->            1        3
        #          \
        #            1

        # tmp -> pivot node
        tmp = node.right
        node.right, tmp.left = tmp.left, node

        return tmp


    def rotation_lr(self, node: Node) -> Node:
        # Left-Right Rotation
        # Double Right Rotation
        # (Heavy right in left child)
        # 
        # Solution:
        # ........simple left rotation + simple right rotation
        node.left = self.rotation_rr(node.left)

        return self.rotation_rr(node)


    def rotation_rl(self, node: Node) -> Node:
        # Right-Left Rotation
        # Double Left Rotation
        # (Heavy left in right child)
        # 
        # Solution:
        # ........simple right rotation + simple left rotation
        node.right = self.rotation_ll(node)

        return self.rotation_rr(node)


    # Works as Enum to Improve reuse
    def balance_factor(self) -> dict:
        return {
            'UNBALANCED_RIGHT': 1,
            'UNBALANCED_LEFT': 5,
            'LIGHTLY_UNBALANCED_RIGHT': 2,
            'LIGHTLY_UNBALANCED_LEFT': 4,
            'BALANCED': 3
        }
