from collections import deque


class Node:
    def __init__(self, val):
        self.parent = None
        self.left = None
        self.right = None
        self.element = val

    def __iter__(self):
        if self.left:
            yield from self.left
        yield self.element
        if self.right:
            yield from self.right


class BinaryTree:

    def __init__(self):
        self.root = None

    def __iter__(self):
        if self.root is not None:
            yield from self.root

    def getRoot(self):
        return self.root

    def is_root(self, p):
        return self.root == p

    def depth(self, p):
        if self.is_root(p):
            return 0
        return 1 + self.depth(p.parent)

    def addroot(self, val):
        if self.root is not None:
            print("Tree is not Empty")
        else:
            self.root = Node(val)

    def addleft(self, p, val):
        if p is None:
            print("Empty Reference !")
            return
        if p.left is not None:
            print("Left child is not Empty")
            return
        else:
            p.left = Node(val)
            p.left.parent = p
            return p.left

    def addright(self, p, val):
        if p is None:
            print("Empty Reference !")
            return
        if p.right is not None:
            print("Right child is not Empty")
            return
        else:
            p.right = Node(val)
            p.right.parent = p
            return p.right

    def is_leaf(self, p):
        if p is not None and p.left is None and p.right is None:
            return True
        else:
            return False

    def deleteTree(self):
        self.root = None

    # inOrder traversal
    def inOrder(self):
        if (self.root is not None):
            self._inOrder(self.root)

        def _inOrder(self, node):
            if (node is not None):
                self._inOrder(node.left)
                print(str(node.element), end=' ')
                self._inOrder(node.right)

    # use inOrder traversal to match parentheses
    def parenthesize(self):
        if self.root is not None:
            return self._parenthesize_recur(self.root)

    def _parenthesize_recur(self, p):
        if self.is_leaf(p):
            print(p.element, end='')
        else:
            print('(', end='')
            self._parenthesize_recur(p.left)
            print(p.element, end='')
            self._parenthesize_recur(p.right)
            print(')', end='')


T = BinaryTree()
T.addroot('+')
print(T.is_root(T.getRoot()))
x = T.addleft(T.getRoot(), '3')
y = T.addright(T.getRoot(), '*')
T.addright(y, '2')
z = T.addleft(y, '+')
T.addleft(z, '5')
T.addright(z, '9')
for x in T:
    print(x)
T.parenthesize()
print()
print(T.depth(y))
