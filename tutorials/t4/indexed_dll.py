# Provided by Dr. Marzieh Ahmadzadeh & Nick Cheng. Edited by Yufei Cui


from DLL import DNode, DoubleLinkedList


class IndexedDLL(DoubleLinkedList):
    '''represents a DLL that provides access to the elements by their index'''

    def __init__(self):
        '''(IndexedDLL) ->NoneType
        initializes the references of an empty IDLL'''
        DoubleLinkedList.__init__(self)

    def insert(self, index, item):
        '''(IndexedDLL, int, obj) -> NoneType
        insert item at  the given index. An exception (IndexError) is raised 
        if the index is invalid
        '''
        # if index is invalid, raise an exception
        if index < 0 or index > self._size:
            raise IndexError("Invalid index provided")
        # if insertion at the front or end is required, call the parent's method
        if index == self._size:
            self.add_last(item)
        elif index == 0:
            self.add_first(item)
        else:
            # Traverse the list to get to the node immediately before the index
            # remember that in dll head is a dummy node
            cur = self._head.get_next()
            for i in range(0, index - 1):
                cur = cur.get_next()
            # create the new node and establish the linkes
            new_node = DNode(item, cur, cur.get_next())
            cur.get_next().set_prev(new_node)
            cur.set_next(new_node)
            self._size += 1

    def remove(self, index):
        '''(IndexedDLL, int) -> obj
        remvoe the node from the list at the given index and returns the element stored in this node
        Raises IndexError if list is empty or index is out of range'''
        # check for the exception, if index is out of range or list is empty.
        if index < 0 or index > self._size - 1 or self.is_empty():
            raise IndexError("Invalid request")
        # if index is 0 or size -1 call the parent's method
        if index == 0:
            element = self.remove_first()
        elif index == self._size - 1:
            element = self.remove_last()
        else:
            # traverse the list to get to a node immediately before the index
            cur = self._head
            for i in range(0, index):
                cur = cur.get_next()
            # remove the node and establish the links between previous node and next node of
            # the node to be deleted
            node_to_delete = cur.get_next()
            element = node_to_delete.get_element()
            cur.set_next(node_to_delete.get_next())
            node_to_delete.get_next().set_prev(cur)
            # nullify the node to make it a subject for GC
            node_to_delete.set_next(None)
            node_to_delete.set_prev(None)
            self._size -= 1
        return element


if __name__ == "__main__":
    idll = IndexedDLL()
    idll.insert(0, "a")
    idll.insert(1, "b")
    idll.insert(1, "c")
    idll.insert(2, "d")
    idll.insert(3, "e")
    idll.insert(1, "f")
    idll.insert(2, "g")
    print(idll)
    idll.remove(0)
    idll.remove(5)
    idll.remove(3)
    print(idll)
