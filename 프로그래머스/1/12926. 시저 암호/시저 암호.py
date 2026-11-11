def solution(s, n):
    ans = ''
    for c in s:
        if c.isupper():
            ans += chr(((ord(c) - ord('A')) + n) % 26 + ord('A'))
        elif c.islower():
            ans += chr(((ord(c) - ord('a')) + n) % 26 + ord('a'))
        else:
            ans += c
            
    return ans