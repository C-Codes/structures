class BinaryNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def append_left(self, data):
        if self.left is None:
            self.left = BinaryNode(data)
        else:
            self.left.append_left(data)

    def append_right(self, data):
        if self.right is None:
            self.right = BinaryNode(data)
        else:
            self.right.append_right(data)

class BinaryTree:
    def __init__(self):
        self.root = None

    def empty(self):
        return self.root is None

    def append_left(self, data):
        if self.empty():
            self.root = BinaryNode(data)
            return
        self.root.append_left(data)

    def append_right(self, data):
        if self.empty():
            self.root = BinaryNode(data)
            return
        self.root.append_right(data)
