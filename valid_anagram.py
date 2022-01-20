def valid_anagram(s,t):
    s = sorted(s)
    t = sorted(t)
    for index in range(len(s)):
        if s[index] != t[index]:
            return False
    return True

# Given two strings s and t , 
# write a function to determine
#  if t is an anagram of s.


s = "rat"
t = 'car'
print("Is this an anagram", valid_anagram(s,t))
""" 
Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
 """