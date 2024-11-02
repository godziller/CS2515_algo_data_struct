from linked_list import *

class Queue:
    def __init__(self):
        self._list = LinkedList()

    def enqueue(self, element):
        self._list.add_last(element)

    def dequeue(self):
        return self._list.remove_first()

    def front(self):
        return self._list.get_first()

    def length(self):
        return self._list.length()

if __name__ == "__main__":
    myQueue = Queue()
    print(myQueue.length())
    myQueue.enqueue('Orangutan')
    myQueue.enqueue('Bonobo')
    print(myQueue.length())
    print(myQueue.front())
    print(myQueue.dequeue())
    print(myQueue.front())


