# Given two stings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.


def canConstruct(ransomNote: str, magazine: str) -> bool:
    r_list = []
    m_list = []
    r_list[:0] = ransomNote
    m_list[:0] = magazine

    # go through the list, once a correction cannot be made, then we return false:
    for letter in r_list:
        if letter in m_list:
            m_list.remove(letter)
        else:
            return False
    return True

    # for each final string:

    print(r_list)
    print(m_list)


ransomNote = "a"
magazine = "b"
ransomNote2 = "aa"
magazine2 = "ab"
magazine3 = "aab"


print(canConstruct(ransomNote, magazine))  # Expected false
