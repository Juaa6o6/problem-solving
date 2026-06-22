def solution(array):
    cnt = len(array)
    array.sort()
    return array[cnt//2]