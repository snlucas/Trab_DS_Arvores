from bst import BST, Node


class AVL(BST):
    def __init__(self) -> None:
        super().__init__()  # Add root
        self.setChildren(None, None)


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

        # Similar to switch case
        balance_factor = {
            -2: 1,
            2: 5,
            -1: 2,
            1: 4
        }

        if deep_difference in balance_factor:
            return balance_factor[deep_difference]


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
        tmp, node.left, tmp.right = node.left, tmp.right, node

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
        tmp, node.right, tmp.left = node.right, tmp.left, node

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



    # ========================================
    def setChildren(self, left, right):
        self.left = left
        self.right = right


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
        self.rebalance()


    def deepthL(self):
        deepL = 0
        if self.left:
            deepL = self.left.deepth()

        return deepL


    def deepthR(self):
        deepR = 0
        if self.right:
            deepR = self.right.deepth()

        return deepR


    def balance(self):
        deepL = self.deepthL()
        deepR = self.deepthR()

        if self.right:
            deepR = self.right.deepth()
        return deepL - deepR


    def deepth(self):
        deepL = self.deepthL()
        deepR = self.deepthR()

        return 1 + max(deepL, deepR)


    def rotateLeft(self):
        self.value, self.right.value = self.right.value, self.value
        prevLeft = self.left
        self.setChildren(self.right, self.right.right)
        self.left.setaFilhos(prevLeft, self.left.left)


    def rotateRight(self):
        self.value, self.left.value = self.left.value, self.value
        prevRight = self.right
        self.setChildren(self.left.left, self.left)
        self.right.setChildren(self.right.right, prevRight)


    def rebalance(self):
        balance: int = self.balance()
        if balance > 1:
            if self.left.balance() > 0:
                self.rotateRight()
            else:
                self.left.rotateLeft()
                self.rotateRight()
        elif balance < -1:
            if self.right.balance() < 0:
                self.rotateLeft()
            else:
                self.right.rotateRight()
                self.rotateLeft()
