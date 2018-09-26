class Item:
    def __init__(self, _data=None):
        self.data = _data
        self.below = None

class Stack:
    def __init__(self):
        self.top = None

    def pop(self):
        data = self.peek()
        self.top = self.top.below
        return data

    def peek(self):
        if self.empty():
            raise Exception
        return self.top.data

    def push(self, data):
        item = Item(data)
        cur = self.top
        self.top = item
        self.top.below = cur

    def empty(self):
        if self.top is None:
            return True
        return False
