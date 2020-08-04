""" 
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Example 1:
Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".


Example 2:
Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".


Example 3:
Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".


Example 4:
Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".


Note:
1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.

Follow up:
Can you solve it in O(N) time and O(1) space? """


def truncateString(String):
    index = 0
    output1 = []
    while index < len(String):
        if String[index] == "#":
            if output1:
                output1.pop()
                index += 1
            else:
                index += 1
        else:
            output1.append(String[index])
            index += 1
    return output1


def backspaceCompare(String1, String2):
    """
    :type String1: str
    :type String2: str
    :rtype: bool
    """
    if truncateString(String1) == truncateString(String2):
        return True
    else:
        return False

    
sampleInput1A = "ab#"
sampleInput1B = "ab#"

test2A = "ab##"
test2B = "c#d#"

test3A = "a##c"
test3B = "#a#c"

test4A = "a#c"
test4B = "b"

print(backspaceCompare(sampleInput1A, sampleInput1B))
print(backspaceCompare(test2A, test2B))
print(backspaceCompare(test3A, test3B))
print(backspaceCompare(test4A, test4B))
