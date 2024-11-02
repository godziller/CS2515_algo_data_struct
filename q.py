
class Queue(object):
    def __init__(self):
        self._list = list()


    #0(1), not accessing/doing anything to any elements in the queue, simply placing and end
    def enqueue(self, element):
        self._list.append(element)

    #0(n)
    def dequeue(self):
        if len(self._list) != 0:
            return self._list.pop(0)
        else:
            return "Empty"

    #0(1)
    def top(self):
        if len(self._list) != 0:
            return self._list[0]
        else:
            return 'Empty'

    #0(1)
    def length(self):
        return len(self._list)


class QueueV2(object):
    def __init__(self):
        self._list = list()
        self._top = 0

    def enqueue(self, element):
        self._list.append(element)

    def dequeue(self):
        element = self._list[self._top]
        self._top += 1
        return element

    def top(self):
        if len(self._list) != self._top :
            return self._list[self._top]
        else:
            return 'Empty'
    #0(1)
    def length(self):
        return len(self._list) - self._top     # gives us n

if __name__ == "__main__":
    myQueue = Queue()
    print(myQueue.dequeue())
    print(myQueue.top())
    print(myQueue.length())
    myQueue.enqueue('ABC')
    print(myQueue.length())
    print(myQueue.top())
    print(myQueue.dequeue())
    print(myQueue.length())