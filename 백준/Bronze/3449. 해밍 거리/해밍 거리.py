n = int(input())
for _ in range(n):
    a = input()
    b = input()
    l = len(a)
    total = 0
    for i in range(l):
        if a[i] != b[i]:
            total += 1
            
    print(f"Hamming distance is {total}.")