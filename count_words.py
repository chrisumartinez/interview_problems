""" 
Given a long text string, count the number of occurrences of each word. 
Ignore case. Assume the boundary of a word is whitespace - a " ", or a line break denoted by "\n". 
Ignore all punctuation, such as . , ~ ? !. Assume hyphens are part of a word - "two-year-old" and "two year old"
 are one word, and three different words, respectively. 

Return the word counts as a string formatted with line breaks,
in alphanumeric order.

Example:
"I do not like green eggs and ham,
I do not like them, Sam-I-Am"

Output:
i 2
do 2
not 2
like 2
green 1
eggs 1
and 1
ham 1
them 1
sam-i-am 1

Also Valid:
and 1
do 2
eggs 1
green 1
ham 1
i 2
like 2
not 2
sam-i-am 1
them 1 """



def count_words(text):
    #ignore case: make entire string lower case and strip punctuation:
    #translator = str.maketrans('','',string.punctuation)
    text = text.lower().replace(",", "").replace(".", "").replace("?", "").replace("!","").replace("~","")
    words = text.split()
    wordMap = {}
    output = ""

    #initialize wordMap with our key values:
    for word in words:
        #if key is not in the wordMap, then add it:
        if word not in wordMap.keys():
            wordMap[word] = 1
        else:
            #increment the counter in wordMap
            wordMap[word] += 1

    for key in wordMap:
        output += key + ' ' + str(wordMap[key]) + "\n"
    
    return output


# test1 = 'I do not like green eggs and ham, I do not like them, Sam-I-Am'
# test2 = "aslkdjld???,a. asdas!~"
# test4 = "nlsnkldandla"
# test5 = "br br br br"
# test6 = "two-year-old"

# print(count_words(test1))
# print(count_words(test2))
# print(count_words(test4))
# print(count_words(test5))
# print(count_words(test6))
