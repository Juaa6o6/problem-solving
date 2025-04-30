import sys
stdin = sys.stdin.read
N, K = map(int, stdin().split())

def factorial(n):
    ans = 1
    for i in range(2, n+1):
        ans *= i
    return ans
result = factorial(N) // (factorial(N-K) * factorial(K))
print(result)