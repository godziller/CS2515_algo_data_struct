from doubly_linked_list import *


class ListADT(object):
    def __init__(self):
        self._list = DoublyLinkedList()

    def get_current(self):
        return self._list._cursor.get_item()

    def add_current_item(self, item):
        self._list.add_after(item ,self._list._cursor)



    def replace_current(self, item):
        self._list._cursor.set_item(item)

    def remove_item(self):
        self._list.remove(self._list._cursor)

    def next(self):
        self._list._cursor = self._list._cursor.get_next()

    def prev(self):
        self._list._cursor = self._list._cursor.get_prev()

    def move_to_front(self):
        self._list._cursor = self._list.get_first()

    def move_to_last(self):
        self._list._cursor = self._list.get_last()

    def has_next(self):
        if self._list._cursor.get_next().get_item() != None:
            return True
        else:
            return False

    # helper methods.

    def add_first(self, item):
        self._list.add_first(item)

    def add_last(self, item):
        self._list.add_last(item)

    def get_first(self):
        return self._list.get_first()

    def get_last(self):
        return self._list.get_last()

    def remove_first(self):
        self._list.remove_first()

    def remove_last(self):
        self._list.remove_last()

    def replace_first_item(self, item):
        self._list.get_first().set_item(item)

    def replace_last_item(self,item):
        self._list.get_last().set_item(item)

    def remove_first(self):
        self._list.remove_first()
    def remove_last(self):
        self._list.remove_last()
    def find(self, item):


if __name__ == "__main__":
    myList = ListADT()
    myList.add_current_item('Orangutan')
    myList.add_current_item('Capuchin')
    myList.add_current_item('Howler')
    myList.add_current_item('Baboon')
    myList.move_to_front()
    print(myList.get_current())
    myList.next()
    print(myList.get_current())

    myList.next()
    myList.next()
    print(myList.get_current())
    myList.move_to_last()
    print(myList.get_current())
    myList.prev()
    print(myList.get_current())

