from fileOpen import txtOpen

def checkMath(responses, answers):
    score = 0
    outOf = len(answers)
    for i in range(len(answers)):
        if responses[i] == answers[i]:
            score += 1
    return score, outOf

def grade(file: str, answers: str):
    responses = txtOpen(file)
    answers = txtOpen(answers)
    score, outOf = checkMath(responses, answers)
    grade = (score/outOf) * 100
    grade = ("The math grade for this file is: {0:.2f}".format(round(grade,2)))
    return grade