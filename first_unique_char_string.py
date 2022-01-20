# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.


def firstUniqChar(s: str) -> int:

    # add items to queue
    # make a frequency hash table for the items:
    hashTable = {}
    for item in s:
        if item not in hashTable:
            hashTable[item] = 1
        else:
            hashTable[item] += 1

    for item in hashTable:
        if hashTable[item] == 1:
            return s.index(item)
            
    return -1
    # once we find


s = "leetcode"
s2 = "loveleetcode"
s3 = "aabb"


print(firstUniqChar(s))  # Expected: 0
print(firstUniqChar(s2))  # Expected: 2
print(firstUniqChar(s3))  # Expected: -1
