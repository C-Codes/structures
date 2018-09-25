class Item:
    def __init__(self, _data=None):
        self.data = _data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def pop(self):
        data = self.peek()
        self.top = self.top.next
        return data

    def peek(self):
        if self.empty():
            raise Exception
        return self.top.data

    def push(self, data):
        item = Item(data)
        cur = self.top
        self.top = item
        self.top.next = cur

    def empty(self):
        if self.top is None:
            return True
        return False


def test_stack():
    print("Testing stack")
    s = Stack()
    N = 100

    print("Check if empty")
    print(s.empty())

    print(f"Pushing {N} values")
    for i in range(N):
        s.push(i)
    print("Peeking top value")
    print(s.peek())
    print("Poping values")
    for i in range(N):
        print(s.pop())
    print("Stack should now be empty")
    try:
        s.pop()
    except Exception:
        print("Got expected Exception")

if __name__ == "__main__":
    test_stack()
