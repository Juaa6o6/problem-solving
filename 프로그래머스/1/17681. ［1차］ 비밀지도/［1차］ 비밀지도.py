def solution(n, arr1, arr2):
    ans = []
    for a, b in zip(arr1, arr2):
        line = format(a | b, f'0{n}b')
        ans.append(line.replace('1', '#').replace('0',' '))

    return ans