class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
def remove(pos,head):
        
        
    length = 0
    tmp = head

    while tmp:
        length += 1
        tmp = tmp.next
    
    if pos < 1 or pos > length:
        print("Invalid Position")
        return head
    
  
    if head is None:
        return None


  # case 1: remove first
    if pos == 1:
        head = head.next
        return head
        

    #case 2: end remove
    elif length == pos:
        
        tmp = head
    
        while tmp.next.next is not None:
            tmp = tmp.next
    
        tmp.next = None
        return head
    
        

    #case3: between remove
    
    else:
        curr = 1
        tmp = head

        while curr < pos - 1:
            tmp = tmp.next
            curr += 1
            
        tmp.next = tmp.next.next
        return head
    
    

def display(head):
    temp = head
    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("None")
    
    
    

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)


display(head)       

head = remove(3, head)  
display(head)

head = remove(1, head)
display(head)

head = remove(4, head)
display(head)