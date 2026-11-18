def solution(n, arr1, arr2):
    ans = ['' for _ in range(n)]
    arr1 = list(map(lambda x:format(x, f'0{n}b'), arr1))
    arr2 = list(map(lambda x:bin(x)[2:].zfill(n), arr2))
    for i in range(n):
        for j in range(n):
            if arr1[i][j] == '1' or arr2[i][j] == '1':
                ans[i] += '#'
            else:
                ans[i] += ' '
            
    return ans