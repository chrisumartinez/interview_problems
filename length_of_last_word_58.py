def lengthOfLastWord(str):
    words = str.split()
    return len(words[-1])


s = "Hello World"
print(lengthOfLastWord(s))  # expected: 5
s2 = "   fly me   to   the moon  "
print(lengthOfLastWord(s2))  # expected: 4
