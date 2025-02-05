l = list(map(int,input("Enter the number : ").split()))
md = l[0]
for i in range(len(l)):
    for j in range(len(l)):
        temp = abs(l[i]) - abs(l[j])
        if md < temp:
            md = temp
print(md)