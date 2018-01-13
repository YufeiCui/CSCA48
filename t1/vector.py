# Provided by Dr. Marzieh Ahmadzadeh for CSCA08

# This code comes from "Data Structures & Algorithms in Python"
# by M. Goodrich, R. Tamassia and M.Goldwasser with some modifications
# to fit my course.


class Vector(object):
    def __init__(self, size):
        ''' (Vector, obj) -> NoneType
        creates a geometric vector of the given size'''
        self._vect = [0] * size

    def length(self):
        ''' (Vector) -> int
        returns the number of items in the vector (i.e. length)'''
        return len(self._vect)

    def get(self, index):
        ''' (Vector, int) -> obj
        returns the object that is found at the given index'''
        return self._vect[index]

    def set(self, index, value):
        ''' (Vector, int, obj) -> NoneType
        set the given index to the given value'''
        self._vect[index] = value

    def add(self, other_vect):
        ''' (Vector, Vector) -> Vector
        returns the sum of two vectors'''
        # check for equality of the length
        if self.length() != other_vect.length():
            # you can throw your own exception
            raise ValueError("dimenstions of the vectors must agree")
        # create an empty vector
        sum = Vector(self.length())
        # add them up
        for index in range(0, self.length()):
            sum.set(index, self._vect[index] + other_vect.get(index))
        return sum

    def equal(self, other_vect):
        '''(Vector, Vector) -> bool
        returns true if two vectors have the same coordinates
        '''
        return self._vect == other_vect._vect

    def __str__(self):
        '''(Vector) -> str
        returns a string representing the vector'''
        return str(self._vect[0:])


if __name__ == "__main__":
    v = Vector(5)
    u = Vector(5)
    print(u.equal(v))
    for i in range(5):
        v.set(i, i)
        u.set(i, i)
    print(u)
    print(v)

    for i in range(5):
        v.set(i, "i ")
        u.set(i, "J ")
    print(u)
    print(v)
    print(v.add(u))
    # The following creates an exception. it's better to throw your own exception
    # u.set(7, 6)
