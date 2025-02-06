l = list(map(int,input().split()))
i = 0
j = len(l) - 1
while i < j:
    if l[i] == 0 and l[j] > 0:
        l[i],l[j] = l[j],l[i]
    i += 1
    j -= 1
print(l)