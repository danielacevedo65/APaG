from getSimilarity import getSimilarity
from htmlParser import strip_tags
from google import google

import time, urllib.parse

from ngram import ngram
from fileOpen import fileOpen

def checkPlagiarism(file):
    isPlagiarized = False
    grams = fileOpen(file)
    ngrams = ngram(grams, 9)
    ngrams = [' '.join(i) for i in ngrams]
    
    for i in range(len(ngrams)):
        toSearch = ngrams[i].encode('utf-8')

        googleResult = googleSearch(toSearch)
        
        for result in googleResult:
            similarity = getSimilarity(toSearch, strip_tags(result.description))
            if similarity >= 65:
                print("This file was plagiarized!")
                isPlagiarized = True
                return isPlagiarized
            
    print("This file is original with no evidence of plagiarism.")
    return isPlagiarized

def googleSearch(query):
    query = urllib.parse.quote_plus(query)
    time.sleep(10)
    return google.search(query, 1)
