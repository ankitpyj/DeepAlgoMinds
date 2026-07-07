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


def printt(root,target):
    
    if root == None:
        return False
    
    if root == target:
        return True
    
    #left 
    # left_ans = printt(root.left,target)
    
    # right_ans = printt(root.right,target)
    
    # return left_ans or right_ans
    
    return printt(root.left ,target) or printt(root.right,target)
      
        

print(printt(root,target=13))