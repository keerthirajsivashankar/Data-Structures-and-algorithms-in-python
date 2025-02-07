def perfect(n,c=0,d=1):
    if d == n :
        return c == n
    if n % d == 0:
        c = c + d
    return perfect(n,c,d+1)
n = int(input())
print(perfect(n))