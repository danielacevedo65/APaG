def ngram(text: str, n: int):
    text = text.split(" ")
    ngrams = []
          
    l = len(text)
    l = int(l/n)
    index = 0
      
    for i in range(l):
        ngrams.append(text[index:index+n])
        index += n-1
      
    return ngrams