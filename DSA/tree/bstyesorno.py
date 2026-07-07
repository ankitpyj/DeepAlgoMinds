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


def bstyes(root):
    
    if root == None:
        return True

    if  not root.left.val < root.val:
        # bstyes(root.left)
        return False
        
    # else:
    #     return False
        
    if root.right.val > root.val:    
        # bstyes(root.right)
        return False
    # else:
    #     return False    
        
    return bstyes(root.left) and bstyes(root.right)
 

print(bstyes(root))
        