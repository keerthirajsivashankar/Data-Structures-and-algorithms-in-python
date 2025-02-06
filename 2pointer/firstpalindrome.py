def palindrome(s):
    i = 0 
    j = len(s)-1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True
l = list(map(str,input().split()))
c = 0 
for s in l:
    if palindrome(s):
        c = c + 1
        print(s)
        break
if c == 0:
    print("No palindrome found")
