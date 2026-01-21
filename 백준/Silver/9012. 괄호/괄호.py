T = int(input())

for _ in range(T):
    stack = []
    ps = input().strip()
    is_vps = True

    for char in ps:
        if char == '(':
            stack.append(char)
        else:
            if stack:
                stack.pop()
            else:
                is_vps = False
                break
                
    if is_vps and not stack:
        print("YES")
    else:
        print("NO")