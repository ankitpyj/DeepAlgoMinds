def bit(n):
    bits =""
    
    while n>0:
        bits = str(n%2) + bits
        n= n//2
           
    return bits 
n= 8
print(bit(n))


