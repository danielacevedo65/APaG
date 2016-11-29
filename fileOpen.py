import re

def fileOpen(file: str):
    file = open(file, 'r')
    fileContent = file.read()
    file.close()
    
    toParse = re.sub("[^A-Za-z0-9^']+",' ', fileContent)
    
    return toParse

def txtOpen(file):
    File = open(file, 'r')
    file = File.readlines()
    File.close()
    for i in range(len(file)):
        file[i] = file[i].strip()
    return file