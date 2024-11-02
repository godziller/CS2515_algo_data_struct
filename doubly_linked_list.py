class Node(object):
    def __init__(self, element, prev, next):
        self._element = element
        self._next = next
        self._prev = prev

    def get_item(self):
        return self._element

    def set_item(self, item):
        self._element = item

    def get_next(self):
        return self._next

    def set_next(self, node):
        self._next = node

    def get_prev(self):
        return self._prev

    def set_prev(self, node):
        self._prev = node


class DoublyLinkedList(object):
    def __init__(self):
        self._count = 0
        self._head = Node(None, None, None)
        self._tail = Node(None, None, self._head)
        self._head._next = self._tail
        self._cursor = self._head

    def length(self):
        return self._count

    def get_first(self):
        return self._head.get_next()

    def get_last(self):
        return self._tail.get_prev()

    def add_after(self, element, in_node):
        next_node = in_node.get_next()
        new_node = Node(element,in_node, next_node)
        in_node.set_next(new_node)
        next_node.set_prev(new_node)
        self._count += 1

    def add_before(self, element, in_node):

        prev_node = in_node.get_prev()
        new_node = Node(element, in_node, prev_node)
        in_node.set_prev(new_node)
        prev_node.set_next(new_node)
        self._count += 1


    def get_after(self, node):
        return node.get_after()

    def get_before(self, node):
        return node.get_prev()

    def add_first(self, element):
        self.add_after(element, self._head)


    def add_last(self, element):
        self.add_before(element, self._tail)

    def remove(self, node):
        before = node.get_prev()
        after = node.get_after()
        before.set_next(after)
        after.set_prev(before)
        node.set_next(None)
        node.set_prev(None)
        self._count -= 1
        self._cursor = before

    def remove_first(self):
        self.remove(self._head.get_next())
    def remove_last(self):
        self.remove(self._tail.get_prev())

if __name__ == "__main__":
    myDLL = DoublyLinkedList()
    print(myDLL._count)
    myDLL.add_first('Orangutan')
    print(myDLL._count)
    myDLL.add_first('Chimp')
    myDLL.add_first('Gorilla')
    print(myDLL._count)
    myDLL.add_last('Macau')
    print(myDLL._count)
    print(myDLL.get_first().get_item())
    print(myDLL.get_last().get_item())