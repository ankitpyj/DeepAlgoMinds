def ishappy(n):
    seen = set()      # added

    while n != 1:
        if n in seen: # added
            return False

        seen.add(n)   # added

        total = 0

        while n > 0:
            digit = n % 10
            total += digit * digit
            n //= 10

        n = total

    return n == 1

n = 2
print(ishappy(n))