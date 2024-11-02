from operator import index


class Element:
    def __init__(self, key, item):
        self._key = key
        self._item = item
        self._hashcode = abs(hash(self._key))

    def __eq__(self, other):
        if self._key == other._key:
            return True
        else:
            return False

class Map(object):
    def __init__(self):
        self._maxsize = 10
        self._length = 0
        self._list = list()
        for index in range(0,self._maxsize):
            self._list.append(None)


    def length(self):
        ...
    def setitem(self, key, value):
        new_item = Element(key,value)
        print(new_item._hashcode)
        index = new_item._hashcode % self._maxsize

        if self._list[index] == None:
            self._list[index] == new_item


    def delitem(self, key):
        ...
    def getitem(self, key):
        ...

if __name__ == "__main__":
    my_map = Map()
    my_map.setitem('Monkey', 'Orangutan')
    my_map.setitem('Big Cat', 'Tiger')
