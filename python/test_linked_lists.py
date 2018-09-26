from singly_linked_list import SinglyLinkedList
from doubly_linked_list import DoublyLinkedList

def test_singly_linked_list_prepend(N):
    print("Testing SinglyLinkedList")
    l = SinglyLinkedList()

    print(f"Prepending {int(N)} values")
    [l.prepend(i) for i in range(int(N))]

def test_singly_linked_list_append(N):
    print("Testing SinglyLinkedList")
    l = SinglyLinkedList()

    print(f"Appending {int(N)} values")
    [l.append(i) for i in range(int(N))]

def test_singly_linked_list_remove_start(N):
    print("Testing SinglyLinkedList")
    l = SinglyLinkedList()

    print(f"Prepending {int(N)} values")
    [l.prepend(i) for i in range(int(N))]
    print(f"Removing {int(N)} values from the start")
    [l.remove_start() for i in range(int(N))]
    try:
        l.remove_start()
    except Exception:
        print("Got expected Exception")

def test_singly_linked_list_remove_end(N):
    print("Testing SinglyLinkedList")
    l = SinglyLinkedList()

    print(f"Prepending {int(N)} values")
    [l.prepend(i) for i in range(int(N))]
    print(f"Removing {int(N)} values from the end")
    [l.remove_end() for i in range(int(N))]
    try:
        l.remove_end()
    except Exception:
        print("Got expected Exception")


def test_doubly_linked_list_prepend(N):
    print("Testing DoublyLinkedList")
    l = DoublyLinkedList()

    print(f"Prepending {int(N)} values")
    [l.prepend(i) for i in range(int(N))]

def test_doubly_linked_list_append(N):
    print("Testing DoublyLinkedList")
    l = DoublyLinkedList()

    print(f"Appending {int(N)} values")
    [l.append(i) for i in range(int(N))]

def test_doubly_linked_list_remove_start(N):
    print("Testing DoublyLinkedList")
    l = DoublyLinkedList()

    print(f"Prepending {int(N)} values")
    [l.prepend(i) for i in range(int(N))]
    print(f"Removing {int(N)-10} values from the start")
    [l.remove_start() for i in range(int(N)-10)]
    try:
        l.remove_start()
    except Exception:
        print("Got expected Exception")
    # print_linked_list(l)

def test_doubly_linked_list_remove_end(N):
    print("Testing DoublyLinkedList")
    l = DoublyLinkedList()

    print(f"Appending {int(N)} values")
    [l.append(i) for i in range(int(N))]
    print(f"Removing {int(N)-10} values from the end")
    [l.remove_end() for i in range(int(N)-10)]
    try:
        l.remove_end()
    except Exception:
        print("Got expected Exception")
    # print_linked_list(l)

def print_linked_list(l):
    print("Print list:")
    _head = l.start
    while (_head is not None):
        print(_head.data)
        _head = _head.next

if __name__ == "__main__":
    # test_singly_linked_list_prepend(N=1000000)
    # test_singly_linked_list_append(N=10000)
    # test_singly_linked_list_remove_start(N=1000000)
    # test_singly_linked_list_remove_end(N=10000)
    # test_doubly_linked_list_prepend(N=1000000)
    # test_doubly_linked_list_prepend(N=1000000)
    # test_doubly_linked_list_append(N=1000000)
    # test_doubly_linked_list_remove_start(N=1000000)
    test_doubly_linked_list_remove_end(N=1000000)
