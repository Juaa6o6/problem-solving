def solution(arr1, arr2):
    
    return [[c + r for c, r in zip(col, row)] for col, row in zip(arr1, arr2)]