def commonElements(a, b, c):
    
    i=j=k=0
    ans =set()

    while i < len(a) and j< len(b) and k<len(c):
        
        if a[i] == b[j] == c[k]:
            ans.add(a[i])
            i+=1
            j+=1
            k+=1
        
        elif a[i] < b[j] :
            i+=1
        
        elif b[j] < c[k] :
            j+=1

        else:
            k+=1
        
    return list(ans)

a = [1,5,10,20,30]
b = [5,13,15,20]
c = [5,20]

print(commonElements(a,b,c))



