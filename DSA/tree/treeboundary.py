def leftView(self, root):
        
        if root is None:
            return [] 
        
        
        left = []
        
        def fxn(root,level):
            
            # base
            if root is None:
                return

            if len(left) == level:
                left.append(root.data)
            
            #left 
            fxn(root.left,level+1)
           
            #right
            fxn(root.right,level+1)
            
        rightt =[]
        
        def right(root,level):
            if root is None:
                return

            if len(rightt) == level:
                rightt.append(root.data)
                
            #right
            right(root.right,level+1)    
            
            #left 
            right(root.left,level+1)
            
        
       
        noneeee = []

    def nonee(root):
        if root is None:
            noneeee.append(None)
            return

        nonee(root.left)
        nonee(root.right)
            