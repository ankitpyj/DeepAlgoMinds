class Node():
    def __init__(self, val=0, left=None, right=None):
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



def findlargest(root):
    
    if root is None:
        return None
    
    if root.right == None:
        return root.val
    
    return findlargest(root.right)


print(findlargest(root))


def findlargestgeneral(root):
    if root is None:
        return 0
    
    
    left_max = findlargestgeneral(root.left)
    right_max = findlargestgeneral(root.right)
    return max(root.val,left_max,right_max)

print(findlargestgeneral(root))



def largestseconf(root):
    
    if root is None:
        return -1
    
    if (root.right is None) and (root.left is None):
        return -1
    
    parent = None
    child = root
    while child.right :
        parent = child
        child = child.right
        
    # Left subtree 
    
    if child.left:
        new_value = child.left
        
        while new_value.right:
            new_value = new_value.right
        return new_value.val
        
    return parent.val

print(largestseconf(root))
        
        
        
        
        
        
        
    
        
        





#GENERAL VCASE


# def solve(root):
#     if root is None:
#         return base_value

#     left = solve(root.left)
#     right = solve(root.right)

#     return combine(root, left, right)


# # Count nodes
# return 1 + left + right

# # Sum nodes
# return root.val + left + right

# # Height
# return 1 + max(left, right)

# # Largest value
# return max(root.val, left, right)