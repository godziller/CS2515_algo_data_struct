""" Sample solutions to Lab on Python Lists for CS2515.

"""

from time import perf_counter
from operator import attrgetter

import random


class Station:
    """ A class to represent a Garda Station's crime stats for 2016. """

    def __init__(self, data):
        self.name = data[0]
        self.district = data[1]
        self.count = int(data[2])

    def __str__(self):
        retstr = ""
        return "(" + self.name + "," + self.district + "," + str(self.count) + ")"

    def __lt__(self, other):
        """ Return true if this stations name is before other's.

        Args:
            other - an instance of Station
        """
        if self.name < other.name:
            return True
        return False

    # def __lte__(self, other):
    #     """ Return true if this stations name is before or equal to other's.

    #     Args:
    #         other - an instance of Station
    #     """
    #     if self < other or self.name == other.name:
    #         return True
    #     return False

    def __eq__(self, other):
        """ Return True if self and other represent the same Garda Station.

        Args:
            other - an instance of Station

        Note that for other applications there might be multiple entries for the
        same station (e.g. crime stats for different years) and so we would want to define
        a different rule for equality - e.g. same name, same district and same year)
        """
        if self.name == other.name:
            return True
        return False


def read_garda_stations():
    """ Read and return a list of garda stations.

    Returns a list of object instances of the Station class.
    """
    all_stations = []
    file = open('garda_stations.txt', 'r', encoding="utf-8")
    for line in file:
        line = line.replace('\n', '')
        new_tuple = tuple(line.split('\t'))
        new_station = Station(new_tuple)
        all_stations.append(new_station)
    file.close()
    return all_stations


def linear_search_field(mylist, field, target):
    """ Execute a linear search in mylist for object with <field> == target.

    Args:
        field - the name of the field to be matched
        mylist: a list of objects

    Return the index of first item with <field> matching target, or -1 if not in the list.
    """
    f = attrgetter(field)
    pos = 0
    while pos < len(mylist):
        if f(mylist[pos]) == target:
            return pos
        pos += 1
    return -1


def linear_search(mylist, target):
    """ Execute a linear search in mylist for object with name == target.

    Args:
        mylist: a list of objects

    Return the index of first item with name matching target, or -1 if not in the list.
    """
    pos = 0
    while pos < len(mylist):
        if mylist[pos].name == target:
            return pos
        pos += 1
    return -1


def binary_search(mylist, target):
    """ Execute a binary search for target in mylist.

    Args:
        mylist: a list of objects

    Return the index of first item matching target, or -1 if not in the list.
    """
    if len(mylist) < 1:
        return -1
    found = False
    low = 0
    upp = len(mylist) - 1
    while low <= upp and not found:
        mid = (low + upp) // 2
        if mylist[mid].name == target:  # Note: searching for content in pos 0
            return mid
        else:
            if target < mylist[mid].name:  # Note: searching for content in pos 0
                upp = mid - 1
            else:
                low = mid + 1
    return -1


def binary_search_field(mylist, field, target):
    """ Execute a binary search of myList for object where <field> matches  target.

    Args:
        field: the name of the field to be used
        mylist: a list of objects

    Return the index of first item with <field>==target, or -1 if not in the list.
    """
    f = attrgetter(field)
    if len(mylist) < 1:
        return -1
    found = False
    low = 0
    upp = len(mylist) - 1
    while low <= upp and not found:
        mid = (low + upp) // 2
        if f(mylist[mid]) == target:  # Note: searching for content in pos 0
            return mid
        else:
            if target < f(mylist[mid]):  # Note: searching for content in pos 0
                upp = mid - 1
            else:
                low = mid + 1
    return -1


def perf_check_call(func, *args):
    """ Run func on *args, and print the performance statistics.

    Args:
        func is the identifier of a defined function
        *args is an arbitrary number of comma-separated input arguments,
              which much match the signature of the function
    """
    start_time = perf_counter()
    result = func(*args)  # Note: func must accept the arguments in *args sequence
    end_time = perf_counter()
    print('%f seconds' % (end_time - start_time))


def dummy_func(input1, input2, input3, input4):
    """ Dummy function to illustrate perf_check_call syntax. """
    return input1 + input2 + input3 + input4


"""
Two examples of execution of perf_check_call.
Note that the first has three inputs, since the function linear_search requires
two input arguments, while the second has 5 inputs, since dummy_func requires four
input arguments.

perf_check_call(linear_search, [(0,9),(1,7),(2,8),(3,6),(4,9)], 3)
perf_check_call(dummy_func, 4, 5, 6, 7)
"""


def grow_by_append(size):
    """ Grow a list by successive appends.

    Args:
        size (int) is the length of the final list
     """
    thelist = []
    for i in range(size):
        thelist.append(i)


def grow_by_insert0(size):
    """ Grow a list by successive insertions in position 0.

    Args:
        size (int) is the length of the final list
     """
    thelist = []
    for i in range(size):
        thelist.insert(0, i)


def growth_cost(size):
    """ Compare the cost of growing a list by append or insert(0,x).

    Args:
        size (int) is the length of the final list
     """
    print('Runtime to append %d integers (at end)   :' % size, end=" ")
    perf_check_call(grow_by_append, size)
    print('Runtime to insert %d integers into cell 0:' % size, end=" ")
    perf_check_call(grow_by_insert0, size)


def shrink_by_pop(size):
    """ Shrink a list by successive pop() calls.

    Args:
        size (int) is the length of the initial list
     """
    thelist = [1] * size
    for i in range(size):
        thelist.pop()


def shrink_by_pop0(size):
    """ Shrink a list by successive pop(0) calls.

    Args:
        size (int) is the length of the initial list
     """
    thelist = [1] * size
    for i in range(size):
        thelist.pop(0)


def shrink_cost(size):
    """ Compare the cost of shrinking a list by pop() or pop(0).

    Args:
        size (int) is the length of the initial list
     """
    print('Runtime to pop %d integers from end      :' % size, end=" ")
    perf_check_call(shrink_by_pop, size)
    print('Runtime to pop %d integers from beginning:' % size, end=" ")
    perf_check_call(shrink_by_pop0, size)


# for lists of length different of powers of 10, compare the cost of different ways to grow a list
for power in range(6):
    growth_cost(pow(10, power))
    print(" ")

# for lists of length different of powers of 10, compare the cost of different ways to shrink the list
for power in range(6):
    shrink_cost(pow(10, power))
    print(" ")

allstations = read_garda_stations()
for station in allstations:
    print(station)
index = linear_search(allstations, "Bridewell Cork")
print('Found: ' + str(allstations[index]))
index = binary_search(allstations, "Bridewell Cork")
print('Found: ' + str(allstations[index]))
index = linear_search_field(allstations, "name", "Bridewell Cork")
print('Found: ' + str(allstations[index]))
index = binary_search_field(allstations, "name", "Bridewell Cork")
print('Found: ' + str(allstations[index]))
allstations.sort(key=lambda x: x.count)
for station in allstations:
    print(station)
