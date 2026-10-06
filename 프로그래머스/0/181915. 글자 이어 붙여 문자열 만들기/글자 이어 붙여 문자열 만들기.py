def solution(my_string, index_list):
    answer = ''
    str_dict = {}
    
    for i, s in enumerate(my_string):
        str_dict[i] = s
    
    for l in index_list:
        answer += str_dict[l]
    return answer