def solution(my_string):
    answer = [int(s) for s in my_string if 48 <= ord(s) <= 57]
    return sum(answer)