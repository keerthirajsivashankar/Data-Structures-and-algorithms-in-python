l1 = list(map(int,input("Enter the list : ").split()))
l2 = list(map(int,input("Enter the list : ").split()))
nl = []
i = 0 
j = 0
n = len(l1)
m = len(l2)
if n > m:
    while i < m :
        nl.append(l1[i])
        nl.append(l2[j])
        i += 1
        j += 1
    nl = nl + l1[i:]
elif m > n :
    while i < n :
        nl.append(l1[i])
        nl.append(l2[j])
        i += 1
        j += 1
    nl = nl + l2[i:]
else:
    while i < n :
        nl.append(l1[i])
        nl.append(l2[j])
        i += 1
        j += 1
print(nl)
    