import time
l1 = list(map(int,input("Enter the list : ").split()))
l1 = sorted(l1)
k = int(input("Enter the target sum : "))
begin = time.time()
l = 0
r = len(l1)-1
c = 0
while l < r:
    if l1[l] + l1[r] == k:
        print(True)
        c = 1
        break
    elif l1[l] + l1[r] > k:
        r = r-1
    elif l1[l] + l1[r] < k:
        l = l+1
if c < 1 :
    print(False)
end = time.time()
print(end - begin)