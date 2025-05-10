n = int(input())
a = 2024
b = 8
if n == 1:
    print(f'{a} {b}')
else:
    for i in range(1, n):
        b += 7
        if b > 12:
            a += 1
            b -= 12
    print(f'{a} {b}')