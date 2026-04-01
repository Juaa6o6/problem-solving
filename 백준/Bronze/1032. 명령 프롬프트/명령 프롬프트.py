n = int(input())
first = list(input())

for _ in range(n-1):
    word = input()
    for i in range(len(word)):
        if word[i] != first[i]:
            first[i] = '?'

print("".join(first))   