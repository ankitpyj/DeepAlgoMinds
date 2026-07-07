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

countt = 0
def printt(root):
    
    global countt
    if root != None:
        countt += 1
        

        # printt(root.left)
        # printt(root.right)
        
        # printt(root.left)
        # print(root.val)
        # printt(root.right)
        printt(root.left)
        printt(root.right)
        # print(root.val)
          
    return countt
        
        

printt(root)