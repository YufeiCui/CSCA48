# Provided by Dr. Marzieh Ahmadzadeh & Nick Cheng. Edited by Yufei Cui


class EmptyHeapException(Exception):
    pass


class Entry(object):
    ''' represents an entry that includes a key and a value'''

    def __init__(self, key, value):
        '''(Item, int, obj) -> NoneType
        constructs an item using key and value'''
        # Representation Invariant
        # _key is a positive integer
        # _value is an object of any type
        self._key = key
        self._value = value

    def get_key(self):
        '''(Entry) ->int
        returns the key of this entry'''
        return self._key

    def get_value(self):
        '''(Entry) ->obj
        returns the value of this entry'''
        return self._value

    def __str__(self):
        '''(Entry) ->str
        returns a string representation  of this entry'''
        return "(" + str(self._key) + ", " + str(self._value) + ")"


class Heap(object):
    ''' represents a heap, which is a complete binary tree, and satisfies 
    a heap-order, using a list.
    In this implementation, each node contains the keys only.
    you complete this code by storing an entry (key, value) in each node.
    '''

    def __init__(self, root_entry):
        '''(Heap, Entry) -> NoneType
        construct a heap with root_entry as its root'''
        # representation invariant
        # _heap is a list
        # _heap[0] represents the root of the tree
        # _heap[0] has the highest priority
        # _heap[2*i + 1] represents the left child of the 
        #     node that stored at index i, and _heap[2*i + 1] >= _heap[i] 
        # _heap[2*i + 2] represents the right child of the 
        #     node that stored at index i, and _heap[2*i + 2] >= _heap[i]
        # _heap[len(_heap) -1] shows the last node
        # _heap[:] represents the result of traversing the tree by BFS, if not empty

        # append root_entry to a newly created empty list.
        self._heap = []
        self._heap.append(root_entry)

    def size(self):
        '''(Heap) -> int
        returns the number of nodes in the heap'''
        return len(self._heap)

    def is_empty(self):
        '''(Heap) -> bool
        returns True if this heap is empty'''
        return len(self._heap) == 0

    def remove_last_node(self):
        '''(Heap) -> Entry
        removes the last node from the heap and returns the entry stored in this node
        Raises: EmptyHeapException if this heap is empty'''
        if self.is_empty():
            raise EmptyHeapException("Heap is empty")
        return self._heap.pop()

    def min(self):
        '''(Heap) -> Entry
        returns the entry with the highest priority
        Raises: EmptyHeapException'''
        if self.is_empty():
            raise EmptyHeapException("Heap is empty")
        return self._heap[0]

    def insert(self, entry):
        '''(Heap, Entry) -> NoneType
        insert the given entry at right place in the heap'''
        # step 1, 2, 3:  find the new last node, insert data, update last node
        # new last node is the element at len(self._heap)
        self._heap.append(entry)
        # step 3, restore heap-order
        self.upheap_bubbling()

    def upheap_bubbling(self):
        '''(Heap) -> None
        restores heap order by swaping the entries along an upward path from inserted node'''
        # find the last node index
        cur = len(self._heap) - 1
        # find the parent (always  (last_node - 1//2) because it rounded down)
        parent = (cur - 1) // 2
        # continue swapping until last node in right place or you get to the root
        while cur > 0 and self._heap[parent].get_key() > self._heap[cur].get_key():
            self._heap[parent], self._heap[cur] = self._heap[cur], self._heap[parent]
            # update cur and parent
            cur = parent
            parent = (cur - 1) // 2

    def extract_min(self):
        '''(Heap) -> Entry
        removes the highest priority Entry and return it.
        Raises: EmptyHeapException
        '''
        # raise an exception if heap is empty
        if self.is_empty():
            raise EmptyHeapException("Heap is empty")
        # step 1: get the entry with minimum key 
        min_value = self._heap[0]
        # remove the last node
        l_node = self._heap.pop(len(self._heap) - 1)
        # step2: replace the root with last node if at least there is one entry in the heap
        if len(self._heap) != 0:
            # replace teh root with the last node
            self._heap[0] = l_node
            # step 3, 4: last node will be updated automatically, so restore the heap_order
            self.downheap_bubbling()
        # return the highest priority item
        return min_value

    def downheap_bubbling(self):
        '''(Heap) -> NoneType
        restore the heap order by swapping the entries down the path'''
        # start from the root
        cur = 0
        # continue going down while heap order is violated
        while self.violates(cur):
            # find the index of the child which contains smaller data/ violates heap order
            child_index = self.find_index(cur)
            # swap data at cur and data at child
            self._heap[cur], self._heap[child_index] = self._heap[child_index], self._heap[cur]
            # update cur to point to child_index
            cur = child_index

    def violates(self, index):
        '''(Heap, index) -> bool
        checks if the given index has a key greater than one of its children'''
        # get left and right child index
        left = index * 2 + 1
        right = index * 2 + 2
        # raise a flag as an indicator of the violation
        violates = True
        # if cur index points to a leaf, it does not violate the heap order. a leaf is a node whose left child index
        # is greater than the heap's length
        if left >= len(self._heap):
            violates = False
        # otherwise, it may have one child. since the heap is a complete tree, therfore it has a left child,
        # which means the index to right child is >= than the heap's length. In this case we check the left child for
        #  the violation of heap-order
        elif right >= len(self._heap):
            violates = self._heap[index].get_key() > self._heap[left].get_key()
        # otherwise, it has two children, therefore you need to check both the children
        else:
            violates = (self._heap[index].get_key() > self._heap[left].get_key()) or (
                        self._heap[index].get_key() > self._heap[right].get_key())
        return violates

    def find_index(self, index):
        '''(Heap, int) -> int
        return the index where it violates the heap order'''
        # find left and right child and initialize returned index
        left = index * 2 + 1
        right = index * 2 + 2
        returned_index = 0
        # if it has one child, it is left child. which means right child's index >= len of heap
        if right >= len(self._heap):
            returned_index = left
        # otherwise, we should find which one of its children has smaller data
        elif self._heap[left].get_key() < self._heap[right].get_key():
            returned_index = left
        else:
            returned_index = right
        # return the found index
        return returned_index

    def BFS(self):
        '''(BT) -> str
        traverse the tree in Breadth First search mehtod
        '''
        # remove all Nones from the list
        result = ""
        for item in self._heap:
            if item is not None:
                result = result + " " + str(item)
        return result


if __name__ == "__main__":
    ''' construct  a priority queue using a heap
    containing these keys:
    (95, 'A'), (40, 'B'), (55, 'C'), (60, 'D'), (20, 'E'), (50, 'F'), (85, 'G')
    '''
    a = Entry(95, 'A')
    b = Entry(40, 'B')
    c = Entry(55, 'C')
    d = Entry(60, 'D')
    e = Entry(20, 'E')
    f = Entry(50, 'F')
    g = Entry(85, 'G')
    heap = Heap(a)
    heap.insert(b)
    heap.insert(c)
    heap.insert(d)
    heap.insert(e)
    heap.insert(f)
    heap.insert(g)

    print(heap.BFS())

    print(heap.extract_min())
    print(heap.BFS())
    print(heap.extract_min())
    print(heap.BFS())
    print(heap.extract_min())
    print(heap.BFS())
    print(heap.extract_min())
    print(heap.BFS())
    print(heap.extract_min())
    print(heap.BFS())
    print(heap.extract_min())
    print(heap.BFS())
    print(heap.extract_min())
    print(heap.BFS())
    """this should raise an exception
    print(heap.extract_min())
    """
