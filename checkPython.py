import sys, subprocess
from fileOpen import txtOpen

def checkPython(responses, answers):
    score = 0
    outOf = len(answers)
    for i in range(len(answers)):
        if responses[i] == answers[i]:
            score += 1
    return score, outOf
    
def getPythonResults(file):
    results = subprocess.check_output([sys.executable, file]).decode().split("SPLIT")
    for i in range(len(results)):
        results[i] = results[i].strip()
    return results
    
def grade(file: str, answers: str):
    responses = getPythonResults(file)
    answers = txtOpen(answers)
    score, outOf = checkPython(responses, answers)
    grade = (score/outOf) * 100
    grade = ("The python grade for this file is: {0:.2f}".format(round(grade,2)))
    return grade