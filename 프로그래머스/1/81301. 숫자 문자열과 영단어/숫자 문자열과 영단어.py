def solution(s):
    num = {
    'zero': 0, '0': 0,
	'one': 1, '1': 1,
	'two': 2, '2': 2,
	'three': 3, '3': 3,
	'four': 4, '4': 4,
	'five': 5, '5': 5,
	'six': 6, '6': 6,
	'seven': 7, '7': 7,
	'eight': 8, '8': 8,
	'nine': 9, '9': 9
    }
    ans = []
    n = ''
    for c in s:
        n += c
        if n in num:
            ans.append(str(num[n]))
            n = ''
    
    return int(''.join(ans))