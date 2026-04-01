n = int(input())
file = [input() for _ in range(n)]
wcnt = len(file[0])
search = ''
if n == 1:
    print(file[0])
else:
    for i in range(wcnt):
        flag = True
        for j in range(n-1):
            if file[j][i] != file[j+1][i]:
                search += '?'
                flag = False
                break

        if flag:
            search += file[j][i]
            
print(search)