def lise(l,x,i):
    if i == len(l):
        return -1
    elif l[i] == x :
        return i
    else:
        return lise(l,x,i+1)
l = list(map(int,input("Enter the list : ").split()))
x = int(input("Enter the element to search in the list : "))
i = 0
s = lise(l,x,i)
if s > -1:
    print(f"The the value {x} is at index {s}")
else:
    print("Not found!")