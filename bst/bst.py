from typing import Callable

# from log.log import print_node


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
    def in_order(self, f: Callable):
        self.in_order_node(self.root, f)

    def in_order_node(self, node: Node, f: Callable):
        # Nil is the stop point
        # So, it runs recursively until None
        if node is not None:
            # Traverse left -> root -> right
            self.in_order_node(node.left, f)
            f(node.key)
            self.in_order_node(node.right, f)

    def pre_order(self, f: Callable):
        self.pre_order_node(self.root, f)

    def pre_order_node(self, node, f: Callable):
        if node is not None:
            # Traverse root -> left -> right
            f(node.key)
            self.pre_order_node(node.left, f)
            self.pre_order_node(node.right, f)

    def post_order(self, f: Callable ):
        self.post_order_node(self.root, f)

    def post_order_node(self, node: Node, f: Callable):
        if node is not None:
            # Traverse left -> right -> root
            self.post_order_node(node.left, f)
            self.post_order_node(node.right, f)
            f(node.key)

    def insert (self, key: int):
        Node newNode = Node (key)

        # Se a raiz está vazia, inicializa ela
        if self.root == None:
            self.root = newNode
        else:
        # Se a árvore não está vazia
        # verifica em qual nó filho deve ser inserido o valor
            self._insert(key, self.root, newNode)

    def _insert(self, key: int, node: Node, newNode: Node):
        # Se a chave enviada for menor que a chave do nó,
        # navega para a esquerda e faz a verificação de nulidade
        # Se a chave enviado for maior que a do nó,
        # Navega para a direita e faz a verificação de nulidade
        # Verificação de nulidade = se o nó está vazio, insere valor nela
        # Se não, verifica em qual filho deve inserir o valor
        if key < node.key:
            if node.left == None:
                node.left = newNode
            else:
                self._insert(key, node.left)
        elif key > node.key:
            if node.right == None:
                node.right = newNode
            else:
                self._insert(key, node.right)

def fill_tree(tree,num_elems=10,max_int=10):
    from random import randint
    for _ in range (num_elems):
        cur_elem = randint(0,max_int)
        tree.insert(cur_elem)
    return tree


tree = BST()
tree = fill_tree(tree)

print(str(tree.root))
# print(tree.root.key)            
# print(tree.root.right.key)
