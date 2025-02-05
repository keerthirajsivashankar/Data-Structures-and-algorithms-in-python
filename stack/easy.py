l = list(map(int, input("Enter the list: ").split()))
i = 0
#l1 = [i for i in l if i not in l1]
while i < len(l):
    if l[i] in l[:i]:  
        l.pop(i)  
    else:
        i += 1  

print(l)
