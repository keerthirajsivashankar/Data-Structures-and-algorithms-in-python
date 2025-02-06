s = input("Enter the string : ")
ns = []
for c in s:
    if c.isalpha():
        ns.append(c.lower())
i = 0 
j = len(ns) - 1
c = 0
while i < j :
    if ns[i] == ns[j]:
        i += 1
        j -= 1
    else:
        print("Not a palindrome ")
        c = 1
        break
if c == 0 :
    print("Palindrome")
print("".join(ns))

        