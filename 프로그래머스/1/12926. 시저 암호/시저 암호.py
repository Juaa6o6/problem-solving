def solution(s, n):
    ans = ''
    for c in s:
        if c != ' ':
            if c.isupper():
                ans += chr(((ord(c) - ord('A')) + n) % 26 + ord('A'))
            else:
                ans += chr(((ord(c) - ord('a')) + n) % 26 + ord('a'))
        else:
            ans += c
            
    return ans