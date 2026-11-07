def solution(num):
    ans = []
    for i in range(len(num)):
        for j in range(i+1, len(num)):
            ans.append(num[i] + num[j])
    return sorted(set(ans))