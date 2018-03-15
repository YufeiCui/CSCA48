class TNode(object):
    ''' a class that represents a binary tree node'''

    def __init__(self, data, left_child=None, right_child=None):
        '''(TNode,obj, TNode,  TNode) -> NoneType
        Constructs a binary tree nodes with the given data'''

        self._left = left_child
        self._data = data
        self._right = right_child

    def set_left(self, left_child):
        '''(TNode, TNode) -> NoneType
        set the left child to the given node'''
        self._left = left_child

    def set_right(self, right_child):
        '''(TNode, TNode) -> NoneType
        set the right child to the given node'''
        self._right = right_child

    def set_data(self, data):
        '''(TNode, obj) -> NoneType
        set the data at this node to the given data'''
        self._data = data

    def get_left(self):
        '''(TNode) -> TNode
        return the pointer to the left child'''
        return self._left

    def get_right(self):
        '''(TNode) -> TNode
        return the pointer to the right child'''
        return self._right

    def get_data(self):
        '''(TNode) -> obj
        return the data stored in this node'''
        return self._data


def visit(Node: 'TNode') -> None:
    print(Node.get_data())


def pre_order(Node: 'TNode') -> None:
    if Node:
        visit(Node)
        pre_order(Node.get_left())
        pre_order(Node.get_right())


def in_order(Node: 'TNode') -> None:
    if Node:
        in_order(Node.get_left())
        visit(Node)
        in_order(Node.get_right())


def post_order(Node: 'TNode') -> None:
    if Node:
        post_order(Node.get_left())
        post_order(Node.get_right())
        visit(Node)


if __name__ == "__main__":
    ''' create this BT using TNode
                 A
               /   \
             B      C   
            /\       \
           D  E      F
                    /
                   G
    '''
    node_G = TNode("G")
    node_F = TNode("F", node_G)
    node_C = TNode("C", None, node_F)
    node_D = TNode("D")
    node_E = TNode("E")
    node_B = TNode("B", node_D, node_E)
    node_A = TNode("A", node_B, node_C)
    
    pre_order(node_A)
    print("========================")
    in_order(node_A)
    print("========================")
    post_order(node_A)
