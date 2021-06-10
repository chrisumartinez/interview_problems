# Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

# You can use each character in text at most once. Return the maximum number of instances that can be formed.


# Example 1:


# Input: text = "nlaebolko"
# Output: 1
# Example 2:


# Input: text = "loonbalxballpoon"
# Output: 2
# Example 3:

# Input: text = "leetcode"
# Output: 0


def maxNumberOfBalloons(text):
    # if text length < 7 return 0:
    if len(text) < 7:
        return 0

    # grab valid characters, store into a dict:
    balloon_dict = {"a": 1, "b": 1, "l": 2, "o": 2, "n": 1}
    user_dict = {}
    count = 0

    # create dict from user input
    for letter in text:
        # if valid letter:
        if letter in balloon_dict:
            # check if letter exists in user_dict:
            if letter in user_dict:
                user_dict[letter] += 1
            else:
                user_dict[letter] = 1

    # get the minimum of values from user_dict:
    min_amount = min(user_dict[letter] for letter in user_dict)

    # if we got a minimum number higher than 0:
    if min_amount > 0:
        min_min_amount = min(user_dict["l"], user_dict["o"])
        # if min amount of o or l is lower than 2 times the other letter:, meaning we are done:
        if min_min_amount >= 2 * min_amount:
            return min_amount
        else:
            return min_min_amount // 2


ex = "nlaebolko"
ex2 = "loonbalxballpoon"
ex3 = "leetcode"
ex4 = "baoollnnololgbax"
print(maxNumberOfBalloons(ex))  # Expected: 1
print(maxNumberOfBalloons(ex2))  # Expected: 2
print(maxNumberOfBalloons(ex3))  # Expected: 0
print(maxNumberOfBalloons(ex4))  # Expected: 2
