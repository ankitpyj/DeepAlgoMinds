class Node():
    def __init__(self, val=0, left=0, right=0,middle =0):
        self.val = val
        self.left = left
        self.middle =middle
        self.right = right
        
        
root = Node(1)

root.left = Node(2)
root.middle = Node(3)
root.right = Node(4)

root.left.left = Node(5)
root.left.middle = Node(6)
root.left.right = Node(7)


root.right.right = Node(10)







