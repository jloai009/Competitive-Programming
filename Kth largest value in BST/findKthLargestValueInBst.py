class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def findKthLargestValueInBst(tree, k, position=[0]):
    if tree:
        r = findKthLargestValueInBst(tree.right, k, position)
        position[0] += 1
        print(position[0])
        if position[0] == k:
            return tree.value
        l = findKthLargestValueInBst(tree.left, k, position)
        return r or l
