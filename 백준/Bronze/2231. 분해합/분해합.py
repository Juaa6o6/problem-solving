N = int(input())
for i in range(1, N):
    digit_sum = 0
    for digit in str(i):
        digit_sum += int(digit)
    if i + digit_sum == N:
        print(i)
        break
else:
    print(0)