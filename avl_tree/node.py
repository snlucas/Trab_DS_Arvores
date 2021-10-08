class Node():
    # Inicializador 
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return "Chave" + str(self.key) + "Valor: " + str(self.value) + " }"