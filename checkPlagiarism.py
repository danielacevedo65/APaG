from getSimilarity import getSimilarity
from htmlParser import strip_tags
from google import google


from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time, urllib.parse

from ngram import ngram
from fileOpen import fileOpen

def checkPlagiarism(file):
    isPlagiarized = False
    grams = fileOpen(file)
    ngrams = ngram(grams, 9)
    ngrams = [' '.join(i) for i in ngrams]
    
    for i in range(len(ngrams)):
        driver = webdriver.Firefox()
        toSearch = ngrams[i].encode('utf-8')
        driver.get("http://google.com")
        search = driver.find_element_by_name('q')
        search.send_keys(ngrams[i])
        search.send_keys(Keys.RETURN)
        
        googleResult = googleSearch(toSearch)
        search = driver.find_element_by_name('q')
        search.send_keys(ngrams[i])
        search.send_keys(Keys.RETURN)
        
        for result in googleResult:
            similarity = getSimilarity(toSearch, strip_tags(result.description))
            if similarity >= 70:
                print("This file was plagiarized!")
                isPlagiarized = True
                driver.quit()
                return isPlagiarized
            
        driver.quit()
            
    print("This file is original with no evidence of plagiarism.")
    return isPlagiarized

def googleSearch(query):
    query = urllib.parse.quote_plus(query)
    time.sleep(10)
    return google.search(query, 1)
