class Treeroot(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    
root = Treeroot(1)
root.left = Treeroot(2)
root.right = Treeroot(3)
root.left.left = Treeroot(4)
root.right.left = Treeroot(5)


def level(root, curr):

    if root is None:
        return curr

    left = level(root.left, curr + 1)
    right = level(root.right, curr + 1)

    return max(left, right)

print(level(root, 0))
    
    