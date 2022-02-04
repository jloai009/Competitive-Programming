def build_bst(array):
    array.sort()
    return build(array, 0, len(array)-1)

def build(array, l , r):
    if l <= r:
        m = (l+r) // 2
        node = BST(array[m])
        node.left = build(array, l , m-1)
        node.right = build(array, m+1, r)
        return node

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None