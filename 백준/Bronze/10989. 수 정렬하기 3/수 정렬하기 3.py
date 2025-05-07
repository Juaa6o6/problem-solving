num = [0] * 10001
for _ in range(int(input())):
  n = int(input())
  num[n] += 1
  
for i in range(1, 10001):
  for _ in range(num[i]):
    print(i)