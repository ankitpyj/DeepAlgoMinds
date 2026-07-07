class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
def insert(pos,val,head):
    
    permanent_head = head
    
    last_node =  None
    
    #length find
    leng = 0
    while head != None:
        leng = leng +1
        
        if head.next == None:
            last_node = head    
            
        head = head.next
        

    
    head = permanent_head
    # case 1 : insert at pos 1
    if pos == 1:
        new_node = Node(val)
        new_node.next = head
        permanent_head = new_node
       
    # case 2: last add    
    elif leng < pos:
        new_node = Node(val)
        last_node.next = new_node
    
    #case 3 : between
    else:
        curr_post = 1
        
        while curr_post < pos-1:
            head = head.next
            curr_post += 1
            
        new_node = Node(val)
        
        temp = head.next
        head.next = new_node
        new_node.next = temp
    
    return permanent_head 
        
            

def display(head):
    tmp = head
    while tmp:
        print(tmp.data, end=" -> ")
        tmp = tmp.next
    print("None")
    
    
    

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)

display(head) 

head = insert(3,100, head)  
display(head)
  
                
                 
                