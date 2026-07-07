class Node():
    def __init__(self, val=0, left=0, right=0):
        self.val = val
        self.left = left
        self.right = right
        
        
root = Node(20)

root.left = Node(10)

root.right = Node(25)
root.left.left = Node(9)
root.left.right = Node(15)

root.right.left = Node(22)
root.right.right = Node(30)



# def insert(val):
#     if root == None:
#         return False
    
#     if val < root.val:
#         root.left = insert(root.left,val)
        
#     else:
#         root.right = insert(root.right,val)
        
#     return root


class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


# Create BST
root = TreeNode(5)

root.left = TreeNode(3)
root.right = TreeNode(8)

root.left.left = TreeNode(2)
root.left.right = TreeNode(4)

root.right.left = TreeNode(7)
root.right.right = TreeNode(9)


def search(root, target):
    if root is None:
        return False

    if root.val == target:
        return True

    elif target < root.val:
        return search(root.left, target)

    else:
        return search(root.right, target)


print(search(root, 4))   # True
print(search(root, 10))  # False
    
    
    
def findlargest(root):
    if root.right == None:
        return root.val
    
    return findlargest(root.right)
        
    
    

    


