import sys
from avl.avl import AVL


avl = AVL()

print('Trabalho de Estrutura de Dados')
print('AVL Tree')

while True:
    print('i - Inserir\nb - Buscar\nr - Remover\np - Percorrer\ns - Sair')
    entrada = input().lower()

    if entrada == 'i':
        n = input('Valor da Chave: ')
        avl.insert(n)
    elif entrada == 'b':
        n = input('Valor da Chave: ')
        if avl.search(n):
            print('Encontrado!')
        else:
            print('Nao encontrado!')
    elif entrada == 'r':
        n = input('Valor da Chave: ')
        avl.remove(n)
    elif entrada == 'p':
        print('1 - Percurso In Order')
        print('2 - Percurso Post Order')
        print('3 - Percurso Pre Order\n')

        n = int(input())

        if n == 1:
            avl.in_order()
        elif n == 2:
            avl.post_order()
        elif n == 3:
            avl.pre_order()
    elif entrada == 's':
        sys.exit()
