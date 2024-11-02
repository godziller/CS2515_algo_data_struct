""" Sample functions for comparing the performance of basic list operations.

"""
import sys
import time
import math


def list_size():
    """ Compare the in-memory sizes of two lists.

    The lists have the same number of objects, but the objects in the second
    list are much bigger.

    The function shows that the in-memory size is determined by the number of
    references, and not by the objects themselves
    """

    mylist = []
    biglist = []
    for i in range(1000):
        mylist.append(1)
        biglist.append((1,2,3,4,5,6,7,8,9,10))
    print('List of', len(mylist), 'ints occupies', sys.getsizeof(mylist), 'bytes')
    print('List of', len(mylist), 'tuples of 10 ints occupies', sys.getsizeof(biglist), 'bytes')

def dynamic_size():
    """ Report the internal size of a list as it grows using append.

    This illustrates that python extends the reserved size in chunks, and then
    fills up each chunk before growing the list again.
    """
    print("The reserved size for a list as it grows by successive appends")
    mylist = []
    for pos in range(120):
        print('List of length', len(mylist), 'takes size (bytes)', sys.getsizeof(mylist))
        mylist.append(1)
   
def cost_of_append_time(value):
    """ Report the time taken to grow a list by successive appends.

    Args:
        value - the (int) number of items to be added to the list.
    """

    mylist = []
    starttime = time.process_time()
    for i in range(value):
        mylist.append(1)
    endtime = time.process_time()
    print((endtime-starttime))

def cost_of_append_perf(value):
    """ Report the system time taken to grow a list by successive appends.

    Args:
        value - the (int) number of items to be appended to the list.
    """

    mylist = []
    starttime = time.perf_counter()
    for i in range(value):
        mylist.append(1)
    endtime = time.perf_counter()
    runtime = endtime - starttime
    print(f'{value:9}: {runtime:1.8f}')

def cost_of_append():
    """Report the the growth in system time for appends as list size grows.
    """

    print("Runtime to create lists of given size by successive appends")
    i = 1
    while i < 100000001:
        cost_of_append_perf(i)
        i = i*10



def size_of_popped_list():
    """ Report the changes in reserved size of a list during deletions. """

    print("Changes in reserved size of list by popping an internal item")
    mylist = []
    for pos in range(65):
        mylist.append(1)
    print('List of length', len(mylist), 'takes size (bytes)', sys.getsizeof(mylist))
    for i in range(40):
        mylist.pop(10)
        print('List of length', len(mylist), 'takes size (bytes)', sys.getsizeof(mylist))


list_size()
dynamic_size()
cost_of_append()
size_of_popped_list()