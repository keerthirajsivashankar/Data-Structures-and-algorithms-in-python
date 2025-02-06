n = int(input())
l = list(map(int,input().split()))
k = int(input())
i = 0
j = k-1
m = l[0]
for i in range(n-k):
    j = i + (k-1)
    if m < sum(l[i:j+1]):
        m = sum(l[i:j+1])
print(m)
    