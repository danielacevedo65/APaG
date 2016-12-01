import re, math
from collections import Counter

def cosine(A, B):
    intersection = set(A.keys()) & set(B.keys())
    print(intersection)
    numerator = getNumerator(A, B, intersection)
    denominator = getDenominator(A, B)
    print(numerator, denominator)
    return calculate(numerator, denominator)
    
def getNumerator(A, B, inter):
    num = 0
    for i in inter:
        num += (A[i] * B[i])
    return num

def getDenominator(A, B):
    Asum = 0
    for i in A.keys():
        Asum += A[i]**2
    Bsum = 0
    for i in B.keys():
        Bsum += B[i]**2
    return float(math.sqrt(Asum) * math.sqrt(Bsum))

def calculate(numerator, denominator):
    if denominator == 0.0:
        return denominator
    return float(numerator) / denominator
    
def countWords(gram):
    return Counter(re.compile(b'\w+').findall(gram))

def getSimilarity(A, B):
    return (cosine(countWords(A), countWords(B))) * 100