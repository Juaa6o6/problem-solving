def check(p, g):
    a, b = p
    c, d = g
    x, y = abs(a-c), abs(b-d)
    return x + y
    
def solution(numbers, hand):
    key = {'1': (0, 0), '2': (0, 1), '3': (0, 2),
          '4': (1, 0), '5': (1, 1), '6': (1, 2),
          '7': (2, 0), '8': (2, 1), '9': (2, 2),
          '*': (3, 0), '0': (3, 1), '#': (3, 2),}
    rx, ry = key['#']
    lx, ly = key['*']
    ans= ''
    
    for num in numbers:
        if num in [1, 4, 7]:
            ans += 'L'
            lx, ly = key[str(num)]
        elif num in [3, 6, 9]:
            ans += 'R'
            rx, ry = key[str(num)]
        else:
            rcnt = check([rx, ry], key[str(num)])
            lcnt = check([lx, ly], key[str(num)])
            if rcnt == lcnt:
                if hand == "right":
                    ans += 'R'
                    rx, ry = key[str(num)]
                elif hand == "left":
                    ans += 'L'
                    lx, ly = key[str(num)]
            elif rcnt < lcnt:
                ans += 'R'
                rx, ry = key[str(num)]
            elif lcnt < rcnt:
                ans += 'L'
                lx, ly = key[str(num)]
    return ans