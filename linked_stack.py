from linked_list import *

class Stack:
    def __init__(self):
        self._list = LinkedList()

    #0(1)
    def push(self, element):
        self._list.add_first(element)

    #0(1)
    def pop(self):
        if self._list.length() != 0:
            return self._list.remove_first()
        else:
            return None

    #0(1)
    def top(self):
        if self._list.length() != 0:
            return self._list.get_first()
        else:
             return None

    #0(1)
    def len(self):
        return self._list.length()

if __name__ == "__main__":
    my_linked_stack = Stack()
    my_linked_stack.push('Orangutan')
    print(my_linked_stack.len())
    print(my_linked_stack.pop())
    print(my_linked_stack.len())
