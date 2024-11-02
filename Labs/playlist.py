""" Classes to implement a (simulated) playlist.

Note that the songs, etc. exist as independent objects, stored
elsewhere in the system. What we are doing with Playlist is linking them
together so that we can recall them and browse them.

For this to work in a single programming exercise, we are including the
definition of the Song class, and in the test methods we may create some
new song instances.

For CS2515 labs on DoublyLinked Lists

"""


class Song:
    """ A song in a music library. """

    def __init__(self, i_title, i_artist, i_year, i_seconds):
        """ Create a new Song.

        Args:
             i_title: the (string) title of the song
             i_artist: the (string) name of the artist (or group)
             i_year: the (string) of year it was released
             i_seconds: the (int) length of the song in seconds

        """
        self.title = i_title
        self.artist = i_artist
        self.year = i_year
        self.seconds = i_seconds

    def __str__(self):
        """ Return a short string representation of the song. """
        return (str(self.title) + ", by "
                + str(self.artist))

    def get_info(self):
        """ Return a full string representation of the song. """
        ret_str = ("Title: " + str(self.title) + "; "
                   + "Artist: " + str(self.artist) + "; "
                   + "Year: " + str(self.year) + "; "
                   + "Seconds: " + str(self.seconds) + "; ")
        return ret_str

    def play(self):
        """ Simulate the song being played. """
        print("   Now playing", self)
        print("   ...")
        print("   (", self.seconds, " seconds later ...)")
        print("   silence")

    def _test():
        """ Create some songs and test their methods.

        Note that this does not have the 'self' input argument, and so is a
        class method - that means it is called by Song._test() and not by
        (e.g.) s._test(), where s is some instance of the Song class.
        """
        song_a = Song("Flowers", "Miley Cyrus",
                      2023, 200)
        song_b = Song("Spectrum", "Florence and the Machine",
                      2012, 311)
        song_c = Song("Ghost Town", "The Specials",
                      1981, 219)
        print("song_a is: ", song_a)
        print('song_b info is:', song_b.get_info())
        print("now about to play song_c")
        song_c.play()


# Song._test()


class DLLSongNode:
    """ An internal node in a doubly linked list of Song files.

    Attributes: (all private)
    """

    # _element: the object in this position in the list
    # _next: the next DLLSongNode instance in the list
    # _prev: the previous DLLSongNode instance in the list

    def __init__(self, item, prevnode, nextnode):
        self._element = item
        self._next = nextnode
        self._prev = prevnode


class Playlist:
    """ A song playlist maintained as a doubly linked list of Song objects.

    Attributes: (all private)
    """

    # _head: an empty DLLSongNode to start the list
    # _tail: an empty DLLSongNode to end the list
    # _size: the number of Song instances in the list
    # _current: one node in the list, representing the current selection
    #           This must always refer to a real node in the list (as opposed
    #           to the dummy head or tail nodes), unless the list is empty, in
    #           which case it refers to the dummy head.

    def __init__(self):
        """ Initialise an empty library. """
        self._head = DLLSongNode(None, None, None)  # before the first item
        self._tail = DLLSongNode(None, self._head, None)  # after the last item
        self._head._next = self._tail
        self._size = 0  # an integer
        self._current = self._head  # the node of the currently selected Song

    def __str__(self):
        """ Return a string representation of the list. """
        outstr = "\n$$$ Playlist\n"
        node = self._head._next
        while node != self._tail:
            if self._current == node:
                outstr += "--> "
            else:
                outstr += "    "
            outstr += "(" + str(node._element) + ")\n"
            # can access node's private variable, because defined in this file
            node = node._next
        return outstr + "$$$\n"

    # ---------- Public Methods ------------------------------#

    def add_song(self, Song):
        """ Add Song to the end of the list.

        Args:
            Song: the Song instance to be added

        """
        node = DLLSongNode(Song, None, None)
        self._add_node_after(node, self._tail._prev)
        if self._size == 1:
            self._current = self._head._next

    def get_current(self):
        """ Get the currently selected Song.

        Returns the Song instance.
        """
        return self._current._element

    def next_song(self):
        """ Select the Song after the current one, in current order.
            Wrap around if at the end of the list.
        """
        if self._size > 0:
            if self._current._next == self._tail:
                self._current = self._head
            self._current = self._current._next
        else:
            self._current = self._head

    def prev_song(self):
        """ Select Song before the current one, in current order.
            Wrap around if at the start of the list.
        """
        if self._size > 0:
            if self._current == self._head:
                self._current = self._tail
            self._current = self._current._prev
        else:
            self._current = self._head

    def reset(self):
        """ Reset the current Song to point to the first Song
            (assuming there is one -- self._head if not)
        """
        if self._size > 0:
            self._current = self._head._next
        else:
            self._current = self._head

    def info(self):
        """ Display the info for the current Song to the screen. """
        if self._size == 0:
            print('\nEmpty list - no Song info to display!\n')
        else:
            print("(Info) " + self._current._element.get_info())

    def remove_current(self):
        """ Remove the currently selected Song from the list.

        Returns the Song instance that has been removed.
        """
        if self._current == self._head:
            return None
        temp = self._current
        self._current = temp._next
        if temp._next == self._tail:
            if self._size > 1:  # since if it is 1, that node is about to be removed
                self._current = self._head._next
            else:
                self._current = self._head
        return self._remove_node(temp)  # and this will decrement size

    def length(self):
        """ Return the number of Songs.
        """
        return self._size

    def search(self, word):
        """ Return the next Song which contains word as a substring.

        If Song is found, current Song should change to be that one.
        If no such Song, leave current selection where it is, and return None.
        """
        if self._size == 0:
            return None
        old = self._current
        wrapped = False
        while not wrapped:
            Song = self._current._element
            print('      searching', Song)
            if (word in Song.title
                    or word in Song.artist):
                return Song
            self.next_song()
            if self._current == self._tail:
                self.next_song()
            if self._current is old:
                wrapped = True
        return None

    # ---------- Private Methods ------------------------------ #

    def _add_node_after(self, node, nodebefore):
        """ (Private) Add a node after the specified DLLNode """
        node._prev = nodebefore
        node._next = nodebefore._next
        nodebefore._next._prev = node
        nodebefore._next = node
        self._size = self._size + 1

    def _remove_node(self, node):
        """ (Private) Remove a node and return its element.

        Note: wipes the DLLNode. """
        self._extract_node(node)
        item = node._element
        node._element = None  # cleaning up, so that Python can save space
        return item

    def _extract_node(self, node):
        """ (Private) Remove a DLLNode from the list.

        Note: leaves the Track instance with the  DLLNode.
        """
        if self._current == node:
            self._current = node._prev
        node._prev._next = node._next
        node._next._prev = node._prev
        node._next = None
        node._prev = None
        self._size = self._size - 1

    def _print_node(self, node):
        """ (Private) test function to print internal node details. """
        print('   ' + str(node._element)
              + "[" + str(node._prev._element)
              + "--" + str(node._next._element) + "]")


# ----------- End of class definition for PlayList --------------------- #


def _lab_test():
    """ The test sequence specified in the lab description. """
    ml = Playlist()
    ml.add_song(Song("Taste", "Sabrina Carpenter", 2024, 157))
    ml.add_song(Song("Good luck babe", "Chappell Roan", 2024, 218))
    ml.add_song(Song("Roadrunner", "The Modern Lovers", 1976, 244))
    print(ml)
    ml.next_song()
    print('[stepped forward one Song, now printing selection')
    ml.info()
    ml.next_song()
    print('[stepped forward one Song, now printing full list]')
    print(ml)
    print("\nCurrent: " + str(ml.get_current()) + "\n")
    ml.prev_song()
    ml.remove_current()
    print('[stepped back one Song, then deleted selection, so current should have stepped forward again]')
    print(ml)
    print('[printing current selection: ]')
    ml.info()
    ml.add_song(Song("Road Runner", "Bo Diddley", 1960, 167))
    ml.next_song()
    ml.next_song()
    print(
        '[added Road Runner as a new Song, then stepped forward twice, so should be at start, then printing current selection]')
    ml.info()
    print('[Now printing full list: ]')
    print(ml)
    word = 'Roa'
    print("Searching for 'Roa' ")
    song = ml.search(word)
    if song is not None:
        print('Found song matching', word, ':')
        print('[and so current selection should now be that song]')
        ml.info()
    else:
        print('No match for', word)
    print('[so current selection should not have changed]')
    ml.info()
    print('[and now printing the final list]')
    print(ml)


def _teststate(candidate, target):
    """ Compare two inputs, and print an error message if not the same.

    Args:
        candidate - an input to be compared to a target
        target - the target that candidate is to be compared to
    """
    if candidate != target:
        print("ERROR: should have been: "
              + str(target)
              + " but was: "
              + str(candidate))


_lab_test()