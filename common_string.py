def twoStrings(s1, s2):
    # check if substring exists in two strings:
    strSet = set()
    for letter in s1:
        if letter not in strSet:
            strSet.add(letter)
    flag = False
    for letter in s2:
        if letter in strSet:
            flag = True

    if not flag:
        return "NO"
    else:
        return "YES"


s1 = "hello"
s2 = "world"

print(twoStrings(s1, s2))
