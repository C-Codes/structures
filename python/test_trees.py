#!/usr/bin/env python

from binary_tree import BinaryTree

def test_binary_tree(N):
    t = BinaryTree()
    for i in range(int(N/2)):
        t.append_left(i)
    for i in range(int(N/2)):
        t.append_right(int(N/2)+i)
    print_tree(t.root)

def print_tree(n, level=0):
    if n is None:
        return(' ')

    print(n.data)
    print('| \\')
    print(print_tree(n.left) + ' ' + print_tree(n.right))


if __name__ == "__main__":
    test_binary_tree(N=10)
