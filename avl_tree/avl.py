from bst.bst import BST
from bst.bst import Node

class AVL(BST):
    def __init__(self) -> None:
        super().__init__()
        self.setChildren(None, None)

    def setChildren(self, left: Node, right: Node):
        self.left = left
        self.right = right

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

    def insert(self, node: Node):
        super().insert(node)
        self.rebalance()