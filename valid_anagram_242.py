def isAnagram(s, t):
    # sort list:
    a = sorted(s)
    b = sorted(t)

    if len(b) != len(a):
        return False
    else:
        # check if each value is equal to each other:
        for index in range(0, len(a)):
            if a[index] != b[index]:
                return False

    return True


a = "anagram"
b = "nagaram"

print(isAnagram(a, b))  # Expected: true
