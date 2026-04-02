def countvowels(s):
    print(s)
    if len(s)==0:
        return 0
    elif s[0] in "aeiouAEIOU":
        return 1+ countvowels(a[1:])
    else:
        return 0+countvowels(s[1:])

print(countvowels("what is in name"))
