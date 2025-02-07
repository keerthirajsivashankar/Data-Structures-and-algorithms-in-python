def prod(m,n):
    if n == 0 or m == 0:
        return -1
    elif n == 1:
        return m
    elif n > 1:
        return m + prod(m,n-1)
m = int(input())
n = int(input())
if m < 0 or n < 0:
    m = abs(m)
    n = abs(n) 
    print(-1*prod(m,n))
else:
    print(prod(m,n))