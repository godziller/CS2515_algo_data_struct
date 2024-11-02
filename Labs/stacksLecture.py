
""" Example functions using a Stack from the lecture.  

    These functions were left as an exercise in the lecture.
    You should try to write these solutions youself, before looking at this code.

    The idea is to create a stack object, and then use it. You should not be
    accessing the elements of the internal list defined in the Stack class.
    Instead, use push(x), pop() and top() ...
"""

from stackA import *
from card import *

def palindrome_check(string):
    """ Determine whether string is a palindrome, using a stack.    """
    mylist = list(string)
    size = len(mylist)
    mid = size // 2
    even = True
    if size % 2 == 1:
        even = False
    print('Midpoint is %d; it is %s that list length is EVEN.' % (mid, even))
    stack = Stack()
    pos = 0
    while pos < mid:        #push first half of the string onto the stack
        stack.push(mylist[pos])
        pos = pos + 1
    if not even:            # advance past the middle item
        pos = pos + 1
    while pos < len(mylist):  #now pop and compare the two halfs
        print('mylist[%d]=%s; stack.top()=%s' % (pos, mylist[pos], stack.top()))
        if mylist[pos] != stack.pop():
            return False
        pos = pos+1
    return True


def palindrome_check_list(inlist):
    """ Determine whether inlist is a palindrome, using a stack.    """
    size = len(inlist)
    mid = size // 2
    even = True
    if size % 2 == 1:
        even = False
    print('Length: %d; Midpoint: %d; it is %s that list length is EVEN.' % (
                                    len(inlist), mid, even))
    stack = Stack()
    pos = 0
    while pos < mid:
        stack.push(inlist[pos])
        pos = pos + 1
    if not even:
        pos = pos + 1
    while pos < len(inlist):
        print('mylist[%d]=%s; stack.top()=%s' % (pos,inlist[pos],stack.top()))
        #if inlist[pos] != stack.pop():
        #if not inlist[pos] == stack.pop():
        if not inlist[pos].is_equal(stack.pop()):
            return False
        pos = pos+1
    return True

from card import Card

def objlistcheck():
    """ Test the function which checks palindrome lists.

        Create a list of 'Card' objects, and pass that in to palindrome ...
    """

    cardlist = []

    print('Checking an empty list of playing cards, should be True')
    print(palindrome_check_list(cardlist))

    cardlist.append(Card(3,3))
    cardlist.append(Card(1,4))
    cardlist.append(Card(12,2))
    cardlist.append(Card(7,1))
    cardlist.append(Card(12,2))
    cardlist.append(Card(1,4))
    cardlist.append(Card(3,3))

    print()
    print('Checking a list of playing cards for being a palindrome, should be True')
    for card in cardlist:
        print(card, end=",")
    print()
    print(palindrome_check_list(cardlist))

    cardlist[2] = Card(11,2)
    print()
    print('Checking a list of playing cards for being a palindrome, should be False')
    for card in cardlist:
        print(card, end=",")
    print()
    print(palindrome_check_list(cardlist))


def postfix(string):
    """ Evaluate a postfix string, using a stack.

        Elements must be separated by spaces.
    """
    tokenlist = string.split()
    stack = Stack()
    for token in tokenlist:
        if token in ["+", "-", "*", "/"]:
            second = stack.pop()
            first = stack.pop()
            if token == "+":
               stack.push(first + second)
            elif token == "-":
               stack.push(first - second)
            elif token == "*":
               stack.push(first * second)
            else:
               stack.push(first / second)
        else:
            stack.push(int(token))
    return stack.pop()

def postfix_verbose(string):
    """ Evaluate a postfix string, using a stack, and explain it.

        Elements must be separated by spaces.
        Display progress on screen.
    """
    tokenlist = string.split()
    stack = Stack()
    for token in tokenlist:
        print('next token taken from string is %s' % token)
        if token in ["+", "-", "*", "/"]:
            second = stack.pop()
            first = stack.pop()
            print('   Op, so pop twice, and evaluate %s %s %s' % (
                                                 first, token, second))
            if token == "+":
                print('    = %f' % (first + second))
                stack.push(first + second)
            elif token == "-":
                print('    = %f' % (first - second))
                stack.push(first - second)
            elif token == "*":
                print('    = %f' % (first * second))
                stack.push(first * second)
            else:
                print('    = %f' % (first / second))
                stack.push(first / second)
            print('   and push back onto stack')
        else:
            print('   Value (=%s) so push onto stack'% token)
            stack.push(int(token))
        print('Stack is now: %s' % stack)
    print('No tokens left, so pop from stack (of length 1): %s' % stack)
    return stack.pop()


if __name__ == '__main__':
    objlistcheck()
    print()
    str = '3 4 + 5 *'
    value = 35
    print('Check postfix %s, should be %d' % (str, value))
    print(postfix(str))
    str = '3 4 5 + *'
    value = 27
    print('Check postfix %s, should be %d' % (str, value))
    print(postfix(str))
    print('Repeated check of %s, showing steps' % str)
    print(postfix_verbose(str))