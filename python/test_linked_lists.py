from linked_lists import SinglyLinkedList

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

def print_linked_list(l):
    print("Print list:")
    _head = l.start
    while (_head is not None):
        print(_head.data)
        _head = _head.next

if __name__ == "__main__":
    test_singly_linked_list_prepend(N=1000000)
    test_singly_linked_list_append(N=10000)
