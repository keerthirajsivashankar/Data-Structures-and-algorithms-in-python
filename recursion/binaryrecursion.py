def binary(l,x,i,j):
    m = (i + j) // 2
    if i > j :
        return print("Not found !")
    elif l[m] == x :
        return print(f"Elemnt found at the index : {m}")
    elif l[m] > x and j < len(n):
        j = m - 1
        return binary(l,x,i,j)
    elif l[m] < x and i > 0:
        i = m+1
        return binary(l,x,i,j)
    else:
        return print("Not found!")
l = list(map(int,input("Enter the list : ").split()))
x = int(input("Enter the element to search in the list : "))
n = len(l)
i = 0
j = n-1
binary(l,x,i,j)