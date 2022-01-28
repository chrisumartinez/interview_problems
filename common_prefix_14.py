def findPrefix(a, b):
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] != b[j]:
            break
        i += 1
        j += 1
    return a[:i]


# def commonPrefix(words):
#     prefix = words[0]
#     for word in words:
#         prefix = findPrefix(word, prefix)
#     return prefix


## DIVIDE AND CONQUER:


def commonPrefix(words, low, high):
    # base case: if `low` is more than `high`, return an empty string
    if low > high:
        return ""

    # base case: if `low` is equal to `high`, return the current string
    if low == high:
        return words[low]

    # find the mid-index
    mid = (low + high) // 2

    # partition => mergeSort:
    left = commonPrefix(words, low, mid)
    right = commonPrefix(words, mid + 1, high)

    return findPrefix(left, right)


def leetcode(strs):
    low = 0
    high = len(strs) - 1
    return commonPrefix(strs, low, high)


strs = ["flower", "flow", "flight"]
print(leetcode(strs))
