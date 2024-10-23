""" Class definition for an array-based implementation of the Stack ADT.

For invalid method calls, does not throw exceptions. Instead, returns
None if a return value is expected, and otherwise ignores the request.

"""


class Stack:
    """ An array-based stack. """

    def __init__(self):
        self.alist = []      # alist should only be accessed using the
                             # methods defined in this class.

    def __str__(self):
        """ Display a stack as a string, by listing elements in sequence.

            |- denotes the bottom of the stack
            -> denotes the top of the stack.
            So '|-x-y-z-> denotes a stack with 3 elements, and z at the top.

        Normally, a method giving this level of detail in the string would not
        be provided - users of the class are only supposed to see the size
        of the stack and the top element. It is provided here so that we can
        use it for debugging and evaluation.
        """
        retstr = '|-'
        for element in self.alist:
            retstr = retstr + str(element) + '-'
        retstr = retstr + '->'
        return retstr

    def pop(self):
        """ Remove and return the top element of the stack. """
        if len(self.alist) == 0:
            return None
        return self.alist.pop()  # the 'top' element is the last in the in the list

    def push(self, element):
        """ Place element onto the top of the stack. """
        self.alist.append(element)  # the 'top' is the last in the list

    def top(self):
        """ Return but don't remove the top element of the stack. """
        if len(self.alist) == 0:
            return None
        return self.alist[-1]  # i.e. report the last element
    
    def length(self):
        """ Return the number of elements on the stack. """
        return len(self.alist)


if __name__ == "__main__":
    # Test the basic functionality of the stack. 
    print("testing the Stack list implementation")
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print('stack should be |-1-2-3-->, and is %s' % stack)
    print('stack.length should be 3, and is %d' % stack.length())
    print('stack.top() should be 3, and is %d' % stack.top())
    print('stack.pop() should be 3, and is %d' % stack.pop())
    print('stack should now be |-1-2-->, and is %s' % stack)
    print('stack.length() should be 2, and is %d' % stack.length())
    stack.pop()
    stack.pop()
    print('popped two more items; length() should be 0, and is %d' % stack.length())
    print('stack.top() should be None, and is %s' % stack.top())
    print('stack.pop() should be None, and is %s' % stack.top())
    print('stack should be |-->, and is %s' % stack)
