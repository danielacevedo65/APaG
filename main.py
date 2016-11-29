import argparse, sys, os.path

from checkPlagiarism import checkPlagiarism

import checkSpelling, checkMath, checkPython, checkMultipleChoice

def main():
    parser = argparse.ArgumentParser(description="CS 585 Project")
    parser.add_argument('-f', action = "store", dest="file", type=str, help="File to be used")
    parser.add_argument('-p', action = "store", dest="checkPlagiarism", type=str, help="'yes' to check for plagirism, 'no' otherwise")
    parser.add_argument('-g', action = "store", dest="grade_style", type=str, help="What type of grading - spelling, math, python, mc")
    parser.add_argument('-as', action = "store", dest="answer_sheet", type=str, help="Answers to compare file to")
    parser = parser.parse_args()
    
    if parser.file == None:
        print("No file was inputted. Please enter '-f' followed by the name of a file")
        sys.exit(1)
    
    if not os.path.isfile(parser.file):
        print("File not found. Please input a valid file.")
        sys.exit(1)
    
    if parser.plagiarism == None and parser.grade_style == None:
        print("Please choose to check for plagirism ('-p') and/or grade a file ('-g')")
        sys.exit(1)
    
    if parser.grade_style != None:
        if parser.grade_style not in ['spelling', 'math', 'python', 'mc']:
            print("Grade style must be one of the following:\n        spelling\n        math\n        python\n        mc")
            sys.exit(1)
        
    if parser.answer_sheet != None:
        if not os.path.isfile(parser.answer_sheet):
            print("Answer sheet not found. Please input a valid file.")
            sys.exit(1)
    
    if parser.answer_sheet == None and parser.grade_style in ['math', 'python', 'mc']:
        print("For the selected grading style (" + str(parser.grade_style) + "), you must input an answer sheet (by using '-as')")
        sys.exit(1)
        
    if parser.plagiarism == "yes":
        isPlagiarized = checkPlagiarism(parser.file)  
        if isPlagiarized:
            print("No grading will be done to this file. The grade received is automatically assigned an F.")
            sys.exit(1)  
    
    if parser.grade_style == "spelling":
        print(checkSpelling.grade(parser.file))
    
    if parser.grade_style == "math":
        print(checkMath.grade(parser.file, parser.answer_sheet))
        
    if parser.grade_style == "python":
        print(checkPython.grade(parser.file, parser.answer_sheet))
        
    if parser.grade_style == "mc":
        print(checkMultipleChoice.grade(parser.file, parser.answer_sheet))
    
if __name__ == '__main__':
    main()