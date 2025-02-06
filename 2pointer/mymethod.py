s = input("Enter the string : ")
ns = []
for c in s:
    if c.isalpha():
        ns.append(c.lower())
ns = "".join(ns)
ns = ns[::-1]
if ns == s :
    print("palindrome")
else:
    print("Not a palindrome")