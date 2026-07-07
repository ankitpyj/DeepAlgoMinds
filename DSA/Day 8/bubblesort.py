def countSwaps(a):
    swaps = 0
    n = len(a)

    for i in range(n):
        for j in range(n - i - 1):

            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swaps += 1

    print(f"Array is sorted in {swaps} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")
    
a=[1,2,3]
countSwaps(a)