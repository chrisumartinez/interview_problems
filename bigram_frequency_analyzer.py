""" 
Given a long string of text, do not ignore punctuation.
Break the text into individual words. Then, for every two words, count the frequency
 of words that come after those two words by storing them as a list of occurrences. 
 Return a string (with line breaks) that shows the frequency of those words.

For example, given:
I do not like green eggs and ham,
I do not like them, Sam-I-Am!
I do not like them with a fox,
I do not like them in a box.
I do not like them here or there,
I do not like them anywhere!
I do not like them, Sam-I-Am,
I do not like green eggs and ham!

Output:
 
I do : not (8) 
do not : like (8) 
not like : green (2) them, (2) them (4) 
like green : eggs (2) 
green eggs : and (2) 
eggs and : ham, (1) ham! (1) 
and ham, : I (1) 
ham, I : do (1) 
like them, : Sam-I-Am! (1) Sam-I-Am, (1) 
them, Sam-I-Am! : I (1) 
Sam-I-Am! I : do (1) 
like them : with (1) in (1) here (1) anywhere! (1) 
them with : a (1) 
with a : fox, (1) 
a fox, : I (1) 
fox, I : do (1) 
them in : a (1) 
in a : box. (1) 
a box. : I (1) 
box. I : do (1) 
them here : or (1) 
here or : there, (1) 
or there, : I (1) 
there, I : do (1) 
them anywhere! : I (1) 
anywhere! I : do (1) 
them, Sam-I-Am, : I (1) 
Sam-I-Am, I : do (1) 

Important:
Make sure your output string is formatted as shown. Do not trim any whitespace 
off the end of each line. At the end, the result should be the same as when you loop over frequency_dict.keys() """

def bigram_frequency_analyzer(text):

    #Break down the text into individual words:
    words = text.split()
    wordMap = {}
    output = ""


    #Create the dictionary for each two words, initalize right now to an empty hashmap:
    for index in range(len(words) - 1):

        #check edge case: if list is out of range
        if index >= len(words) - 2:
            break
            
        wordMap_key = words[index] + " " + words[index + 1]
        if wordMap_key not in wordMap:
            occurences = {}
            wordMap[wordMap_key] = occurences            

    #now lets look for occurences within each word:
    for index in range(len(words)-1):

        #check edge case: if list is out of range:
        if index >= len(words)-2:
            break

        #grab key:
        wordMap_key = words[index] + " " + words[index + 1]
        #grab word following the key:
        occurence_key = words[index + 2]
        
        #if the word is not found in key -> value: hashMap:
        if occurence_key not in wordMap[wordMap_key]:
            wordMap[wordMap_key][occurence_key] = 1
        else:
            wordMap[wordMap_key][occurence_key] += 1

    #Clean up output:
    for key in wordMap.keys():
        output += key + " : "
        for occurence_key in wordMap[key].keys():
            output += occurence_key + " "
            output +=  "("  + str(wordMap[key][occurence_key]) + ")" + " "
        output +=  "\n"


    return output



# test1 = "I do not like green eggs and ham, I do not like them, Sam-I-Am! I do not like them with a fox, I do not like them in a box. I do not like them here or there, I do not like them anywhere! I do not like them, Sam-I-Am, I do not like green eggs and ham!"
# print(bigram_frequency_analyzer(test1))
