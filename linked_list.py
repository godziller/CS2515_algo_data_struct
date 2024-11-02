
class Node(object):
    def __init__(self, element, next):
        self._element = element
        self._next = next

    def get_element(self):
        return self._element

    def get_next(self):
        return self._next

    def set_next(self,node):
        self._next = node

class LinkedList(object):
    def __init__(self):
        self._count = 0
        self._head = None
        self._tail = None


    def length(self):
        return self._count

    def add_first(self, element):
        new_node = Node(element, self._head)
        self._head = new_node
        if self._count == 0: # first Node coming in
            self._tail = new_node
        self._count += 1

    def get_first(self):
        return self._head.get_element()

    def remove_first(self):
        if self._count != 0:
            temp_element = self._head.get_element()
            self._head = self._head.get_next()
            self._count -= 1
            return temp_element
        else:
            return None
    def get_last(self):
        return self._tail.get_element()

    # removes the last node for a SLL and returns it to the caller
    def remove_last(self) -> object:
        ...
    # add an element to the last/tail of the SLL
    def add_last(self, element) -> None:
        if self._count == 0: # adding to tail of empty list
            self.add_first(element)
        else:
            myNode = Node(element, None)
            self._tail.set_next(myNode)
            self._tail = myNode
            self._count += 1


    # return the elment from the SLL but does not remove it.
    def get_last(self) -> object:
        ...
if __name__ == '__main__':
    myLinkedList = LinkedList()
    print(myLinkedList.length())
    myLinkedList.add_first('Orangutan')
    myLinkedList.add_first('Chimp')
    myLinkedList.add_first('Capuchin')
    myLinkedList.add_first('Spider monkey')

    print(myLinkedList.length())

    print(myLinkedList.remove_first())
    print(myLinkedList.remove_first())
    print(myLinkedList.remove_first())
    print(myLinkedList.remove_first())

    print(myLinkedList.length())
