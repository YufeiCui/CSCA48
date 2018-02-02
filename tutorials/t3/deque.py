# Provided by Dr. Marzieh Ahmadzadeh & Nick Cheng. Edited by Yufei Cui


class EmptyQueueError(Exception):
    '''An error to be raised when someone tries to dequeue from an empty queue'''


class Deque(object):
    '''A double ended queue'''

    def __init__(self):
        '''(Deque) -> NoneType
        Construct an empty Deque
        '''
        # Representation invariant:
        # _contents is a list
        # _contents[:] are the objects in the deque.
        # len(_contents) is the number of items in the deque
        # if 0 <= i < j < len(_contents), then
        #    _contents[i] is to the left of _contents[j] in the deque
        #    _contents[j] is to the right of _contents[i] in the deque

        self._contents = []

    def enqueue_left(self, item):
        '''(Deque, obj) -> None
        Add item onto the left side of the deque
        '''
        self._contents = [item] + self._contents

    def enqueue_right(self, item):
        '''(Deque, obj) -> None
        Add item onto the right side of the deque
        '''
        self._contents = self._contents + [item]

    def dequeue_left(self):
        '''(Deque) -> object
        Remove and return the leftmost item in the deque
        '''
        if self.is_empty():
            raise EmptyQueueError("Can't dequeue from an empty queue")
        else:
            item = self._contents[0]
            self._contents = self._contents[1:]
            return item

    def dequeue_right(self):
        '''(Deque) -> object
        Remove and return the rightmost item in the deque
        '''
        if self.is_empty():
            raise EmptyQueueError("Can't dequeue from an empty queue")
        else:
            item = self._contents[-1]
            self._contents = self._contents[:-1]
            return item

    def is_empty(self):
        '''(Deque) -> bool
        Return True iff this deque is empty
        '''
        return len(self._contents) == 0


if __name__ == "__main__":
    dq = Deque()
    dq.enqueue_left('A')
    dq.enqueue_left('B')
    dq.enqueue_left('C')
    dq.enqueue_right('D')
    dq.enqueue_right('E')
    dq.enqueue_right('F')
    dq.enqueue_left('G')
    while not dq.is_empty():
        print(dq.dequeue_right())
        # beware that you'll receive an exception at some point. Why?
        print(dq.dequeue_left())
