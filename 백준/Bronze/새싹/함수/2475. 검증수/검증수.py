def koi(num):
    a = 0
    for i in num:
        a += i**2
    return a%10

print(koi(list(map(int, input().split()))))