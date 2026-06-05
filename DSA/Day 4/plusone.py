def plusOne(digits):
    n = len(digits)
    # last number meh change krna h 
    for i in range(n-1,-1,-1):

        # last digit <9:
        if digits[i] < 9 :
            digits[i] += 1
            return digits
        
        # last digit ==9 --> 0 and carry forward :
        else:
            digits[i] = 0
        
    return [1] + digits
        

digits = [9,9,9]
print(plusOne(digits))