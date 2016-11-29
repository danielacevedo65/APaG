import enchant
from fileOpen import fileOpen

def checkSpelling(text: str):
    text = text.split()
    checkifEnglish = enchant.Dict("en_US")
    score = 0
    outOf = 0
    for word in text:
        outOf += 1
        if checkifEnglish.check(word):
            score += 1
    return score, outOf

def grade(file: str):
    text = fileOpen(file)
    score, outOf = checkSpelling(text)
    grade = (score/outOf) * 100
    grade = ("The spelling grade for this file is: {0:.2f}".format(round(grade,2)))
    return grade
