import sys

def math(A, B):
    h = (A+B)*(A-B)
    return str(h)

A, B = map(int, sys.stdin.readline().split())
sys.stdout.write(math(A, B))