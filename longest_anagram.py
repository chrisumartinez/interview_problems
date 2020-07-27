""" 
Given a string and a dictionary, find the longest entry in the dictionary that can be created by deleting characters from the string.

Example:
string = "batman", dictionary = ["bat", "aman", "antman"]

longest_anagram(string, dictionary) = "aman" """


#O(n^2)
def longest_anagram(string):

    #sort the string from a -> z:
    master_string = sorted(string)
    # Sort the entry of the 
    # for each entry in dictionary:
    longest_anagram_length = ""
    for entry in dictionary:
        entry_valid = True
        #sort the entry
        sorted_entry = sorted(entry)
        string = master_string[:]
        #Compare the values of both entry and string:
        for index in range(len(sorted_entry)):
            #Compare these:
            #print("Entry[Index]: ", sorted_entry[index], " String: ", string)
            #if found in the string
            if sorted_entry[index] in string:
                #pop it off, continue
                string.remove(sorted_entry[index])
            else:
                #not found, then anagram is invalid
                entry_valid = False
                break
        #check now if it was a valid anagram:
        if entry_valid:
            #check if it will be the longest length:
            if len(longest_anagram_length) < len(entry):
                longest_anagram_length = entry

        #print("Longest Anagram Length: ", longest_anagram_length)

    return longest_anagram_length


dictionary = ["bat", "aman", "antman"]
print(longest_anagram("batman"))
