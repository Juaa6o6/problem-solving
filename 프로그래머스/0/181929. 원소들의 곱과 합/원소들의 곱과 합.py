def solution(num_list):
    hap = 0
    gop = 1
    for num in num_list:
        hap += num
        gop *= num
    
    if gop < hap**2:
        return 1
    else:
        return 0