# Yufei stole this from Albert because he thinks that this recursion exercise is really really
# good and is great practice to recursion.
#
# NOTE: THESE RECURSIVE FUNCTIONS ARE VERY VERY HARD (for students who have NEVER seen recursion before). So don't be
# discouraged and ask Yufei for help if you need to.

"""CSCC24 Lab Week 2: Recursion exercises.

This lab recalls your recursion skill.  Please use recursion to implement the
given functions.  Think of the style of all those recursive programs in CSCB36.
The language is Python 3.

Each function is worth 1 mark.

Due Friday 6PM on MarkUs: https://markus.utsc.utoronto.ca/cscc24w18/
"""


def length(lst):
    """Compute the length of lst (a list).

    Don't use Python's len(lst), of course.  Recall that to ask whether lst is
    non-empty, you can use lst as a boolean condition; when it is non-empty,
    lst[1:] is lst with one fewer item.

    """

    pass


def skip_even(s):
    """Return a new string that omits the even-indexed characters in the input
    string s.

    Examples:
    skip_even("") is ""
    skip_even("abcdefg") is "bdf"

    Suggestion: It is most helpful to use mutual recursion: Define also your own
    skip_odd function that omits the odd-indexed characters.  Have skip_even and
    skip_odd call each other to get the jobs done.  Buy one get one free!

    """

    pass


def tree_max(tree):
    """Compute the maximum of the numbers in the input tree.

    In this function, a tree is represented by a list in which each item can be:
    * an int
    * another tree, i.e., a list in which each item can be... ad nauseum
    Each list involved is non-empty.

    Example: tree_max([1, [3,[5],2], [4]]) is 5

    The recursion in this function is intended for recursing into subtrees;
    you may use common Python features for list processing.

    Suggestions:

    * What do isinstance(5, int) and isinstance([1,4], int) do?

    * What do
        4 if True else 10
      and
        4 if False else 10
      do?

    * List comprehension is great for transforming the items in a list.

      Example: [5*x for x in [3,1,4]] = [5*3, 5*1, 5*4]

    * max([1,5,4]) computes the maximum of the given list.

    """

    pass


def my_filter(predicate, lst):
    """Return a new list of those items x in lst such that predicate(x)
    is True, in their relative order in lst.

    Precondition: lst is a list; predicate maps items to booleans.

    Examples:

    * my_filter(whatever, []) = []

    * If you have
        def pos(n):
            return n > 0
      then my_filter(pos, [3, 1, -4, 0, 5, 9, -2, 7]) = [3, 1, 5, 9, 7]

      Equivalently,
      my_filter(lambda n: n>0,  [3, 1, -4, 0, 5, 9, -2, 7]) = [3, 1, 5, 9, 7]

    Write your own recursion over the list; do not use list comprehension here.

    """

    pass


def parse_binary_le(s):
    """Parse the string s of 0s and 1s into the corresponding number.

    The string is in little-endian order, i.e., the least significant bit is
    at the beginning of the string. E.g., "01011" stands for binary 11010,
    decimal 26.

    If s is empty, the answer is 0.

    Example: parse_binary_le("01011") = decimal 26

    Precondition: s is a string consisting of only '0's and '1's.

    """

    pass


