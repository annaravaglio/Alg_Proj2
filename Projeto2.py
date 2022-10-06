import pandas as pd
import numpy as np
import time
import sys
sys.setrecursionlimit(5000000)

arquivo = pd.read_csv("books.csv", sep=";")

#Funções para formatar o tempo
def formatTime(diff):
    r = diff % 3600
    minutes, seconds = divmod(r, 60)
    print("{minutes:0>2}:{seconds:05.3f}".format(minutes=minutes, seconds=seconds))

#Cálculo do tempo
#Marca tempo inicial
initIndice = time.time()
#Marca tempo final
fimIndice = time.time()
#Subtrai inicial do final para o total de tempo utilizado na busca
totalIndice = fimIndice - initIndice
#Formata o tempo total de execução da busca
formatTime(totalIndice)

class NodoArvore:
    def __init__(self, chave=None, esquerda=None, direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita

    def __repr__(self):
        return '%s <- %s -> %s' % (self.esquerda and self.esquerda.chave,
                                    self.chave,
                                    self.direita and self.direita.chave)
                                    
def em_ordem_binaria(raiz):
    if not raiz:
        return

    # Visita filho da esquerda.
    em_ordem_binaria(raiz.esquerda)

    # Visita nodo corrente.
    print(raiz.chave),

    # Visita filho da direita.
    em_ordem_binaria(raiz.direita)

def insere_binaria(raiz, nodo):
    """Insere um nodo em uma árvore binária de pesquisa."""
    # Nodo deve ser inserido na raiz.
    if raiz is None:
        raiz = nodo

    # Nodo deve ser inserido na subárvore direita.
    elif raiz.chave < nodo.chave:
        if raiz.direita is None:
            raiz.direita = nodo
        else:
            insere_binaria(raiz.direita, nodo)

    # Nodo deve ser inserido na subárvore esquerda.
    else:
        if raiz.esquerda is None:
            raiz.esquerda = nodo
        else:
            insere_binaria(raiz.esquerda, nodo)

def busca_binaria(raiz, chave):
    """Procura por uma chave em uma árvore binária de pesquisa."""
    # Trata o caso em que a chave procurada não está presente.
    if raiz is None:
        return None

    # A chave procurada está na raiz da árvore.
    if raiz.chave == chave:
        return raiz

    # A chave procurada é maior que a da raiz.
    if raiz.chave < chave:
        return busca_binaria(raiz.direita, chave)

    # A chave procurada é menor que a da raiz.
    return busca_binaria(raiz.esquerda, chave)

arvorebinaria = NodoArvore(0)
initInsercaoBin = time.time()
for i in range(0,2999,+1):
    add = arquivo.iloc[i,0]
    node = NodoArvore(add)
    insere_binaria(arvorebinaria, node)
fimInsercaoBin = time.time()
insercaoBin = fimInsercaoBin - initInsercaoBin
formatTime(insercaoBin)
print(insercaoBin)

initOrdena = time.time()
em_ordem_binaria(arvorebinaria)
fimOrdena = time.time()
ordenaBin = fimInsercaoBin - initInsercaoBin

initIndice1 = time.time()
busca_binaria(arvorebinaria,1)
fimIndice1 = time.time()
totalIndice1 = fimIndice1 - initIndice1
formatTime(totalIndice1)
print(totalIndice1)

initIndice2 = time.time()
busca_binaria(arvorebinaria,5518)
fimIndice2 = time.time()
totalIndice2 = fimIndice2 - initIndice2
formatTime(totalIndice2)
print(totalIndice2)

initIndice3 = time.time()
busca_binaria(arvorebinaria,11037)
fimIndice3 = time.time()
totalIndice3 = fimIndice3 - initIndice3
formatTime(totalIndice3)
print(totalIndice3)

initIndice4 = time.time()
busca_binaria(arvorebinaria,2802)
fimIndice4 = time.time()
totalIndice4 = fimIndice4 - initIndice4
formatTime(totalIndice4)
print(totalIndice4)

initIndice5 = time.time()
busca_binaria(arvorebinaria,8249)
fimIndice5 = time.time()
totalIndice5 = fimIndice5 - initIndice5
formatTime(totalIndice5)
print(totalIndice5)

initIndice6 = time.time()
busca_binaria(arvorebinaria,10964)
fimIndice6 = time.time()
totalIndice6 = fimIndice6 - initIndice6
formatTime(totalIndice6)
print(totalIndice6)

initIndice7 = time.time()
busca_binaria(arvorebinaria,5000)
fimIndice7 = time.time()
totalIndice7 = fimIndice7 - initIndice7
formatTime(totalIndice7)
print(totalIndice7)


import sys
from tkinter.tix import Tree

from setuptools import find_packages

# Create a tree node
class TreeNode(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree(object):

    # Function to insert a node
    def insert_node(self, root, key):

        # Find the correct location and insert the node
        if not root:
            return TreeNode(key)
        elif key < root.key:
            root.left = self.insert_node(root.left, key)
        else:
            root.right = self.insert_node(root.right, key)

        root.height = 1 + max(self.getHeight(root.left),self.getHeight(root.right))

        # Update the balance factor and balance the tree
        balanceFactor = self.getBalance(root)
        if balanceFactor > 1:
            if key < root.left.key:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)

        if balanceFactor < -1:
            if key > root.right.key:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)

        return root

    def find_node(self,root,val):
        if (root is None):
            return False
        elif (root.key == val):
            return True
        elif(root.key < val):
            return self.find_node(root.right,val)
        return self.find_node(root.left,val)


    # Function to delete a node
    def delete_node(self, root, key):

        # Find the node to be deleted and remove it
        if not root:
            return root
        elif key < root.key:
            root.left = self.delete_node(root.left, key)
        elif key > root.key:
            root.right = self.delete_node(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.getMinValueNode(root.right)
            root.key = temp.key
            root.right = self.delete_node(root.right, temp.key)
        if root is None:
            return root

        # Update the balance factor of nodes
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        balanceFactor = self.getBalance(root)

        # Balance the tree
        if balanceFactor > 1:
            if self.getBalance(root.left) >= 0:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        if balanceFactor < -1:
            if self.getBalance(root.right) <= 0:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        return root

    # Function to perform left rotation
    def leftRotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.getHeight(z.left),self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),self.getHeight(y.right))
        return y

    # Function to perform right rotation
    def rightRotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.getHeight(z.left),self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),self.getHeight(y.right))
        return y

    # Get the height of the node
    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    # Get balance factore of the node
    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root
        return self.getMinValueNode(root.left)

    def preOrder(self, root):
        if not root:
            return
        print("{0} ".format(root.key), end="")
        self.preOrder(root.left)
        self.preOrder(root.right)

    # Print the tree
    def printHelper(self, currPtr, indent, last):
        if currPtr != None:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "
            print(currPtr.key)
            self.printHelper(currPtr.left, indent, False)
            self.printHelper(currPtr.right, indent, True)

arvoreAVL = AVLTree()
root = None
initInsercaoAVL = time.time()
for i in range(0,2999,+1):
    add = arquivo.iloc[i,0]
    root = arvoreAVL.insert_node(root,add)
fimInsercaoAVL = time.time()
insercaoAVL = fimInsercaoAVL - initInsercaoAVL
formatTime(insercaoAVL)
print(insercaoAVL)

arvoreAVL.printHelper(root, "", True)

initIndice1 = time.time()
print(arvoreAVL.find_node(root,1))
fimIndice1 = time.time()
totalIndice1 = fimIndice1 - initIndice1
formatTime(totalIndice1)
print(totalIndice1)

initIndice2 = time.time()
print(arvoreAVL.find_node(root,5518))
fimIndice2 = time.time()
totalIndice2 = fimIndice2 - initIndice2
formatTime(totalIndice2)
print(totalIndice2)

initIndice3 = time.time()
print(arvoreAVL.find_node(root,11037))
fimIndice3 = time.time()
totalIndice3 = fimIndice3 - initIndice3
formatTime(totalIndice3)
print(totalIndice3)

initIndice4 = time.time()
print(arvoreAVL.find_node(root,2802))
fimIndice4 = time.time()
totalIndice4 = fimIndice4 - initIndice4
formatTime(totalIndice4)
print(totalIndice4)

initIndice5 = time.time()
print(arvoreAVL.find_node(root,8249))
fimIndice5 = time.time()
totalIndice5 = fimIndice5 - initIndice5
formatTime(totalIndice5)
print(totalIndice5)

initIndice6 = time.time()
print(arvoreAVL.find_node(root,10964))
fimIndice6 = time.time()
totalIndice6 = fimIndice6 - initIndice6
formatTime(totalIndice6)
print(totalIndice6)

initIndice7 = time.time()
print(arvoreAVL.find_node(root,5000))
fimIndice7 = time.time()
totalIndice7 = fimIndice7 - initIndice7
formatTime(totalIndice7)
print(totalIndice7)

initIndice8 = time.time()
print(arvoreAVL.find_node(root,3939))
fimIndice8 = time.time()
totalIndice8 = fimIndice8 - initIndice8
formatTime(totalIndice8)
print(totalIndice8)