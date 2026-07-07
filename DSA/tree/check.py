class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.left = TreeNode(5)

def search(root, target):

    if root is None:
        return False

    if root.val == target:
        return True

    return search(root.left, target) or search(root.right, target)


def printt(root,target):
    
    if root == None:
        return "empty"
    
    if root.val == target:
        return "root"
    
    if search(root.left,target):
        return "left"
    
    if search(root.right ,target):
        return "right"
    
    return "not found"


print(printt(root, 1))   # root
print(printt(root, 2))   # left
print(printt(root, 4))   # left
print(printt(root, 3))   # right
print(printt(root, 5))   # right
print(printt(root, 10))  # not found






