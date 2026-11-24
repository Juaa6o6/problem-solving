def dist(p, q):
    return abs(p[0] - q[0]) + abs(p[1] - q[1])
    
def solution(numbers, hand):
    key = {1: (0, 0), 2: (0, 1), 3: (0, 2),
          4: (1, 0), 5: (1, 1), 6: (1, 2),
          7: (2, 0), 8: (2, 1), 9: (2, 2),
          '*': (3, 0), 0: (3, 1), '#': (3, 2),}
    right, left = key['#'], key['*']
    main = 'R' if hand == 'right' else 'L'
    ans= ''
    
    for num in numbers:
        target = key[num]
        if num in [1, 4, 7]:
            h = 'L'
        elif num in [3, 6, 9]:
            h = 'R'
        else:
            rd = dist(right, target)
            ld = dist(left, target)
            if rd < ld:
                h = 'R'
            elif ld < rd:
                h = 'L'
            else:
                h = main
                
        ans += h
        if h == 'R':
            right = target
        elif h == 'L':
            left = target
            
    return ans