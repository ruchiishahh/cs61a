## Extra Linked Lists and Sets ##

from lab08 import *

# Set Practice

def add_up(n, lst):
    """Returns True if any two non identical elements in lst add up to any n.

    >>> add_up(100, [1, 2, 3, 4, 5])
    False
    >>> add_up(7, [1, 2, 3, 4, 2])
    True
    >>> add_up(10, [5, 5])
    False
    """
    s = set(lst)
    temp_s = set()
    for x in s:
        if not n-x == x:
            temp_s.add(n-x) 
    if len(temp_s.intersection(s)) > 0:
        return True
    return False    

def pow(n,k):
    """Computes n^k.

    >>> pow(2, 3)
    8
    >>> pow(4, 2)
    16
    """
    if k==1:
        return n
    elif k%2 == 0:
        return pow(n*n,k//2)
    else:
        return n*pow(n,k-1)

def missing_no(lst):
    """lst contains all the numbers from 1 to n for some n except some
    number k. Find k.

    >>> missing_no([1, 0, 4, 5, 7, 9, 2, 6, 3])
    8
    >>> missing_no(list(filter(lambda x: x != 293, list(range(2000)))))
    293
    """
    s1 = set(lst)
    s2 = set(range(0,len(lst)+1)) 
    return list(s2 - s1)[0]

def find_duplicates_k(k, lst):
    """Returns True if there are any duplicates in lst that are within k
    indices apart.

    >>> find_duplicates_k(3, [1, 2, 3, 4, 1])
    False
    >>> find_duplicates_k(4, [1, 2, 3, 4, 1])
    True
    """
    s = set(lst[:k+1])
    return len(s) != len(lst[:k+1])

