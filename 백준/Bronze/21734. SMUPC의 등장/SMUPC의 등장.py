get=input("")
mylen=int(len(get))
add=0
for i in range(mylen):
    num=str(ord(get[i]))
    for j in range(len(num)):
        add=add+int(num[j])
    print(get[i]*add)
    add=0