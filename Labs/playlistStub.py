""" Classes to implement a (simulated) playlist.

Note that the songs, etc. exist as independent objects, stored
elsewhere in the system. What we are doing with Playlist is linking them
together so that we can recall them and browse them.

For this to work in a single programming exercise, we are including the
definition of the Song class, and in the test methods we may create some
new song instances.

For CS2515 labs on DoublyLinked Lists

Stub file - the implementation of the class Playist needs to be
completed.

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


Song._test()


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

    # Can be implemented with the dummy head and dummy tail, or instead with
    # fields first and last, that point to DLLSongNodes with real song
    # instances

    # but must have the following two fields:

    # _size: the number of Song instances in the list
    # _current: one node in the list, representing the current selection
    #           This must always refer to a real node in the list (as opposed
    #           to a dummy head or tail node), unless the list is empty, in
    #           which case it refers to the dummy head.

    def __init__(self):
        """ Initialise an empty library. """

    def __str__(self):
        """ Return a string representation of the list. """

    # ---------- Public Methods ------------------------------#

    # This is the specification - each one of these methods should be implemented,
    # return types should not be different from that specified, the order of the
    # arguments should not change, and arguments should not be removed.
    # If you add additional arguments, they must go at the end of the sequence,
    # and they must be optional.
    # Anyone calling your code must be able to invoke the methods below exactly
    # as they are specified, and they must receive return types as specified.

    def add_song(self, Song):
        """ Add Song to the end of the list.

        Args:
            Song: the Song instance to be added

        """

    def get_current(self):
        """ Get the currently selected Song.

        Returns the Song instance.
        """

    def next_song(self):
        """ Select the Song after the current one, in current order.
            Wrap around if at the end of the list.
        """

    def prev_song(self):
        """ Select Song before the current one, in current order.
            Wrap around if at the start of the list.
        """

    def reset(self):
        """ Reset the current Song to point to the first Song
            (assuming there is one -- self._head if not)
        """

    def info(self):
        """ Display the info for the current Song to the screen. """

    def remove_current(self):
        """ Remove the currently selected Song from the list.

        Returns the Song instance that has been removed.
        """

    def length(self):
        """ Return the number of Songs.
        """

    def search(self, word):
        """ Return the next Song which contains word as a substring.

        If Song is found, current Song should change to be that one.
        If no such Song, leave current selection where it is, and return None.
        """


# ---------- Private Methods ------------------------------ #

# Methods in here are for you as programmer, if they help you write the public
# methods.

# Some of the methods from the lecture on DoublyLinkedLists might be useful.
# I use  add_node_after() and remove_node()

# But you don't have to put anything here - it is fine to implement it
# directly inside the public methods above.


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


def _teststate(input1, input2):
    """ Compare two strings, and print an error message if not the same. """
    if input1 != input2:
        print("ERROR: should have been: "
              + str(input2)
              + " but was: "
              + str(input1))


_lab_test()