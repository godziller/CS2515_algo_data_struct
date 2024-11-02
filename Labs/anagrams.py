""" Example functions for comparing methods of checking anagrams (as lists).

    Contains four main functions
        isAnagramReplace: for each element in the 1st list, find a match in
                          the 2nd and replace it with a null character
        isAnagramRemove:  for each element in the 1st list, find a match in
                          the 2nd and delete it 
        isAnagramSort:    sort the two lists, and then step through them in
                          parallel, checking the elements match
        isAnagramCount:   initialse a list of count=0 of length alphabet size,
                          then for each index in list1, read the element in that index in 
                          list 1 and list 2, increment the count for  list1 item and 
                          decrement the count for list2 item, and make sure they are all 0 
                          at the end
        isAnagramDict:    same as ...Count, but using a Python dict
        isAnagramCount2:  for each element in the alphabet, count the number
                          of times it appears in each list, and make sure
                          they are all the same

    The alphabet is integers from 0 to 9999.
    
    Also contains some performance evaluation functions.

    To run, invoke perf_check_random(k), where k is the length of a pair of
    random lists to be checked for being anagrams.
"""

from time import perf_counter

import random


def performance_check(list1, list2, size):
    """ Evaluate the performance of the anagram functions.

    Note that the ...replace() function will take a long time to run
    on long input lists, and so that line should be commented out
    for lists of length > 100K.

    Args:
        list1: first list for comparison
        list2: second list for comparison
        size: the size of the alphabet

    """
    
    print('List length: %d' % len(list1))

    # run each function on the two lists, checking clock times in between

    # first the count method
    count_start_time = perf_counter()
    count_res = is_anagram_count(list1, list2, size)
    count_end_time = perf_counter()
    print('Count time    : %f %s' % (count_end_time - count_start_time,
                                     count_res))

    # then the dict method
    count_start_time = perf_counter()
    count_res = is_anagram_dict(list1, list2)
    count_end_time = perf_counter()
    print('Dict time     : %f %s' % (count_end_time - count_start_time,
                                     count_res))

    # then the dict2 method
    count_start_time = perf_counter()
    count_res = is_anagram_dict2(list1, list2)
    count_end_time = perf_counter()
    print('Dict2 time    : %f %s' % (count_end_time - count_start_time,
                                     count_res))



    # now the sort method
    # create copies, so that we don't change data for later methods
    if len(list1) < 10000001:
        copylist1 = list1.copy()
        copylist2 = list2.copy()
        sort_start_time = perf_counter()
        sort_res = is_anagram_sort(copylist1, copylist2)
        sort_end_time = perf_counter()
        print('Sort time     : %f %s' % (sort_end_time - sort_start_time,
                                         sort_res))

        """        
        # now do a quick check on the time required just for sorting
        # to see whether the expensive part is the sort or the sequence of comparisons
        # do this before the replace function, because replace changes the lists
        copylist3 = list1.copy()
        copylist4 = list2.copy()
        waypoint_time = perf_counter()
        copylist3.sort()
        copylist4.sort()
        end_time = perf_counter()
        # now print the stats for the pure sort
        print('   pure sort time: %f' % (end_time - waypoint_time))
        """
    else:
        print('Lists too long to run the sort method')

    # then the 2nd count method
    if len(list1) < 1000001:
        count_start_time = perf_counter()
        count_res = is_anagram_count2(list1, list2, size)
        count_end_time = perf_counter()
        print('Count2 time   : %f %s' % (count_end_time - count_start_time,
                                     count_res))
    else:
        print('Lists too long to run the 2nd count method')
        
        
    # now the remove method
    if len(list1) < 100000:
        copylist1 = list1.copy()
        copylist2 = list2.copy()
        remove_start_time = perf_counter()
        remove_res = is_anagram_remove(copylist1, copylist2)
        remove_end_time = perf_counter()
        print('Remove time   : %f %s' % (remove_end_time - remove_start_time,
                                         remove_res))
    else:
        print('Lists too long to run the remove method')
        
    # now the replace method
    # should create copies, but dont need to, since last algorithm in this iteration
    if len(list1) < 100000:
        replace_start_time = perf_counter()
        replace_res = is_anagram_replace(list1, list2)
        replace_end_time = perf_counter()
        print('Replace time  : %f %s' % (replace_end_time - replace_start_time,
                                         replace_res))
    else:
        print('Lists too long to run the replace method')
        

    

def correctness_check(list1, list2):
    """ Test the correctness of anagram functions.

    Args:
        list1: first list for comparison
        list2: second list for comparison
    """

    print('List 1: %s' % list1)
    print('List 2: %s' % list2)

    # run each function on the two lists

    # first the count method
    print('count: %s' % is_anagram_count(list1, list2))

    # then the dict method
    print('dict: %s' % is_anagram_dict(list1, list2))

    # now the sort method
    # create copies, so that we don't change data for later methods
    copylist1 = list1.copy()
    copylist2 = list2.copy()
    print('sort: %s' % is_anagram_sort(copylist1, copylist2))

    # now the replace method
    print('replace: %s' % is_anagram_replace(list1, list2))


def perf_check_random(k, size):
    """ Compare performance on random lists of length k.

    Lists must be composed of elements in {0, ..., size-1}

    Args:
        k: (int) length of lists
        size: (int) length of alphabet

    """

    print('Alphabet size:', size)

    if k < 1:
        return False

    # generate a random list of length k, then copy it and shuffle the copy
    # then call performance_check on the lists
    rand_list = list()    
    for i in range(k):
        rand_list.append(random.randint(0,size-1))
    second_list = rand_list.copy()
    random.shuffle(second_list)
    performance_check(rand_list, second_list, size)

def run_scale_tests():
    k = 10
    while k < 1000001:
        perf_check_random(k)
        k = k*10
    
    
def is_anagram_replace(list1, list2):
    """ Check whether two lists are anagrams, by replacement.

    For each element in the first input, find a match in the second and
    replace it by a null value so it cant be matched again.

    Args:
        list1: first list for comparison
        list2: second list for comparison

    Returns:
        true if lists of same length and all elements replaced
        false otherwise
    """

    if len(list1) != len(list2):  # anagrams must be same length
        return False
                                           
    for pos1 in range(len(list1)):      # for each element in list1
        found = False                   # found a match for list1[pos1] yet?
        pos2 = 0
        while pos2 < len(list2) and not found:  # step list2 looking for match
            if list1[pos1] == list2[pos2]:      # if we find the match
                found = True
                list2[pos2] = None              # replace element in the list
            pos2 += 1

        if not found:                       # if we didn't find a match
            return False                    # prefix is not in list2

    return True
        

def is_anagram_remove(list1, list2):
    """ Check whether two lists are anagrams, by removing matched items.

    For each element in the first input, find a match in the second and
    remove it.

    Args:
        list1: first list for comparison
        list2: second list for comparison

    Returns:
        true if lists of same length and all elements removed from 2nd
        false otherwise
    """

    if len(list1) != len(list2):  # anagrams must be same length
        return False
                                           
    for pos1 in range(len(list1)):      # for each element in list1
        found = False                   # found a match for list1[pos1] yet?
        pos2 = 0
        while pos2 < len(list2) and not found:  # step list2 looking for match
            if list1[pos1] == list2[pos2]:      # if we find the match
                found = True
                del list2[pos2]              # remove element from the list
            pos2 += 1

        if not found:                       # if we didn't find a match
            return False                    # prefix is not in list2

    return True
        
def is_anagram_sort(list1, list2):
    """ Check whether two lists are anagrams, by sorting and comparing.

    Sort the lists, then step through in parallel checking that the
    elements match

    Args:
        list1: first list for comparison
        list2: second list for comparison

    Returns:
           true if lists of same length and all elements match
           false otherwise
    """

    if len(list1) != len(list2):  # anagrams must be same length
        return False

    list1.sort()                   # sort each list
    list2.sort()

    for pos in range(len(list1)):         # step through the lists in parallel
        if list1[pos] != list2[pos]:      # if elements don't match
            return False                  # it can't be an anagram

    return True                          

def is_anagram_count(list1, list2, size):
    """Check whether two lists are anagrams, by counting elements.

       Lists must be composed of elements in {0, ..., size-1}
       
       Create a list of 0s of same length as alphabet.
       
       For position in the two lists simultaneously, count +1 for the 
       character in that position in list 1, and count -1 for the character
       in that position in list 2.

    Args:
        list1: first list for comparison
        list2: second list for comparison
        size: length of alphabet

       Returns:
           true if lists of same length and all elements have count 0
           false otherwise
    """

    if len(list1) != len(list2): # anagrams must be same length
        return False

    count_list = [0] * size    # the counters for each element in the alphabet

    for i in range(len(list1)):      # step through each position in turn
        # elt1 = list1[i]              # element from list1
        # count_list[elt1] += 1   # increment counter for elt1
        # one-line version of the two lines above: 
        count_list[list1[i]] +=1
        # elt2 = list2[i]              # element from list2
        # count_list[elt2] -= 1   # decrement counter for elt2
        # one-line version of the two lines above:
        count_list[list2[i]] -=1
    
    for pos in count_list:
        if pos != 0:
            return False              # if any element is non-zero
    
    return True

def is_anagram_dict(list1, list2):
    """ Check whether two lists are anagrams, by counting elements using a dict.

    Lists must be composed of elements in {0, ..., 999}

    Create an empty dictionary, where keys will be in {0, ..., 999}, and values
    the number of appearances in list1 minus the number in list2. If an
    integer does not appear as a key in the dict, then it has not appeared
    in either list.
    For each position in the lists, for the elt in list1, add 1 to the
    value for the key corresponding to that elt, and create a new entry with
    value 1 if there is no such key; for the elt in list2, do the same, but
    use -1 in each case.
    for each key in the dict, if the value is not 0, return false.
    return true.

    Args:
        list1: first list for comparison
        list2: second list for comparison

    Returns:
        true if lists of same length and contain same bag of elements (and so
        all entries in fainal dict are 0)
    """

    if len(list1) != len(list2):  # anagrams must be same length
        return False

    count = {}  # the dictionary for maintaining the counts

    for i in range(len(list1)):          # step through each position in turn
        # count[list1[i]] = count.get(list1[i],0) + 1  # incr value or set to 1
        # count[list2[i]] = count.get(list2[i],0) -1
        if list1[i] in count:
            count[list1[i]] += 1
        else:
            count[list1[i]] = 1
        if list2[i] in count:
            count[list2[i]] -= 1
        else:
            count[list2[i]] = -1

    for key in count:
        if count[key] != 0:
            return False              # if any element is non-zero

    return True

def is_anagram_dict2(list1, list2):
    """ Check whether two lists are anagrams, by counting elements using a dict.

    Lists must be composed of elements in {0, ..., 999}

    Create an empty dictionary. For each item in list1, add it as key with value 1,
    or increment its value. For each item in list 2, decrement its value (and if it hits 0,
    remove the key); if it is not in the dictionary, stop and return False.

    Args:
        list1: first list for comparison
        list2: second list for comparison

    Returns:
        true if lists of same length and contain the same bag of elements (and so
        the final dictionary should have no keys)
    """

    if len(list1) != len(list2):  # anagrams must be same length
        return False

    count = {}  # the dictionary for maintaining the counts

    for i in range(len(list1)):          # step through each position in turn
        # count[list1[i]] = count.get(list1[i],0) + 1  # incr value or set to 1
        # count[list2[i]] = count.get(list2[i],0) -1
        if list1[i] in count:
            count[list1[i]] += 1
        else:
            count[list1[i]] = 1

    for i in range(len(list2)):        
        if list2[i] in count:
            count[list2[i]] -= 1
            if count[list2[i]] == 0:
                del count[list2[i]]
        else:
            return False

    return True

def is_anagram_count2(list1, list2, size):
    """Check whether two lists are anagrams, by counting elements.

       Lists must be composed of elements in {0, ..., size-1}
       
       For each character in the alphabet, count how many time it appears in list1,
       then how many times it appears in list2, and if not the same, return False.

       If cell returned False, then they are anagrams.

    Args:
        list1: first list for comparison
        list2: second list for comparison
        size: the size of the alphabet

       Returns:
           true if lists of same length and all elements have count 0
           false otherwise
    """

    if len(list1) != len(list2): # anagrams must be same length
        return False

    for x in range(size):
        count1 = list1.count(x)
        count2 = list2.count(x)
        if count1 != count2:
            return False
    
    return True
    
for i in [10,100,500,1000,2000,5000,10000,50000,100000,500000,1000000,10000000]:
    perf_check_random(i, 1000)