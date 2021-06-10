# You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

# Letters are case sensitive, so "a" is considered a different type of stone from "A".


# Example 1:

# Input: jewels = "aA", stones = "aAAbbbb"
# Output: 3
# Example 2:

# Input: jewels = "z", stones = "ZZ"
# Output: 0


# Constraints:

# 1 <= jewels.length, stones.length <= 50
# jewels and stones consist of only English letters.
# All the characters of jewels are unique.


def numJewelsInStones(jewels, stones):
    output = 0
    jewels_arr = list(jewels)
    for jewel in jewels_arr:
        for stone in stones:
            if jewel == stone:
                output += 1

    return output


jewels = "aA"
stones = "aAAbbbb"
jewels2 = "z"
stones2 = "ZZ"
print(numJewelsInStones(jewels, stones))  # Expected: 3
print(numJewelsInStones(jewels2, stones2))  # Expected: 0
