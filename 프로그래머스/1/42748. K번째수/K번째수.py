def solution(array, commands):
    ans = []
    for com in commands:
        i, j, k = com
        ans.append(sorted(array[i-1:j])[k-1])
    return ans