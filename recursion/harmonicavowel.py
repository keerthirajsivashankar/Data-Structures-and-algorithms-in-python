def lenofharmony(s):
    count = 0
    c = "bcdfghjklmnpqrstvwxy"
    for ch in s:
        if ch in c:
            count += 1
        elif ch in "0123456789":
            count += 1
    if len(s) < 5:
        return 0
    elif count > 0:
        return 0 
    else:
        i = 0
        j = 0
        maxx = float('-inf')
        while j < len(s):
            while s[i] > s[j]:
                i += 1
            j += 1
            maxx = max(maxx,len(s[i:j]))
    return maxx
s = input("Enter the string : ")
print(lenofharmony(s))