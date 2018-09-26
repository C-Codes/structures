class Item:
    def __init__(self, _data=None):
        self.data = _data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.back = None

    def add(self, data):
        item = Item(data)
        if self.back is not None:
            self.back.next = item
        self.back = item
        if self.front is None:
            self.front = self.back

    def remove(self):
        data = self.peek()
        self.front = self.front.next
        if self.empty():
            self.back = None
        return data

    def peek(self):
        if self.empty():
            raise Exception
        return self.front.data

    def empty(self):
        if self.front is None:
            return True
        return False
