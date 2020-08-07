""" 
You are given a dictionary of words that indicate what sentiment score they have.
Given a list of strings, output a list of integers that indicates what total sentiment score the strings have.
Not all words are given a sentiment score, so some words or parts of words will not contribute to the sentiment score.

Example:

sentiments = {
 "amazing": 0.4,
 "sad": -0.8,
 "great": 0.8,
 "no": -0.1,
 "yes": 0.1,
 "angry": -0.7,
 "happy": 0.8
}

texts = [
  "that makes me so happy! amazing.", 
  "I'm so angry about this sad thing.", 
  "sad but true, amazing",
  "yes that is great, and amazing"
]




Should output:
[1.2000000000000002, -1.5, -0.4, 1.3] """

def sentiment_scores(sentiments, texts):
    #output a list of integers:
    #indicate with totat sentiment scores:
    emotions_list = []

    #for each text in texts:
    for text in texts:

        total_score = 0
        #split the entire string using no delimiter
        strings = text.split()
        
        #now for each string, check value within the sentiments lookup table:
        for string in strings:
            #strip the puncuation:
            string = string.replace("!", "").replace("?", "").replace(",","").replace(".","").replace("'","")
            #check if value exists within the lookup table:
            if string in sentiments:
                # adjust the total score:
                total_score += sentiments[string]
        
        #once we finish up tallying scores from strings, append the total score of the string:
        emotions_list.append(total_score)

    return emotions_list


sentiments = {
 "amazing": 0.4,
 "sad": -0.8,
 "great": 0.8,
 "no": -0.1,
 "yes": 0.1,
 "angry": -0.7,
 "happy": 0.8
}

texts = [
  "that makes me so happy! amazing.", 
  "I'm so angry about this sad thing.", 
  "sad but true, amazing",
  "yes that is great, and amazing"
]

print(sentiment_scores(sentiments, texts))