def solution(array, commands):
    ans = []
    for com in commands:
        i, j, k = com
        arr = sorted(array[i-1:j])
        ans.append(arr[k-1])
    return ans