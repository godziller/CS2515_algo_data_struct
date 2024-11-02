
class Element:
    """ Represents an element with a key and value. """
    
    def __init__(self, k, v):
        """ Create an element with given key k and value v.

            The key must be an immutable type.
        """
        self._key = k
        self._value = v

    def __eq__(self, other):
        """ Return True if this element's key equals other's key. """
        return self._key == other._key

    def __lt__(self, other):
        """ Return True if this element's key is less than other's key. """
        return self._key < other._key

    def _wipe(self):
        """ Set the instance variables to None. """
        self._key = None
        self._value = None


class HashMapV1:
    """ An implementation of a simple Hash Map.

        Maintains a fixed length list of positions, and each position stores an
        unsorted list of elements.
    """

    def __init__(self, sz = 10):
        """ Create an empty Hash Table with size sz.

        If no sz parameter is given, it will create a table of length 10.

        Args:
            sz - the (int) size of the underlying list
        """
        self._map = [None] * sz   # the container for the items - a list of None references
        for i in range(len(self._map)):
            self._map[i] = []     # initialise all cells to the empty list 
        self._size = 0            # the number of elements in the map
        # Initialising every cell to an empty bucket is not the best use of space, and
        # may be a little slower (since we have to create the empty lists), but it is easier to
        # code, since we know there is always a list in each cell.


    def __str__(self):
        """ Return a string representation of the Hash Table. """
        outstr = 'size = ' + str(self._size) + '\n'
        for alist in self._map:
            if alist is not None:
                for elt in alist:
                    outstr += '(' + str(self._comphash(elt._key)) + ') '
                    outstr += str(elt._key) + ' : ' + str(elt._value) + '\n'
        return outstr

    def getitem(self, key):
        """ Return the value with a given key, or None if key not in Map.

        Args:
            key - the lookup key for the search (must be immutable).
        """
        #  method body goes here


    def setitem(self, key, value):
        """ Assign value to elt with key; create new elt if needed.

        Args:
            key - the lookup key
            value - the item to be added for (or reassigned to) that key
        """
        #  method body goes here



    def delitem(self, key):
        """ Remove element and return value of elt with key if exists.

            Returns None if no such elt is in Map.

        Args:
            key - the lookup key to be deleted.
        """
        # method body goes here

    def length(self):
        """ Return the number of items in the map. """
        # method body goes here

    def _comphash(self, key):
        """ Turn an immutable type into a location in this hash map. 
        
        Note: method does both hash and compression ...
        Note: it has to be based on the current length of the list,
        since we are compressing to find a cell in the current list.
        """
        return hash(key) % len(self._map)
        # Not strictly needed as a separate method - could just call hash in 
        # the appropriate places in the methods above - BUT all 4 methods must 
        # use exactly the same hash and compression methods, so it is safer to 
        # have each one call this method, and to implement the consistent 
        # behaviour here. Then, when you want to change to a different hash or 
        # compression method, you only have to change it in one place.


def test(mymap):
    """ Test an implementation of a Hash Map.

    Args:
        mymap - an implementation of a Hash Map.

    The Hash map must provide the following methods:
        setitem(key,value)
        getitem(key) - return the item with given key, if in map; else return None
        delitem(key) - return the value assocaited with given key, and delete from map; else return None
    """
    print()
    mymap.setitem('CS1106', 'Introduction to Relational Databases')
    mymap.setitem('CS1110', 'Systems Organisation I')
    mymap.setitem('CS1111', 'Systems Organisation II')
    mymap.setitem('CS1112', 'Foundations of Computer Science I')
    mymap.setitem('CS1113', 'Foundations of Computer Science II')
    mymap.setitem('CS1115', 'Web Development 1')
    mymap.setitem('CS1116', 'Web Development 2')
    mymap.setitem('CS1117', 'Introduction to Programming')
    mymap.setitem('CS2051', 'Introduction to Digital Media')
    mymap.setitem('CS2052', 'Introduction to Internet Information Systems')
    mymap.setitem('CS2501', 'Database Design and Administration')
    mymap.setitem('CS2502', 'Logic Design')
    mymap.setitem('CS2503', 'Operating Systems 1')
    mymap.setitem('CS2505', 'Network Computing')
    mymap.setitem('CS2506', 'Operating Systems II')
    mymap.setitem('CS2507', 'Computer Architecture')
    mymap.setitem('CS2508', 'Computer Animation')
    mymap.setitem('CS2509', 'XML and the Extended Enterprise')
    mymap.setitem('CS2510', 'Web Servers')
    mymap.setitem('CS2511', 'Usability Engineering')
    mymap.setitem('CS2512', 'Authoring')
    mymap.setitem('CS2513', 'Intermediate Programming')
    mymap.setitem('CS2514', 'Introduction to Java')
    mymap.setitem('CS2515', 'Algorithms and Data Structures I')
    mymap.setitem('CS2516', 'Algorithms and Data Structures II')
    print('Book of Modules for 1st and 2nd year Computer Science')
    print(mymap)
    print('CS BoM contains CS2515 (display CS2515)?', str(mymap.getitem('CS2515')))
    print('CS BoM contains CS2504 (display None)?', str(mymap.getitem('CS2504')))
    print('CS2515 has title (A&DS I):', mymap.getitem('CS2515'))
    print('CS2504 has title (None):', mymap.getitem('CS2504'))
    print('Add new module CS2599:Facebook (None):', mymap.setitem('CS2599', 'Facebook'))
    print('CS2599 has title (Facebook):', mymap.getitem('CS2599'))
    print('Book of Modules for 1st and 2nd year Computer Science')
    print(mymap)
    print('Change title of CS2599 to Death of Twitter (None):', mymap.setitem('CS2599', 'Death of Twitter'))
    print('CS2599 has title (Death of Twitter):', mymap.getitem('CS2599'))
    print('Removing CS1113 (FoCSII):', mymap.delitem('CS1113'))
    print('CS BoM contains CS1113 (None)?', str(mymap.getitem('CS1113')))
    print('Book of Modules for 1st and 2nd year Computer Science')
    print(mymap)

sz = 10
print("-------------------------------------------")
print("Simple static bucket array hash map")
print("Number in brackets is the cell of the top-level list")
test(HashMapV1(sz))
