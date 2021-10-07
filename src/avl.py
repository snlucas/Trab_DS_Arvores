from node import Node
from bst import BST

class AVL(BST):

    #Estrutura da árvore
    def __init__(self) -> None:
        super().__init__()
        self.setChildren(None, None)

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
