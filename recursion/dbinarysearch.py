l = list(map(int,input("Enter the list : ").split()))
x = int(input("Enter the element to search in the list : "))
n = len(l)
i = 0
j = n-1
c = 0
while i<=j:
    m = (i+j) // 2
    if l[m] == x :
        print(f"Element found at index : {m}")
        c = c + 1
        break
    elif l[m] < x :
        i = m + 1
    elif l[m] > x :
        j = m - 1
if c == 0 :
    print("Element not found !")