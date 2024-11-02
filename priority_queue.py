

class Element(object):
    def __init__(self, priority, item):
        self._priority = int(priority)
        self._element = item

    #0(1)
    def __gt__(self, other):
        if self._priority > other._priority:
            return True
        else:
            return False

    #0(1)
    def __lt__(self, other):
        if self._priority < other._priority:
            return True
        else:
            return False

class PriorityQueue(object):
    def __init__(self):
        self._list = list()
        self._length = 0

        ...
    #something that can add to priorities as clumps
    #groups of prios stay together

    #0(n)
    def add(self, priority, item):
        new_element = Element(priority, item)
        if len(self._list) == 0:
            self._list.append(new_element)
        else:
            for elem in self._list:
                if elem > new_element:
                    index = self._list.index(elem)
                    self._list.insert(index, new_element)
                    break

    #0(1)
    def remove_min(self):
        #item = self._list[0]._element
        return self._list.pop(0)._element
       # return item

    #0(1)
    def min(self):
        return self._list[0]._element

    #0(1)
    def length(self):
        return len(self._list)


if __name__ == "__main__":
    myPQ = PriorityQueue()
    myPQ.add(4,'Orangutan')
    print(myPQ.min())
    myPQ.add(2, 'Gorrilla')
    print(myPQ.min())
    myPQ.add(3, 'Monkey')
    myPQ.add(1, 'Human')
    print(myPQ.min())
    print(myPQ.length())
    print(myPQ.remove_min())
    print(myPQ.length())