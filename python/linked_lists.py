class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.start = None

    def prepend(self, data):
        new_start = Node(data)
        new_start.next = self.start
        self.start = new_start

    def append(self, data):
        new_end = Node(data)
        if self.empty():
            self.start = new_end
            return
        _head = self.start
        while _head.next is not None:
            _head = _head.next
        _head.next = new_end

    def empty(self):
        if self.start is None:
            return True
        return False
