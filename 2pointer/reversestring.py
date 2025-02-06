s = list(input())
i = 0
j = len(s)-1
while i < j :
    if s[i].isalpha() and s[j].isalpha():
        s[i],s[j] = s[j],s[i]
    else:
        if not s[i].isalpha():
            i += 1
            if s[i].isalpha() and s[j].isalpha():
                s[i],s[j] = s[j],s[i]
        elif not s[j].isalpha():
            j -= 1
            if s[i].isalpha() and s[j].isalpha():
                s[i],s[j] = s[j],s[i]
    i += 1
    j -= 1
print("".join(s))