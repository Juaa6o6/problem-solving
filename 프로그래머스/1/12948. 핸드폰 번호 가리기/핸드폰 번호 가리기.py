def solution(lst):
    return '*'*len(lst[:-4])+''.join(lst[-4:])