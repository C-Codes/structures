from queue import Queue
#from timing import timerfunc
# @timerfunc
def test_queue(N):
    print("Testing queue")
    q = Queue()

    print("Check if empty")
    print(q.empty())

    print(f"Adding {N} values")
    [q.add(i) for i in range(N)]

    print("")
    print("Peeking front value")
    print(q.peek())
    print("Removing values")
    [q.remove() for i in range(int(N/2)-1)]
    print("Mid-value:")
    print(q.remove())
    [q.remove() for i in range(int(N/2))]
    print("Queue should now be empty")
    try:
        q.remove()
    except Exception:
        print("Got expected Exception")

if __name__ == "__main__":
    test_queue(N=1000000)
