class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.start = None
        self.end = None

    def prepend(self, data):
        new_start = Node(data)
        new_start.next = self.start
        if self.start is not None:
            self.start.prev = new_start
        self.start = new_start
        if self.end is None:
            self.end = self.start
            self.end.prev = self.start

    # this isn't really something you will want to do very often ...
    def append(self, data):
        new_end = Node(data)
        new_end.prev = self.end
        if self.end is not None:
            self.end.next = new_end
        self.end = new_end
        if self.start is None:
            self.start = self.end
            self.start.next = self.end

    def remove_start(self):
        # remove a node from the start of the linked list
        if self.empty():
            raise Exception
        data = self.start.data
        self.start = self.start.next
        if self.start is None:
            self.end = None
        else:
            self.start.prev = None
        return data

    def remove_end(self):
        # remove a node from the end of the linked list
        if self.empty():
            raise Exception
        data = self.end.data
        self.end = self.end.prev
        if self.end is None:
            self.start = None
        else:
            self.end.next = None
        return data

    def empty(self):
        if self.start is None:
            return True
        return False
