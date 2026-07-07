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

def print_leaf(root):
    if root is None:
        return

    if root.left is None and root.right is None:
        print(root.val)
        return

    print_leaf(root.left)
    print_leaf(root.right)

print_leaf(root)
