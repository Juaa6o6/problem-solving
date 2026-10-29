def solution(arr1, arr2):
    c, r = len(arr1), len(arr1[0])
    ans = [[0] * r for _ in range(c)]
    
    for i in range(c):
        for j in range(r):
            ans[i][j] = arr1[i][j] + arr2[i][j]
    return ans