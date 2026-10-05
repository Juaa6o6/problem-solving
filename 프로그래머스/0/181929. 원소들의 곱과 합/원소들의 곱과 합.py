def solution(num_list):
    hap = 0
    gop = 1
    for num in num_list:
        hap += num
        gop *= num
    
    return 1 if gop < hap**2 else 0