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

    # this isn't really something you will want to do very often ...
    def append(self, data):
        new_end = Node(data)
        if self.empty():
            self.start = new_end
            return
        _head = self.start
        while _head.next is not None:
            _head = _head.next
        _head.next = new_end

    def remove_start(self):
        # remove a node from the start of the linked list
        if self.empty():
            raise Exception
        data = self.start.data
        self.start = self.start.next
        return data

    def remove_end(self):
        # remove a node from the end of the linked list
        if self.empty():
            raise Exception
        _head = self.start
        if _head.next is None:
            # only a single element in list - remove it
            data = _head.data
            self.start = None
            return data
        # more than one element in list - look 2 nexts ahead
        while _head.next.next is not None:
            _head = _head.next
        data = _head.next.data
        _head.next = None
        return data

    def empty(self):
        if self.start is None:
            return True
        return False
