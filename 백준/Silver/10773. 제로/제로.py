def main():
    k = int(input().strip())
    stack = []
    
    for _ in range(k):
        num = int(input().strip())
        if num == 0:
            if stack:
                stack.pop()
        else:
            stack.append(num)
    
    print(sum(stack))

if __name__ == "__main__":
    main()