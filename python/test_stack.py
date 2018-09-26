from stack import Stack
#from timing import timerfunc
# @timerfunc
def test_stack(N):
    print("Testing stack")
    s = Stack()

    print("Check if empty")
    print(s.empty())

    print(f"Pushing {N} values")
    [s.push(i) for i in range(N)]

    print("")
    print("Peeking top value")
    print(s.peek())
    print("Poping values")
    [s.pop() for i in range(int(N/2)-1)]
    print("Mid-value:")
    print(s.pop())
    [s.pop() for i in range(int(N/2))]
    print("Stack should now be empty")
    try:
        s.pop()
    except Exception:
        print("Got expected Exception")

if __name__ == "__main__":
    test_stack(N=1000000)
