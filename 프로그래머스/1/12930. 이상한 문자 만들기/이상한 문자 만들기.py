def solution(s):
    string = s.split(" ")
    ans = []
    for st in string:
        if st == " ": continue
        res = ''
        for i in range(len(st)):
            if i % 2 == 0:
                res += st[i].upper()
            else:
                res += st[i].lower()
        ans.append(res)
                
    return ' '.join(ans)