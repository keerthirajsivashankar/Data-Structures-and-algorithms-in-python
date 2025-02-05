l = list(map(int,input("Enter the number : ").split()))
n = len(l)
nl = []
for val in l:
    if val > 0:
        nl.append(val)
nen = len(nl)
d = n - nen
for i in range(0,d):
    val = 0
    nl.append(val)
print(nl)