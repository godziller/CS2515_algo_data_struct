class Stack(object):
    def __init__(self):
        self._list = []
      #  self._len = 0
        ...

    #0(1~)
    def push(self, element):
        self._list.append(element)

    #0(1)
    def pop(self):
        if len(self._list) != 0:
            return self._list.pop()
        else:
            return "Nothing to pop"
    #0(1)
    def len(self):
        return len(self._list)

    #0(1)
    def top(self):
        if self._list != 0:
            return self._list[-1]
        else:
            return 'Nothing in the q'

    def __str__(self):
        retstr = '|-'
        for element in self._list:
            retstr = retstr + str(element) + '-'
        retstr = retstr + '->'
        return retstr

if __name__ == "__main__":
    myStack = Stack()
    myString1 = 'Orangutan'
    myStack.push(myString1)

    myString2 = 'Chimpanzee'
    myStack.push(myString2)

    myString3 = 1
    myStack.push(myString3)
    print(myStack)

    myString4 = 'Gibbon'
    myStack.push(myString4)

    print(myStack.top())
    myElement = myStack.pop()
    print(myElement)
    print(myStack.top())

    print(myStack.top())
    myElement = myStack.pop()
    print(myElement)
    print(myStack.top())