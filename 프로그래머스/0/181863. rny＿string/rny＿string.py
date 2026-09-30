def solution(rny_string):
    answer = ['rn' if rny == 'm' else rny for rny in rny_string]
    return ''.join(answer)