def solution(arr):
    i = 0
    ans = [arr[i]]
    flag = arr[i]
    for _ in range(len(arr)-1):
        if flag != arr[i+1]:
            ans.append(arr[i+1])
            flag = arr[i+1]
        i += 1
            
    return ans