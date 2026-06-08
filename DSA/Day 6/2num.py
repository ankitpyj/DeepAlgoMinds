def num(n):

    if n<0:
        return False
    
    while n%2 == 0:
        n//=2

    return n == 1

n=10
print(num(n))
    

#TLE  o(logn)