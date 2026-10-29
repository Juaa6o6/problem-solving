def solution(arr):
    ans = []
    for a in arr:
        if ans[-1:] == [a]:
            continue
        ans.append(a)
            
    return ans